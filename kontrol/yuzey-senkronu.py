#!/usr/bin/env python3
"""Yüzey senkronu ve format kapısı — §15.2 adım 6'nın makine karşılığı.

DENETIM-v1.3.md kök neden M5-Y1: "üç normatif yüzey, tek sürüm damgası, sıfır senkron
kuralı." v1.4 kuralı DÜZYAZI olarak yazdı; v1.5 ve v1.6 ikisi de kuralı ihlal etti
(§6.2'deki gömülü STATE.md şablonu ile kurulum/proje/STATE.md iki yönde birden ayrıştı).
Düzyazı kural tutmadı. R2'nin doktrini gereği kural kâğıttan çıkarılıp buraya kondu.

Kullanım:  python3 kontrol/yuzey-senkronu.py
Çıkış:     0 = tüm kapılar geçti, 1 = en az bir kapı KALDI.

Bu betiğin kendi kuralı: hiçbir kapı "kontrol edecek şey bulamadım" diye SESSİZCE
geçemez. Bulamazsa KALDI verir — sessiz geçiş, v1.3 denetiminin "denetim koşturuldu,
kapı koşturulmadı" bulgusunun ta kendisidir.
"""
import re
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
TALIMAT = KOK / "AJAN-ISLETIM-TALIMATI.md"
TALIMAT_KOPYA = KOK / "kurulum/claude/AJAN-ISLETIM-TALIMATI.md"
STATE = KOK / "kurulum/proje/STATE.md"
CLAUDE_MD = KOK / "kurulum/claude/CLAUDE.md"
SKILL = KOK / "kurulum/claude/skills/ajan-isletim/SKILL.md"
HTML = KOK / "ajan-isletim-talimati.html"

sonuclar = []


def kapi(ad):
    def sarmala(fn):
        try:
            hatalar = fn()
        except Exception as e:  # bir kapının patlaması da KALDI'dır, sessizlik değil
            hatalar = [f"kapı çalışamadı: {type(e).__name__}: {e}"]
        sonuclar.append((ad, hatalar))
        return fn
    return sarmala


def oku(p):
    return p.read_text(encoding="utf-8")


def gomulu_sablon(metin):
    """§6.2'deki ```markdown çitinin içeriğini döndürür."""
    satir = metin.split("\n")
    i62 = next(i for i, l in enumerate(satir) if l.startswith("### 6.2"))
    bas = next(i for i in range(i62, len(satir)) if satir[i].strip() == "```markdown")
    son = next(i for i in range(bas + 1, len(satir)) if satir[i].strip() == "```")
    return "\n".join(satir[bas + 1:son])


def kanonik_surum(metin):
    m = re.search(r"^#\s+AJAN İŞLETİM TALİMATI\s+—\s+(v\d+\.\d+(?:\.\d+)?)\s*$", metin, re.M)
    if not m:
        raise AssertionError("başlıktan sürüm okunamadı")
    return m.group(1)


@kapi("1. Sürüm senkronu — türev yüzeyler")
def _():
    surum = kanonik_surum(oku(TALIMAT))
    h = []
    for p in (CLAUDE_MD, SKILL):
        bulunan = set(re.findall(r"v\d+\.\d+(?:\.\d+)?", oku(p)))
        if not bulunan:
            h.append(f"{p.relative_to(KOK)}: hiç sürüm damgası yok (senkron doğrulanamaz)")
        elif bulunan != {surum}:
            h.append(f"{p.relative_to(KOK)}: {sorted(bulunan)} ≠ {surum}")
    html = oku(HTML)
    kunye = re.search(r"Sürüm\s+(v\d+\.\d+(?:\.\d+)?)", html)
    if not kunye:
        h.append(f"{HTML.name}: künyede sürüm bulunamadı")
    elif kunye.group(1) != surum:
        h.append(f"{HTML.name}: künye {kunye.group(1)} ≠ {surum}")
    # altbilgi de bir sürüm yüzeyi: v1.6'da künye türetildi ama altbilgi v1.0'da kaldı
    alt = re.search(r"<footer>.*?—\s+(v\d+\.\d+(?:\.\d+)?)", html, re.S)
    if not alt:
        h.append(f"{HTML.name}: altbilgide sürüm bulunamadı")
    elif alt.group(1) != surum:
        h.append(f"{HTML.name}: altbilgi {alt.group(1)} ≠ {surum}")
    return h


@kapi("2. İki talimat kopyası birebir")
def _():
    if oku(TALIMAT) != oku(TALIMAT_KOPYA):
        return [f"{TALIMAT.name} ile {TALIMAT_KOPYA.relative_to(KOK)} ayrışmış"]
    return []


@kapi("3. Gömülü STATE.md şablonu == kurulum/proje/STATE.md")
def _():
    gomulu = gomulu_sablon(oku(TALIMAT))
    tek = oku(STATE).rstrip("\n")
    if not gomulu.strip():
        return ["§6.2 çiti boş — karşılaştırılacak şablon yok"]
    if gomulu != tek:
        g = set(re.findall(r"^## .+$", gomulu, re.M))
        t = set(re.findall(r"^## .+$", tek, re.M))
        fark = sorted((g - t) | (t - g))
        return ["§6.2 gömülü şablonu ile kurulum/proje/STATE.md ayrışmış"] + [
            f"  yalnız bir tarafta: {b}" for b in fark
        ]
    return []


@kapi("4. Kapanış damgası == başlık sürümü")
def _():
    metin = oku(TALIMAT)
    surum = kanonik_surum(metin)
    m = re.search(r"\*\*Belge sonu — (v\d+\.\d+(?:\.\d+)?)\.\*\*", metin)
    if not m:
        return ["kapanış damgası bulunamadı"]
    if m.group(1) != surum:
        return [f"kapanış damgası {m.group(1)} ≠ başlık {surum}"]
    return []


@kapi("5. Kırık §-atfı yok")
def _():
    metin = oku(TALIMAT)
    # başlıklar iki biçimde: "## 5. KAPSAM ..." (sayıdan sonra nokta) ve
    # "### 5.4 KAPSAM UYUMU ..." (nokta yok). İkisini de yakala.
    basliklar = set(re.findall(r"^#{2,4}\s+(\d+(?:\.\d+)*)\.?\s", metin, re.M))
    altbolum = {b for b in basliklar if "." in b}
    if len(basliklar) < 10 or len(altbolum) < 10:
        return [f"yalnız {len(basliklar)} başlık ({len(altbolum)} alt bölüm) "
                f"ayrıştırılabildi — ayrıştırıcı bozuk"]
    atiflar = set(re.findall(r"§\s?(\d+(?:\.\d+)*)", metin))
    if not atiflar:
        return ["hiç §-atfı bulunamadı — ayrıştırıcı bozuk"]
    kirik = sorted(atiflar - basliklar, key=lambda s: [int(x) for x in s.split(".")])
    return [f"kırık atıf: §{k}" for k in kirik]


@kapi("6. Başlık sayı iddiası == içerik sayısı (ana akış)")
def _():
    satir = oku(TALIMAT).split("\n")
    i = next((i for i, l in enumerate(satir) if l.startswith("## 2. ANA AKIŞ")), None)
    if i is None:
        return ["§2 başlığı bulunamadı"]
    iddia = re.search(r"(\d+)\s+adım", satir[i])
    if not iddia:
        return ["§2 başlığında sayı iddiası bulunamadı"]
    son = next(j for j in range(i + 1, len(satir)) if satir[j].startswith("## "))
    gercek = len([l for l in satir[i:son] if re.match(r"^\[\d+\]", l)])
    if gercek == 0:
        return ["§2'de [n] biçiminde adım bulunamadı — sayaç bozuk"]
    if int(iddia.group(1)) != gercek:
        return [f"§2 başlığı {iddia.group(1)} adım diyor, gövdede {gercek} adım var"]
    return []


@kapi("7. Sözlükte ölü terim yok")
def _():
    metin = oku(TALIMAT)
    i = metin.find("## EK — HIZLI SÖZLÜK")
    if i < 0:
        return ["sözlük bölümü bulunamadı"]
    sozluk = metin[i:]
    # v1.5'te sistemden silinen mekanizmalar (DENETIM-v1.3.md R4)
    olu = ["KO / VT", "Kullanım Oranı", "Verimli Tur", "T_dalga", "T_asgari", "kalibrasyon tablosu"]
    return [f"sözlükte ölü terim tanımlı: {t}" for t in olu if t in sozluk]



# ---------------------------------------------------------------------------
# Kapı 8–11: ANLAMSAL senkron. v1.6.1 denetiminin hükmü: kapı 1–7 ucuz sınıfı
# (sürüm damgası, birebir kopya, kırık atıf, ölü terim) kapatıyordu; bu belgeyi
# üç sürüm üst üste ısıran sınıf ise anlamsaldı — çözülen ama yanlış hedefli
# atıf, bölümüyle çelişen şablon, gövdesiyle uyuşmayan sayı, kataloğa girmemiş rol.
# ---------------------------------------------------------------------------

SAYI = {"bir": 1, "iki": 2, "üç": 3, "dört": 4, "beş": 5, "altı": 6, "yedi": 7,
        "sekiz": 8, "dokuz": 9, "on": 10}


def _blok(metin, bas, son):
    i = metin.index(bas)
    j = metin.index(son, i + len(bas))
    return metin[i:j]


@kapi("8. Sözlük sayı iddiası == gövdedeki liste uzunluğu")
def _():
    metin = oku(TALIMAT)
    # (sözlük terimi, iddiayı çeken desen, sayılacak blok, madde deseni)
    iddialar = [
        ("Anomali", r"tetikleyen (\w+) durumdan biri",
         ("Anomali tanımı", "**Üyeler:**"), r"^\[ \]"),
        ("İzole alt görev", r"§7\.1'deki (\w+) testi",
         ("### 7.1", "Dördü de \"evet\" değilse"), r"^\[ \]"),
        ("Büyük adım", r"§8\.1'deki (\w+) tetikleyiciden",
         ('"Büyük adım" tanımı', "Bunların hiçbiri yoksa"), r"^\[ \]"),
    ]
    h = []
    for terim, desen, (bas, son), madde in iddialar:
        satir = next((l for l in metin.split("\n")
                      if l.startswith(f"| **{terim}**")), None)
        if satir is None:
            h.append(f"sözlükte '{terim}' bulunamadı — ayrıştırıcı bozuk")
            continue
        m = re.search(desen, satir)
        if not m:
            h.append(f"'{terim}' sözlük satırından sayı iddiası çıkarılamadı")
            continue
        ham = m.group(1)
        iddia = SAYI.get(ham.lower(), int(ham) if ham.isdigit() else None)
        if iddia is None:
            h.append(f"'{terim}': '{ham}' sayıya çevrilemedi")
            continue
        gercek = len(re.findall(madde, _blok(metin, bas, son), re.M))
        if gercek == 0:
            h.append(f"'{terim}': sayılacak madde bulunamadı — sayaç bozuk")
        elif gercek != iddia:
            h.append(f"sözlük '{terim}' için {iddia} diyor, gövdede {gercek} madde var")
    return h


@kapi("9. §13 şablonlarında ölü mekanizma yok")
def _():
    metin = oku(TALIMAT)
    sablonlar = _blok(metin, "## 13. ŞABLONLAR", "## 14. KONTROL LİSTELERİ")
    # v1.4–v1.5'te sistemden çıkarılan mekanizmalar. §13 kopyala-yapıştır bölümüdür:
    # buradaki metin ajana birebir gider, yani iki kopyadan OPERATİF olanıdır.
    olu = ["Toplam süre", "karmaşıklık/kritiklik", "payını %", "T_dalga", "T_i ",
           "kalibrasyon tablosu", "Kullanım Oranı", "Verimli Tur"]
    return [f"§13 şablonunda ölü mekanizma: {m}" for m in olu if m in sablonlar]


@kapi("10. Nöbetçi atıflar doğru bölüme gidiyor")
def _():
    metin = oku(TALIMAT)
    # Çözülen ama YANLIŞ HEDEFLİ atıf, kapı 5'e görünmez. Yüksek trafikli
    # olanlar burada kilitlenir: her biri bir denetim bulgusudur (B3, B7).
    nobetci = [
        (r"`\.ajan-ucus\.log`, §(\d+\.\d+)", "2.0",
         "uçuş kaydı §2.0'da tanımlı; §2.2 kapsam değişikliğidir"),
        (r"bölümleri güncellendi \(§(\d+\.\d+)\)", "6.3",
         "§6.2 boş şablondur; yazma protokolü §6.3'tedir"),
    ]
    h = []
    for desen, gereken, neden in nobetci:
        m = re.search(desen, metin)
        if not m:
            h.append(f"nöbetçi atıf bulunamadı: {desen} — ayrıştırıcı bozuk")
        elif m.group(1) != gereken:
            h.append(f"§{m.group(1)} yerine §{gereken} olmalı — {neden}")
    return h


# Rol adı -> agents/ dosyası. Beyin orkestratördür (ana ajan), dosya gerekmez.
ROL_DOSYA = {
    "Beyin (Orkestratör)": None,
    "Boşluk-Planlayıcı": "bosluk-planlayici.md",
    "Uzman İşçi": "uzman-isci.md",
    "Doğrulayıcı": "dogrulayici.md",
    "Meta-Doğrulayıcı": "meta-dogrulayici.md",
    "Nihai Testçi": "nihai-testci.md",
    "Gözcü (Shadow)": "gozcu.md",
    "Öğretmen": "ogretmen.md",
    "Kapsam Belirleyici": "kapsam-belirleyici.md",
    "Kapsam Uyumu Denetçisi": "kapsam-uyumu-denetcisi.md",
    "Karantina Okuyucu": "karantina-okuyucu.md",
    "Hipotez Üretici": "hipotez-uretici.md",
    "Çürütücü": "curutucu.md",
}
# §3.1 dışında doğurulan, dosyası olan roller
EK_DOSYA = {"kurul-uyesi.md"}

# v1.6.1 denetiminin AÇIK bulguları (B1, B6). Bu küme YALNIZ KÜÇÜLEBİLİR:
# yeni bir rol dosyasız kalırsa kapı KALDI verir. Tasarım işi bitince buradan silinir.
ACIK_B1_B6 = {"gozcu.md", "kapsam-belirleyici.md", "kapsam-uyumu-denetcisi.md"}


@kapi("11. Rol kataloğu == agents/ dosyaları (açık küme büyümüyor)")
def _():
    metin = oku(TALIMAT)
    tablo = _blok(metin, "### 3.1", "**Aynı rollerin")
    roller = [m.group(1) for m in re.finditer(r"^\| \*\*(.+?)\*\*", tablo, re.M)]
    if len(roller) < 10:
        return [f"yalnız {len(roller)} rol ayrıştırıldı — ayrıştırıcı bozuk"]
    h = []
    for r in roller:
        if r not in ROL_DOSYA:
            h.append(f"§3.1'de kataloglanmamış rol: {r} — ROL_DOSYA'ya eklenmeli")
            continue
        d = ROL_DOSYA[r]
        if d is None:
            continue
        if not (KOK / "kurulum/claude/agents" / d).exists() and d not in ACIK_B1_B6:
            h.append(f"'{r}' rolünün tanım dosyası yok ({d}) — §3: dosyasız rol "
                     f"tam araç setiyle doğar, YASAK sütunu uygulanmaz")
    beklenen = {d for d in ROL_DOSYA.values() if d} | EK_DOSYA
    mevcut = {f.name for f in (KOK / "kurulum/claude/agents").glob("*.md")}
    for f in sorted(mevcut - beklenen):
        h.append(f"kataloğa bağlanmamış ajan dosyası: {f}")
    for d in sorted(ACIK_B1_B6 & mevcut):
        h.append(f"{d} artık var — ACIK_B1_B6'dan silin (küme yalnız küçülür)")
    return h


kalan = 0
print("YÜZEY SENKRONU VE FORMAT KAPISI\n" + "=" * 46)
for ad, hatalar in sonuclar:
    if hatalar:
        kalan += 1
        print(f"KALDI  {ad}")
        for h in hatalar:
            print(f"       → {h}")
    else:
        print(f"GEÇTİ  {ad}")
print("=" * 46)
if kalan:
    print(f"{kalan} kapı KALDI — §15.2 adım 6 tamamlanmadan teslim edilemez.")
    sys.exit(1)
print(f"{len(sonuclar)} kapının tamamı geçti.")

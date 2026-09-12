#!/usr/bin/env python3
"""Kapı testi — yuzey-senkronu.py'nin kapıları gerçekten yakalıyor mu?

Her kapı için kasıtlı bir kusur enjekte edilir, kapının KALDI verdiği doğrulanır,
sonra dosyalar geri alınır. Hiç KALDI vermeyen bir kapı SAHTE'dir: v1.3 denetiminin
"denetim koşturuldu, kapı koşturulmadı" bulgusunun aynısını üretir.

Kullanım:  python3 kontrol/kapi-testi.py
Çıkış:     0 = her kapı yakalıyor, 1 = en az bir kapı sahte.
"""
import re
import subprocess
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
DOSYALAR = [
    "AJAN-ISLETIM-TALIMATI.md",
    "kurulum/claude/AJAN-ISLETIM-TALIMATI.md",
    "kurulum/proje/STATE.md",
    "kurulum/claude/CLAUDE.md",
    "kurulum/claude/skills/ajan-isletim/SKILL.md",
    "ajan-isletim-talimati.html",
]
YEDEK = {f: (KOK / f).read_bytes() for f in DOSYALAR}
TALIMATLAR = DOSYALAR[:2]


def geri():
    for f, b in YEDEK.items():
        (KOK / f).write_bytes(b)


def calistir():
    r = subprocess.run([sys.executable, str(KOK / "kontrol/yuzey-senkronu.py")],
                       capture_output=True, text=True, cwd=KOK)
    return r.returncode, re.findall(r"^KALDI  (\d+)\.", r.stdout, re.M)


def degistir(dosyalar, eski, yeni):
    for f in dosyalar:
        p = KOK / f
        m = p.read_text(encoding="utf-8")
        if eski not in m:
            raise AssertionError(f"{f}: enjekte edilecek desen bulunamadı: {eski!r}")
        p.write_text(m.replace(eski, yeni, 1), encoding="utf-8")


TESTLER = [
    ("1", "türev yüzey sürümü geride kaldı",
     lambda: degistir(["kurulum/claude/CLAUDE.md"], "v1.6.1", "v1.5")),
    ("2", "iki talimat kopyası ayrıştı",
     lambda: degistir(["kurulum/claude/AJAN-ISLETIM-TALIMATI.md"], "# AJAN", "# ayrışma\n# AJAN")),
    ("3", "gömülü şablon ile tek dosya ayrıştı",
     lambda: degistir(["kurulum/proje/STATE.md"], "## 6. Kapsam kayıtları", "## 6. Zaman kayıtları")),
    ("4", "kapanış damgası bayat",
     lambda: degistir(TALIMATLAR, "**Belge sonu — v1.6.1.**", "**Belge sonu — v1.3.**")),
    ("5", "kırık §-atfı",
     lambda: degistir(TALIMATLAR, "(§10.2,", "(§10.99,")),
    ("6", "başlık sayı iddiası içerikle tutmuyor",
     lambda: degistir(TALIMATLAR, "## 2. ANA AKIŞ — baştan sona 11 adım",
                      "## 2. ANA AKIŞ — baştan sona 10 adım")),
    ("7", "sözlükte ölü terim",
     lambda: degistir(TALIMATLAR, "| **Kural enflasyonu**",
                      "| **KO / VT** | Kullanım Oranı = kullanılan/tahsis. |\n| **Kural enflasyonu**")),
]

print("KAPI TESTİ — her kapı yakalaması gerekeni yakalıyor mu?\n" + "=" * 54)
sahte = []
try:
    for no, ad, mutasyon in TESTLER:
        geri()
        mutasyon()
        kod, kalanlar = calistir()
        if kod == 1 and no in kalanlar:
            print(f"YAKALADI  kapı {no}: {ad}")
        else:
            sahte.append(no)
            print(f"KAÇIRDI   kapı {no}: {ad}   (çıkış={kod}, KALDI={kalanlar})")
finally:
    geri()

kod, _ = calistir()
print("=" * 54)
print(f"temiz ağaç: {'geçiyor' if kod == 0 else 'GEÇMİYOR'}")
if sahte or kod != 0:
    print(f"SAHTE KAPI: {sahte or '—'}; temiz ağaç çıkışı: {kod}")
    sys.exit(1)
print(f"{len(TESTLER)} kapının tamamı gerçekten çalışıyor.")

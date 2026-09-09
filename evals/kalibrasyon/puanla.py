#!/usr/bin/env python3
"""Tohumlanmış hata testini puanlar: yakalama (recall) ve tuzak kontrolü.

Kullanım:
    python3 puanla.py <rapor.md> [<rapor2.md> ...]

Her tohum için, o tohumu tespit etmiş bir raporun kaçınılmaz olarak içereceği
ayırt edici işaretler tanımlıdır. Bir tohum, işaret gruplarının HEPSİ raporda
geçiyorsa bulunmuş sayılır (ör. hem "36 ay" hem "24" geçmeli).

Bu betik yakalamayı otomatik ölçer. İsabet (precision) otomatik ölçülemez —
raporlanan bulguların gerçek olup olmadığı okunarak değerlendirilir; betik
yalnızca tuzağın (P1) raporlanıp raporlanmadığını işaretler.
"""

import re
import sys
from pathlib import Path

# (kod, madde, açıklama, [ [alternatif1, alternatif2...], [grup2...] ])
# Bir tohum bulundu sayılır: her grup için en az bir alternatif raporda geçmeli.
TOHUMLAR = [
    ("T1", "01", "36 ay / 24 ay süre uyuşmazlığı",
     [["36 ay", "36 (otuz altı)", "otuz altı ay"], ["24 ay", "24 (yirmi dört)", "yirmi dört ay", " 24 "]]),
    ("T2", "02", "Ek-B toplamı 68.000 ≠ 72.000",
     [["68.000", "68000"], ["72.000", "72000"]]),
    ("T3", "03", "Ek-C mevcut değil",
     [["Ek-C", "EK-C", "Ek C"]]),
    ("T4", "04", "Nova A.Ş. ↔ Nova Ltd. Şti.",
     [["Ltd. Şti.", "Ltd Şti", "Limited"], ["A.Ş.", "Anonim"]]),
    ("T5", "06", "Lisans bedeli OPEX ↔ CAPEX",
     [["OPEX", "İşletme gideri", "işletme gideri"], ["CAPEX", "Yatırım harcaması", "yatırım harcaması"]]),
    ("T6", "09", "Rapor yükümlülüğü ↔ tavsiye",
     [["tavsiye"], ["yükümlü"]]),
    ("T7", "16", "Teminat oranı boş",
     [["teminat", "Teminat"], ["%....", "%......", "boş", "doldurulma", "belirtilme"]]),
    ("T8", "17", "Meridyen Lojistik kalıntısı",
     [["Meridyen"]]),
    ("T9", "18", "Tam 10 gün açıkta",
     [["10 gün"], ["az", "fazla", "eşit", "kapsa", "açık", "boş"]]),
    ("T10", "26", "Özet ↔ Ek-A onay şartı",
     [["özet", "Özet", "ÖZET"], ["A.1", "Ek-A", "onay", "bütçe"]]),
    ("T11", "09", "Ters yönlü istisna: Madde 6.4 ölü hüküm",
     [["6.4", "6/4"], ["6.2", "6/2", "30 gün"], ["60 gün", "erteleme", "ertele"]]),
]

# Tuzak P1: Madde 4.1 ↔ 5.1. Saklı tutma DOĞRU yönde (genel kural özel kurala
# boyun eğiyor), dolayısıyla çelişki olarak raporlanmamalı.
TUZAK_ISARET = [["Madde 4", "Madde 4.1"], ["Madde 5", "Madde 5.1", "12 ay", "asgari süre"]]
TUZAK_IDDIA = ["çelişki", "çelişkili", "çakış", "tutarsız", "geçersiz kıl", "ölü hüküm"]


def grup_gecti(metin: str, alternatifler: list[str]) -> bool:
    return any(alt.lower() in metin.lower() for alt in alternatifler)


def puanla(yol: Path) -> dict:
    metin = yol.read_text(encoding="utf-8")
    bulunan, kacan = [], []
    for kod, madde, aciklama, gruplar in TOHUMLAR:
        if all(grup_gecti(metin, g) for g in gruplar):
            bulunan.append((kod, madde, aciklama))
        else:
            kacan.append((kod, madde, aciklama))

    # Tuzak: iki maddeye birlikte atıf + çelişki dili
    tuzak_atif = all(grup_gecti(metin, g) for g in TUZAK_ISARET)
    tuzak_iddia = grup_gecti(metin, TUZAK_IDDIA)
    tuzak_riski = tuzak_atif and tuzak_iddia

    return {
        "dosya": yol.name,
        "yol": str(yol),
        "bulunan": bulunan,
        "kacan": kacan,
        "yakalama": len(bulunan) / len(TOHUMLAR),
        "tuzak_riski": tuzak_riski,
        "uzunluk": len(metin),
    }


def yazdir(s: dict) -> None:
    print(f"\n{'=' * 64}")
    print(f"  {s['yol']}")
    print(f"{'=' * 64}")
    print(f"  Yakalama : {len(s['bulunan'])}/{len(TOHUMLAR)}  (%{s['yakalama'] * 100:.0f})")
    print(f"  Rapor    : {s['uzunluk']} karakter")
    if s["bulunan"]:
        print("\n  Bulunan tohumlar:")
        for kod, madde, aciklama in s["bulunan"]:
            print(f"    ✓ {kod} · madde {madde} · {aciklama}")
    if s["kacan"]:
        print("\n  Kaçan tohumlar:")
        for kod, madde, aciklama in s["kacan"]:
            print(f"    ✗ {kod} · madde {madde} · {aciklama}")
    print(f"\n  Tuzak (P1 · Madde 4↔5 meşru istisna):")
    if s["tuzak_riski"]:
        print("    ⚠ Rapor bu ikiliye çelişki dilinde değiniyor — elle kontrol et,")
        print("      çelişki olarak raporlandıysa isabet oranı düşer.")
    else:
        print("    ✓ Çelişki olarak raporlanmış görünmüyor.")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    sonuclar = []
    for arg in sys.argv[1:]:
        yol = Path(arg)
        if not yol.exists():
            print(f"Bulunamadı: {yol}")
            continue
        s = puanla(yol)
        sonuclar.append(s)
        yazdir(s)
    if len(sonuclar) > 1:
        print(f"\n{'=' * 64}\n  KARŞILAŞTIRMA\n{'=' * 64}")
        for s in sonuclar:
            tuzak = "riskli" if s["tuzak_riski"] else "temiz"
            print(f"  {len(s['bulunan'])}/10  tuzak:{tuzak:7s}  {s['dosya']}")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

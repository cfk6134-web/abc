# Kalibrasyon Cevap Anahtarı

`sozlesme-tohumlu.md` dosyasına **10 bilinen hata** ve **1 tuzak** yerleştirilmiştir.

Bu dosyayı denetimi yapan tarafa vermeyin — yalnızca sonucu değerlendirirken kullanın.

## Ölçülen iki oran

- **Yakalama (recall):** 10 tohumdan kaçı bulundu?
- **İsabet (precision):** Raporlanan bulguların kaçı gerçek (tohum ya da doğrulanabilir bir kusur), kaçı uydurma?

Yalnızca yakalamayı ölçmek yanıltıcıdır: her cümleye çelişki diyen bir kurgu %100 yakalar ama kullanılamaz.

## Tohumlar

| # | Hedef madde | Konum | Tohum |
|---|---|---|---|
| T1 | 01 · Tarihsel | Madde 3.1 | 01.04.2025 – 31.03.2027 aralığı 24 aydır; metin "36 ay" diyor |
| T2 | 02 · Sayısal | Ek-B | Kalemler 42.000 + 18.000 + 12.000 = 72.000; tabloda "TOPLAM 68.000". Ayrıca Madde 6.1 aylık bedeli 72.000 TL olarak veriyor |
| T3 | 03 · Referans | Madde 9.1 | "Ek-C'de düzenlenmiştir" deniyor; belgede yalnızca Ek-A ve Ek-B var |
| T4 | 04 · Varlık | Madde 1.1 ↔ 11.1 | Taraf "Nova Bilişim Teknolojileri A.Ş." tanımlı; Madde 11'de "Nova Bilişim Ltd. Şti." |
| T5 | 06 · Sınıflandırma | Ek-B ↔ Madde 7.1 | Lisans yenileme bedeli Ek-B'de OPEX, Madde 7'de CAPEX |
| T6 | 09 · Hak-yükümlülük | Madde 8.1 ↔ 14.1 | Aynı rapor yükümlülüğü bir yerde "yükümlüdür", diğerinde "tavsiye edilir" |
| T7 | 16 · Eksiklik | Madde 10.1 | Teminat oranı "%......" boş bırakılmış; Madde 6.3 bu orana atıf yapıyor |
| T8 | 17 · Şablon kalıntısı | Madde 15.2 | "Meridyen Lojistik A.Ş." taraf değil, başka sözleşmeden kalmış |
| T9 | 18 · Koşul kapsama | Madde 13.1 | "10 günden az" / "10 günden fazla" — tam 10 gün hiçbir dala girmiyor |
| T10 | 26 · Belge mimarisi | Yönetici özeti ↔ Ek-A A.1 | Özet "ek onay veya koşula bağlı olmaksızın uygulanabilir" diyor; Ek-A kapsam genişletmeyi yazılı onay ve bütçe artışı şartına bağlıyor |
| T11 | 09 + KG-2 · Ters istisna | Madde 6.4 ↔ 6.2 | "Madde 6.2 hükümleri saklı kalmak kaydıyla … 60 güne kadar erteleyebilir" — saklı tutulan 30 günlük ödeme kuralı olduğu için erteleme yetkisi kendi kendini iptal ediyor; ölü hüküm. **Mekanik istisna süzgeci bunu kaçırır** |

## Tuzak (raporlanmamalı)

| # | Konum | Neden bulgu değil |
|---|---|---|
| P1 | Madde 4.1 ↔ Madde 5.1 | Madde 4.1 "**Madde 5 hükümleri** saklı kalmak kaydıyla" diyerek fesih hakkını 12 aylık asgari süreye tabi kılıyor. Saklı tutma **doğru yönde**: genel kural özel kurala boyun eğiyor. Düzgün kurulmuş kural-istisna ilişkisidir; çelişki olarak raporlanması **isabet oranını düşürür** |

## T11 ile P1 arasındaki fark — testin can alıcı noktası

İkisi de "saklı kalmak kaydıyla" içerir. Ayıran şey **yön**:

- **P1 (bulgu değil):** Genel kural (fesih hakkı), özel kuralı (12 ay kilit) saklı tutuyor → özel kural genel kuralı sınırlıyor, kurgu sağlam.
- **T11 (bulgu):** Özel kural (60 gün erteleme), genel kuralı (30 gün ödeme) saklı tutuyor → erteleme yetkisi hiç uygulanamaz, ölü hüküm.

İfadeyi görüp bulguyu düşüren bir süzgeç P1'i doğru geçer ama T11'i kaçırır. Yönü okuyan bir süzgeç ikisini de doğru sınıflandırır. Bu çift, istisna süzgecinin mekanik mi yoksa anlamlı mı çalıştığını ölçer.

## Değerlendirme

```
Yakalama = bulunan tohum / 11
İsabet   = (gerçek bulgu) / (raporlanan toplam bulgu)
```

P1'i çelişki olarak raporlamak isabeti düşürür. Belgede tohum dışında da küçük kusurlar
bulunabilir (ör. Madde 12'nin denetim sıklığı ile Madde 9'un raporlama periyodu arasındaki
ilişkinin tanımsızlığı); bunlar uydurma sayılmaz, "gerçek bulgu" kabul edilir — uydurma,
belgede karşılığı olmayan ya da alıntısı metinde bulunmayan bulgudur.

# Denetim Raporu — BT-DST-2026/017

## R-1 · Kapak ve kapsam sınırı

**Belge:** `evals/gercek-test/sozlesme-dogrulanmamis.md` (BT-DST-2026/017, Rev. 3)
**Denetlenen sürüm:** commit `ab3d60be62e6` (belge denetimden önce donduruldu)
**Mod:** TAM · **Tarih:** 2026-09-23
**Kullanılan araçlar:** metinsel arama, aritmetik hesaplama (Python). Dış kaynak erişimi **yok** — ağ politikası engelli.

### Neyin denetlenmediği

- **Mevzuat atıfları dış kaynağa karşı teyit edilemedi** (ağ erişimi yok) → madde 12 bulguları `DIŞ DOĞRULAMA GEREKLİ` olarak bırakıldı.
- **Revizyon tablosunun doğruluğu** denetlenemedi: önceki sürümler elde yok, "Ek-2 birim fiyatları güncellendi" kaydı fiili değişiklikle karşılaştırılamadı (madde 10 kısmen kapsam dışı).
- **"Sayfa: 1/4"** beyanı doğrulanamadı.
- **Tek koşu** yapıldı → KG-6 gereği bulgular `KESİN` üstü kesinlik iddia etmez.

### Denetimin kendi sınırı (önemli)

Belgeyi denetleyen taraf, belgeyi yazan tarafla aynıdır. Belge kasıtlı tohum içermeden, hiçbir sayı/tarih/atıf doğrulanmadan yazıldı; dolayısıyla bulgular önceden bilinmiyordu. Ancak bu tasarım, harici bir belgeyle yapılacak testten zayıftır. Bulguların hepsi alıntı ve aritmetikle kontrol edilebilir durumdadır — yargıya dayanan tek bulgu B-09'dur.

---

## R-2 · Özet sayım

| Etiket | Adet |
|---|---|
| `ÇELİŞKİLİ` | 6 |
| `BELİRSİZ` | 3 |
| `DIŞ DOĞRULAMA GEREKLİ` | 1 |
| `BELGEDE BELİRTİLMİYOR` | 0 |
| **Ana bulgu** | **11** |
| Etkilenen konum | 17 |

Riske göre: Yüksek 7 · Orta 3 · Düşük 1
**Doğrulanıp temiz çıkan kontroller: 9** (aşağıda, R-5)

**En kritik üç bulgu:** varlık adedi çelişkisi (320 ↔ 280), fesih hakkı ile 18 aylık kilit çakışması, "sözleşme bedeli" teriminin tanımsızlığı — teminat ve ceza tavanı bu terime bağlı.

---

## R-3 · Bulgular

### B-01 · Ölçüm noktası adedi çelişkili — `ÇELİŞKİLİ` · Madde 02 · Yüksek · Kesin

- **Madde 2.1:** "Ek-1'de tanımlanan 320 adet ölçüm noktası"
- **Ek-1 tablosu:** "Ölçüm noktası | 280"

Aynı varlık kümesi iki yerde farklı sayıda. Madde 2.1 açıkça Ek-1'e atıf yaptığı için iki değer aynı evreni tarif ediyor; beş unsur örtüşüyor. Veri toplama ünitesi (48) her iki yerde tutuyor — yani hata tek kalemde.

**Etki:** Mali ve operasyonel. Bakım kapsamı ve Ek-2'deki "periyodik bakım" bedeli 40 noktalık belirsizlik taşıyor.
**Gerekli bilgi:** Gerçek kurulu adet.
**Öneri:** Doğru adet tespit edilip tek yerde (Ek-1) tanımlanmalı, Madde 2.1 yalnızca Ek-1'e atıf yapmalı — sayı tekrarlanmamalı.

---

### B-02 · Ek-3 atfının hedefi yok — `ÇELİŞKİLİ` · Madde 03 · Yüksek · Kesin

- **Madde 6.3:** "ölçüm kayıtlarını **Ek-3**'te belirtilen yöntemle tutar"
- Belgede yalnızca **EK-1** ve **EK-2** var (araçla doğrulandı).

**Etki:** Operasyonel. Müdahale süresi ölçüm yöntemi tanımsız kalıyor; Madde 9.1 cezası bu ölçüme dayandığı için ceza uygulaması dayanaksız.
**Öneri:** Ek-3 eklenmeli veya ölçüm yöntemi Madde 6'ya yazılmalı.

---

### B-03 · Yüklenici'nin tüzel kişilik türü çelişkili — `ÇELİŞKİLİ` · Madde 04 · Yüksek · Kesin

- **Madde 1.1:** "Teknova Sistem Çözümleri **Anonim Şirketi**"
- **Madde 13.1:** "Teknova Sistem Çözümleri **Ltd. Şti.**"

Devir yasağı, tanımlı taraftan farklı bir tüzel kişiliğe yükleniyor.

**Etki:** Hukuki. Devir yasağının hangi tüzel kişiyi bağladığı tartışmaya açık.
**Öneri:** Madde 13.1'de tanımlı kısaltma ("Yüklenici") kullanılmalı; ticari unvan tekrarlanmamalı.

---

### B-04 · "Sözleşme bedeli" tanımsız — `BELİRSİZ` · Madde 19 · Yüksek · Kesin

- **Madde 4.1:** "Sözleşmenin **yıllık** bedeli 4.860.000 TL"
- **Madde 5.1:** "**sözleşme bedelinin** %6'sı oranında kesin teminat… 291.600 TL"
- **Madde 9.3:** "toplam ceza, **yıllık bedelin** %10'unu aşamaz… 486.000 TL"

Belge yalnızca *yıllık* bedeli tanımlıyor; "sözleşme bedeli" terimi tanımsız. Üç yıllık toplam 14.580.000 TL'dir (hesaplandı). Madde 5.1'deki 291.600 TL rakamı yıllık bedele göre hesaplanmış (4.860.000 × %6 = 291.600, doğrulandı) — yani rakam yıllık esası varsayıyor ama metin bunu söylemiyor. Madde 9.3 aynı durumda "yıllık" diyerek açık, Madde 5.1 demiyor.

**Etki:** Mali. Teminat, sözleşme toplamına göre hesaplanırsa 874.800 TL olurdu — üç katı.
**Gerekli bilgi:** Teminatın matrahı yıllık mı toplam bedel mi?
**Öneri:** Madde 5.1'de "yıllık bedelin %6'sı" yazılmalı ya da Madde 1.3'e "Sözleşme Bedeli" tanımı eklenmeli.
**Not (İP-6):** Bu bulgu B-04 kökünden; Madde 5.1 ve 9.3 aynı düzeltmeyle kapanır.

---

### B-05 · Kullanılabilirlik eşiğinde cezasız aralık — `ÇELİŞKİLİ` · Madde 18 · Yüksek · Kesin

- **Madde 7.1:** "Aylık sistem kullanılabilirlik oranı **en az %99,5** olacaktır."
- **Madde 7.2:** "Kullanılabilirlik oranı **%99'un altına** düştüğünde Madde 9 hükümleri uygulanır."

%99,00 ile %99,50 arasındaki her değer Madde 7.1'i ihlal ediyor ama hiçbir yaptırıma bağlanmıyor. Yükümlülük ile yaptırım aynı eşiğe oturmuyor.

**Etki:** Operasyonel ve mali. Yüklenici %99,1'de sürekli çalışsa ihlal hâlinde olur, ceza doğmaz.
**Öneri:** İki eşik tek değere çekilmeli (ör. her ikisi de %99,5) ya da aradaki aralık için kademeli yaptırım tanımlanmalı.

---

### B-06 · Artvin'de kritik arıza müdahale süresi çelişkili — `ÇELİŞKİLİ` · Madde 09 · Yüksek · Kesin

- **Madde 6.1:** "Kritik arızalarda müdahale süresi **en fazla 4 saattir**."
- **Ek-1/1.B:** "**Artvin** ilindeki varlıklar için saha müdahalesi, ulaşım koşulları nedeniyle **8 saat** içinde yapılır."

Artvin'de bir kritik arıza için iki farklı üst sınır geçerli. Madde 6.1 mutlak ("en fazla"), 1.B ise istisna gibi yazılmış ama **hiçbir saklı tutma kaydı yok** — KG-2 gereği bağlayıcı ifade yoksa çelişki olarak raporlanır. Muhtemelen kasıtlı bir istisna, ancak kurgusu eksik.

**Etki:** Hukuki ve mali. Artvin'de 6 saatte yapılan müdahale için ceza doğup doğmadığı belirsiz (Madde 9.1).
**Öneri:** Madde 6.1'in başına "Ek-1/1.B hükümleri saklı kalmak kaydıyla" eklenmeli — saklı tutma yönü genel kuraldan özel kurala bakmalı.

---

### B-07 · Gizlilik süresi çelişkili — `ÇELİŞKİLİ` · Madde 09 · Yüksek · Kesin

- **Madde 11.1:** "bilgileri **süresiz olarak** gizli tutar"
- **Madde 11.2:** "Gizlilik yükümlülüğü, sözleşmenin sona ermesinden itibaren **5 yıl** devam eder."

Aynı yükümlülük için biri süresiz, diğeri süreli. Bağlayıcı istisna ifadesi yok.

**Etki:** Hukuki. Altıncı yılda yapılan bir ifşanın ihlal sayılıp sayılmayacağı belgeden çıkarılamıyor.
**Öneri:** Tek süre benimsenmeli; kademeli koruma isteniyorsa bilgi türüne göre ayrılmalı (ör. ticari sır süresiz, diğerleri 5 yıl).

---

### B-08 · Fesih hakkı 18 aylık kilitle çakışıyor — `ÇELİŞKİLİ` · Madde 09 · Yüksek · Kesin

- **Madde 10.1:** "İdare, 30 gün önceden yazılı bildirimde bulunmak kaydıyla sözleşmeyi tek taraflı olarak feshedebilir."
- **Madde 10.3:** "Sözleşme, **ilk 18 ay içinde** taraflarca feshedilemez."

Aynı madde içinde, biri koşulsuz hak tanıyor, diğeri 18 ay boyunca yasaklıyor. İki fıkrayı bağlayan saklı tutma kaydı yok.

**Etki:** Hukuki ve mali. 10. ayda gönderilen bir fesih bildiriminin geçerliliği belirsiz.
**Öneri:** Madde 10.1'e "Madde 10.3 hükümleri saklı kalmak kaydıyla" eklenmeli.

---

### B-09 · Yönetici özeti gövdeyle çelişiyor — `ÇELİŞKİLİ` · Madde 26 · Orta · Kesin

- **Yönetici özeti:** "Sözleşme, İdare'nin tek taraflı fesih hakkını saklı tutar ve **ilave onay gerektirmez**."
- **Madde 10.3:** ilk 18 ay fesih yasağı (fesih hakkını sınırlıyor)
- **Madde 17.1:** kapsam genişletme "Bilgi Teknolojileri Direktörlüğü'nün yazılı onayına tabidir"

Özet iki noktada gövdeden daha serbest bir tablo çiziyor: koşulsuz fesih hakkı ve onay gerekmemesi. Yalnızca özeti okuyan bir karar alıcı yanılır.

**Etki:** Operasyonel. Özet çoğu zaman tek okunan bölümdür.
**Öneri:** Özete 18 aylık kilit ve kapsam onayı şartı eklenmeli.

---

### B-10 · İki küçük belirsizlik — `BELİRSİZ` · Madde 19 · Düşük · Kesin

- **Madde 5.2:** "**kabul işlemlerinin** tamamlanmasından 30 gün sonra iade edilir" — "kabul işlemleri" belgede hiçbir yerde tanımlanmamış (araçla doğrulandı: tek geçiş, tanım yok). Teminat iadesinin başlangıç anı belirsiz.
- **Madde 6.4:** bildirimler "ertesi iş günü saat **09:00** itibarıyla alınmış sayılır" — ancak Madde 1.3'teki Çalışma Saatleri **08:30**'da başlıyor. 30 dakikalık boşluğun gerekçesi yok.

**Öneri:** "Kabul işlemleri" Madde 1.3'te tanımlanmalı; 6.4'teki saat Çalışma Saatleri başlangıcına çekilmeli.

---

### B-11 · KVKK madde atfı — `DIŞ DOĞRULAMA GEREKLİ` · Madde 12 · Katman 3 · Orta

- **Madde 12.2:** "aynı Kanun'un **8. maddesinde** öngörülen **aydınlatma** yükümlülüğü"

6698 sayılı Kanun'da aydınlatma yükümlülüğünün 10. maddede, 8. maddenin ise kişisel verilerin aktarılmasına ilişkin olduğu kanaatindeyim; ancak **bu bir dış doğruluk sorusudur ve bu denetimde dış kaynak erişimi yoktu.** KG-7 gereği iddia seviyesi düşürülmüştür: mevzuat metniyle teyit edilmeden düzeltme yapılmamalıdır.

**Öneri:** Madde numarası yürürlükteki Kanun metninden teyit edilmeli.

---

### Değerlendirilip düşürülen adaylar

| No | Aday | Ret gerekçesi |
|---|---|---|
| R-01 | Madde 3.1 süresi (01.02.2026–31.01.2029 = "36 ay") | **Hesap aracım 35 ay verdi — araç yanlış.** 01.02.2026 + 36 ay = 01.02.2029; bunun bir gün öncesi 31.01.2029. Sözleşme doğru. Naif ay farkı hesabı gün bileşenini atlıyor. |
| R-02 | Madde 9.1 eşiği ("8 saate kadar" / "8 saatten fazla") | "…e kadar" ifadesi sınır değeri içerir; tam 8 saat ilk dala düşer. Boşluk yok — B-05'teki durumla karıştırılmamalı. |
| R-03 | Madde 8.4 "eğitim düzenlemesi tavsiye edilir" | Yükümlülükler başlığı altında tavsiye kipi kullanılmış; üslup kusuru. Aynı edim için başka yerde zorunluluk kipi yok, dolayısıyla madde 09 anlamında kip çakışması oluşmuyor. İzleme notu. |
| R-04 | Madde 16.1 yetkili mahkeme (Ankara) ↔ İdare'nin adresi (Trabzon) | Yetkili mahkeme taraflarca serbestçe kararlaştırılabilir; Ankara Yüklenici'nin adresidir. Kalıntı karinesi yok. |
| R-05 | Ek-2'de "Yedek parça karşılığı" kaleminin yatırım harcaması sayılması | Muhasebe sınıflandırması belge içinde başka bir yerde çelişmiyor; doğruluğu dış standarda bağlı, iç tutarsızlık değil. |

---

## R-5 · Doğrulanıp temiz çıkan kontroller

Bunlar raporlanabilir bulgu değil; isabet oranının anlamlı olması için kaydedilmiştir.

| Kontrol | Sonuç |
|---|---|
| Ek-2 kalem toplamı (210+120+60+15) | 405.000 ✓ tabloyla uyumlu |
| Aylık taksit × 12 | 4.860.000 ✓ Madde 4.1 ile uyumlu |
| Teminat %6 hesabı (yıllık esasa göre) | 291.600 ✓ rakam doğru (matrah tanımı B-04) |
| Ceza üst sınırı %10 | 486.000 ✓ Madde 9.3 ile uyumlu |
| Veri toplama ünitesi adedi (Madde 2.1 ↔ Ek-1) | 48 = 48 ✓ |
| Sözleşme süresi 36 ay | ✓ doğru (bkz. R-01) |
| İç madde atıfları (Madde 1, 7, 9, 17) | hepsinin hedefi var ✓ |
| Tanımlı terimler (Kritik Arıza, Saha, Çalışma Saatleri, Müdahale Süresi) | tanımlı ve tutarlı kullanılmış ✓ |
| Revizyon tablosu Rev.3 "teminat oranı %6'ya çıkarıldı" | Madde 5.1'de %6 ✓ yansımış |

---

## R-4 · Kapsama listesi

**✓** kontrol edildi, bulgu yok · **B-xx** bulgu · **–** uygulanabilir değil · **✗** kontrol edilemedi

| Madde | Özet | M1–5 | M6–9 | M10–13 | M14–17 | İmza | Ek-1 | Ek-2 | Rev. |
|---|---|---|---|---|---|---|---|---|---|
| 01 Tarihsel | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | – | – | ✓ |
| 02 Sayısal | ✓ | B-01 | ✓ | ✓ | – | – | B-01 | ✓ | – |
| 03 Referans | ✓ | ✓ | B-02 | ✓ | ✓ | – | ✓ | ✓ | ✓ |
| 04 Varlık | ✓ | ✓ | – | B-03 | – | ✓ | – | – | – |
| 05 Mantıksal | B-09 | ✓ | ✓ | B-07 | ✓ | – | ✓ | ✓ | – |
| 06 Sınıflandırma | – | – | – | – | – | – | ✓ | R-05 | – |
| 07 Format | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 08 Görsel-metin | – | – | – | – | – | – | – | – | – |
| 09 Hak-yükümlülük | ✓ | ✓ | B-06 | B-07, B-08 | ✓ | – | B-06 | – | – |
| 10 Versiyon | ✓ | ✓ | – | – | – | – | – | ✗ | ✗ |
| 11 Dilbilimsel | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 12 Mevzuat | – | – | – | B-11 | – | – | – | – | – |
| 13 Meta-veri | ✓ | ✓ | – | – | – | – | – | – | ✓ |
| 14 İmza/yetki | – | ✓ | – | – | – | ✓ | – | – | – |
| 15 İstatistiksel | – | – | – | – | – | – | – | – | – |
| 16 Eksiklik | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17 Şablon kalıntısı | ✓ | ✓ | ✓ | R-04 | ✓ | ✓ | ✓ | ✓ | ✓ |
| 18 Koşul/eşik | – | ✓ | B-05, R-02 | ✓ | – | – | ✓ | – | – |
| 19 Belirsiz terim | ✓ | B-04, B-10 | B-10 | ✓ | ✓ | – | ✓ | ✓ | – |
| 20 Çok dillilik | – | – | – | – | – | – | – | – | – |
| 21 Para/vergi/kur | ✓ | ✓ | ✓ | – | – | – | – | ✓ | – |
| 22 Kapsam evreni | ✓ | ✓ | ✓ | ✓ | ✓ | – | ✓ | – | – |
| 23 İddia-kanıt | – | – | – | – | – | – | – | – | – |
| 24 İzlenebilirlik | – | – | – | – | – | – | – | – | – |
| 25 Durum geçişi | – | – | ✓ | ✓ | ✓ | – | – | – | – |
| 26 Belge mimarisi | B-09 | – | – | – | – | – | – | – | – |

Uygulanabilir değil (–) işaretli maddeler: belgede görsel yok (08), istatistik yok (15), tek dilli (20), amaç-ölçüt zinciri içermiyor (24), iddia-kanıt yapısı yok (23).

---

## İstatistikler

| Birim | Sayı |
|---|---|
| İncelenen iddia birimi | 52 (numaralı fıkra + özet cümlesi + tablo satırı) |
| İncelenen mutlak tarih | 5 |
| İncelenen süre/periyot ifadesi | 19 |
| İncelenen sayısal/parasal ifade | 24 |
| İncelenen terim | 9 (1'i tanımsız) |
| İç atıf | 7 (hepsinin hedefi var) |
| Ek atfı | 3 (1'i hedefsiz) |
| Dış mevzuat atfı | 2 (ikisi de teyit edilemedi) |
| Doğrulanan birebir alıntı | 21 / 21 |
| **Ana bulgu** | **11** |
| Etkilenen konum | 17 |
| Gerekçeli ret | 5 |
| Temiz çıkan kontrol | 9 |
| İnsan onayı gereken yüksek riskli bulgu | 6 |
| Dış doğrulama bekleyen | 1 |

Tek yüzdelik skor verilmemektedir. Doğru ifade: *incelenen 52 iddia biriminde 6 yüksek, 3 orta ve 1 düşük öncelikli sorun ile 1 dış doğrulama gerektiren iddia tespit edilmiştir; 5 aday bulgu gerekçeyle düşürülmüştür; mevzuat atıfları ve revizyon geçmişi denetlenememiştir.*

---

## Denetimin kendi denetimi

Rapordaki her birebir alıntı, kaynak metinde metinsel aramayla doğrulandı (KG-1). Bu kontrol **kendi raporumda bir kusur buldu:** R-03 satırında revizyon kaydı "teminat %6'ya çıkarıldı" olarak yazılmıştı; kaynakta "teminat **oranı** %6'ya çıkarıldı" geçiyor. Bir kelime düşürülmüştü. Düzeltildi.

Doğrulama betiğinin sınırı: raporda tırnak içinde geçen her metin kaynak alıntısı değil — önerilen düzeltme metinleri ve tanımlanması istenen terimler de tırnaklı. Betik bunları ayırt etmiyor, ayrıca büyük/küçük harfe duyarlı. Bu nedenle "bulunamadı" çıkan 13 dizgeden 12'si yanlış alarmdı; yalnızca biri gerçek kusurdu. Betiğin kaynak alıntısını öneri metninden ayırt etmesi gerekiyor — açık iş.

**İkinci kendini-denetleme bulgusu:** R-2 özet sayımı ile gövde ve istatistikler birbirini tutmuyordu — özet "10 ana bulgu / 6 temiz kontrol" derken gövdede 11 bulgu (B-01…B-11) ve R-5'te 9 temiz kontrol vardı. Aynı sayının iki yerde farklı olması, bu sistemin Madde 02'sinin tam olarak aradığı kusurdur; denetim raporunun kendisi bu kusuru taşıyordu. Düzeltildi ve sayımlar betikle doğrulandı (11 = 11 = 11).

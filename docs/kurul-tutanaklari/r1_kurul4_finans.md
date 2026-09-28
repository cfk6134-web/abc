# Kurul 4: Hane Finansı, TCO ve Sürdürülebilirlik — 1. Tur Değerlendirmesi

## 1. Güçlü yönler
- **Önce işlev geliyor.** "İhtiyaca uygunluk" 30 puan alıyor. Finansal açıdan en pahalı hata, gereksiz ya da yanlış ürünü almaktır. Bu ağırlık o hatayı önlüyor.
- **Hollanda'ya özgü risk ayrıca puanlanıyor.** "NL'de garanti/servis/iade" (10) ile "satıcı güvenliği" (7) birlikte, AB dışından alımın gizli maliyetlerini dolaylı olarak cezalandırıyor. Bu maliyetler iade kargosu, ulaşılamayan servis ve dolandırıcılık riskidir.
- **Sahiplik süresi düşünülmüş.** "Uzun dönem sahiplik değeri" ve "ömür" kalemleri var, yani sistem yalnızca kasadaki fiyata bakmıyor.

## 2. Zayıf yönler ve kör noktalar
1. **Fiyat sistemde görünmüyor.** Satın alma fiyatı hiçbir satırda açıkça yer almıyor. €400'lık ve €1.200'lük iki ürün aynı puanı alabilir. Sistem "en iyi ürünü" buluyor, "hanem için en doğru harcamayı" bulmuyor.
2. **8 puan maliyeti taşımaya yetmiyor.** Hollanda'da elektrik 2026'da ortalama €0,26–0,29/kWh (CBS/ANWB) seviyesinde. Yılda 150 kWh fazla tüketen bir buzdolabı, 12 yılda yaklaşık **€500** ek maliyet çıkarıyor. Bu fark çoğu zaman iki modelin fiyat farkından büyük. Yazıcı mürekkebi, robot süpürge filtresi ve zorunlu uygulama abonelikleri de aynı şekilde fiyatı ikiye katlayabilir. Bunların hepsi şu an 8 puanlık tek bir satıra sıkışmış.
3. **Maliyet aynı anda birden fazla satırda puanlanıyor.** Dayanıklılık (20), ömür (5) ve sahiplik değeri (8) aynı ekonomik gerçeği ölçüyor: ürün kaç yıl dayanır ve yılda kaça mal olur? Bunları ayrı ayrı puanlamak hem çifte sayım yaratır hem de tutarsızlığa yol açar.
4. **AB dışından alımın maliyeti modellenmemiş.** 1 Temmuz 2026'dan itibaren €150 altı gönderilerde gümrük muafiyeti kalktı. Yerine kalem başına **€3** sabit gümrük vergisi geldi. 1 Kasım 2026'dan itibaren buna **€2** AB işlem ücreti (afhandelingsvergoeding) ekleniyor. İthalat BTW'si (%21) 2021'den beri €0'dan itibaren alınıyor. Taşıyıcının gümrükleme ücreti de cabası. Ucuz görünen Temu/AliExpress fiyatı, teslimde %10–30 pahalanabilir.
5. **İkinci el ve refurbished seçenekleri yok.** Marktplaats'ta değerini koruyan markalar TCO'yu ciddi biçimde düşürüyor (Apple, Miele, kaliteli bisikletler gibi). Swappie, Back Market ve Leapp gibi refurbished seçenekler de genellikle en iyi €/yıl oranını veriyor. Sistem bunları aday listesine bile almıyor.
6. **Sürdürülebilirlik ölçülemeyen bir kalem olarak kalmış.** 5 puan "iyi niyet" puanına dönüşme riski taşıyor. Oysa sürdürülebilirliğin ölçülebilir kısmı zaten parayla ifade edilebiliyor: ömür, enerji, yedek parça ve yazılım destek yılı.
7. **Tahmin belirsizliği göz ardı ediliyor.** Enerji fiyatı, ömür ve ikinci el değeri tahmindir. Duyarlılık aralığı olmadan tek bir sayı yanıltıcı bir kesinlik izlenimi veriyor.

## 3. Somut öneriler

### 3.1 TCO formülü (BTW dahil, €)
```
TCO = P + T + N × (E + S + A + B) + R_risk − V_N

P  = satın alma fiyatı (BTW dahil; indirim/cashback düşülmüş)
T  = teslim + kurulum + (AB dışıysa: €3/kalem gümrük + €2 işlem ücreti
     + taşıyıcı gümrükleme ücreti + ithalat BTW'si, eğer fiyata dahil değilse)
E  = yıllık enerji = kWh/yıl (EPREL etiketi) × €0,28  (duyarlılık: €0,22–0,35)
S  = yıllık sarf malzemesi (mürekkep, filtre, fırça, pil…)
A  = zorunlu abonelik/uygulama ücreti
B  = beklenen bakım/onarım (garanti bitince arıza olasılığı × onarım bedeli)
R_risk = iade/servis zorluğu için risk payı (AB dışı veya servisi olmayan marka)
V_N = N yıl sonra ikinci el değeri (Marktplaats'ta benzer ilanların medyanı × 0,8)
N  = gerçekçi kullanım ömrü; üreticinin yedek parça/yazılım desteği yılıyla sınırlanır
```
**Temel metrik: Yıllık maliyet = TCO / N (€/yıl).** Ömrün uzaması bu sayıyı otomatik olarak düşürür. Böylece sürdürülebilirlik kullanıcıya doğrudan ölçülebilir bir fayda olarak yansır.

Hurda ve bertaraf: NL perakendecisinden alınan elektrikli ürünlerde verwijderingsbijdrage (geri dönüşüm katkı payı) fiyata dahildir. Oud-voor-nieuw kuralıyla eski cihaz ücretsiz geri alınır, yani bertaraf maliyeti ≈ €0 olur. AB dışı satıcıda bu güvence yok, bu yüzden R_risk'e eklenmeli. Statiegeld (depozito) çoğu dayanıklı üründe ihmal edilebilir düzeydedir.

### 3.2 Fiyat bandı stratejisi (üç adım)
1. **Eleme kapıları:** Adayın aşağıdakileri geçmesi gerekir:
   - ihtiyaca uygunluk puanının en az %60'ı,
   - güvenli satıcı,
   - CE işareti ve AB içinde ulaşılabilir garanti.

   Bu kapılar, en ucuz ama işe yaramayan ürünün "değer oranıyla" kazanmasını engeller.
2. **Bütçe bandı:** Harcamadan önce bir tavan belirlenir. Karşılaştırma bu bandın ±%25'i içindeki aday seti ile yapılır. Aday setine en az bir refurbished veya ikinci el seçenek konur.
3. **Puanlama ve çapraz kontrol:**
   - TCO puanı, 100'lük skorun içinde göreli olarak hesaplanır: `TCO puanı = 18 × (en düşük €/yıl ÷ adayın €/yıl)`.
   - Ayrıca bilgi amaçlı bir **değer oranı** raporlanır: fiyat dışı puan ÷ (€/yıl). Bu oran toplama eklenmez, yalnızca üst sıradaki adaylar birbirine yakınsa karar ölçütü olur. Eklenmemesinin nedeni çifte sayımı önlemektir.
   - Azalan getiriyi görünür kılmak için bir kural: bir üst modelin ek maliyeti, fiyat dışı puanda en az aynı oranda artış sağlamıyorsa ucuz model seçilir.

### 3.3 Rubrik: "Onarılabilirlik ve destek" (8 puan)
- Resmi yedek parça ve yazılım desteği ≥ 7 yıl: 3 puan. 5 yıl: 2 puan. Bilinmiyor: 0 puan.
- AB onarılabilirlik endeksi (telefon/tablet A–E, Haziran 2025'ten beri) veya iFixit skoru: 0–3 puan.
- Pil ve sarf malzemesi kullanıcı tarafından değiştirilebilir, üçüncü taraf muadilleri serbest: 0–2 puan.

Ölçülemeyen "yeşil" iddialara puan verilmez.

## 4. Kurul 4'ün önerdiği ağırlık tablosu

| Ölçüt | Puan |
|---|---|
| Kullanım amacına ve ihtiyaca uygunluk (eleme kapısı ≥ %60) | 25 |
| **Yıllık sahip olma maliyeti — TCO/N (fiyat, enerji, sarf, abonelik, NL/AB dışı ek maliyetler, ikinci el değeri)** | **18** |
| Gerçek kullanımda ölçülen performans | 17 |
| Kalite, dayanıklılık ve güvenilirlik (arıza oranı, kullanıcı raporları) | 15 |
| NL'de garanti, servis ve iade kolaylığı | 10 |
| Onarılabilirlik ve parça/yazılım destek süresi (ömür TCO'nun içinde) | 8 |
| Satıcı ve işlem güvenliği (ayrıca eleme kapısı) | 7 |
| **Toplam** | **100** |

Tablodaki değişikliklerin gerekçesi:
- Eski "teslim + sahiplik değeri" (8) ve "ömür/sürdürülebilirlik" (5) satırlarının ölçülebilir kısımları TCO satırında birleşti. Bu satır, fiyatı da içerecek şekilde 18 puana çıktı.
- Onarılabilirlik kendi başına 8 puana yükseldi, çünkü doğrudan N'yi (ömrü) ve B'yi (bakım/onarım maliyetini) güvence altına alıyor.
- Uygunluk ve performanstan alınan 8 puan maliyete aktarıldı. Mantığı şu: aynı işi gören iki ürün arasında yılda €100 fark, hane için gerçek bir farktır.

**Duyarlılık notu:** Karar, enerji fiyatının €0,22 veya €0,35 olması ya da ömrün ±%30 değişmesi durumunda sıralama değişmiyorsa sağlamdır. Sıralama değişiyorsa ucuz ve onarılabilir aday tercih edilir.

---
Kaynaklar:
- [Consilium – küçük paketlere gümrük vergisi (1 Temmuz 2026)](https://www.consilium.europa.eu/en/press/press-releases/2025/12/12/customs-council-agrees-to-levy-customs-duty-on-small-parcels-as-of-1-july-2026/)
- [Avalara – €150 muafiyetinin sonu](https://www.avalara.com/blog/en/europe/2025/11/eu-end-150-customs-duty-exemption-2026.html)
- [Douane – €2 afhandelingsvergoeding (1 Kasım 2026)](https://www.douane.nl/afhandelingsvergoeding-e-commerce/)
- [Rijksoverheid – €2 Avrupa ek ücreti](https://www.rijksoverheid.nl/actueel/nieuws/2026/09/22/europese-toeslag-van-euro-2-voor-pakketjes-van-buiten-de-eu)
- [ANWB – Wat kost 1 kWh?](https://www.anwb.nl/energie/wat-kost-1-kwh)
- [Pure Energie – stroomprijs september 2026](https://pure-energie.nl/energieprijzen/stroomprijs-per-kwh/)

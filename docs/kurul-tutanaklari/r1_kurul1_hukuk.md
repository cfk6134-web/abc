# Kurul 1 — Hollanda Tüketici Hukuku ve Satıcı Güvenliği: Değerlendirme

*Tarih: 28 Eylül 2026. Hukuki bilgi genel niteliktedir; bireysel hukuki danışmanlık değildir.*

## 1. Güçlü yönler

- **Ürün odaklı çekirdek doğru.** Uygunluk (30) + performans (20) + kalite (20) = 70 puanla sistem, "ucuz ama işe yaramaz" alımları önlüyor. Hukuken de mantıklı: BW 7:17'deki *conformiteit* ölçütü de "tüketicinin makul beklentisi"ne dayanır. Ürün baştan yanlış seçilmişse, hukuki koruma bunu düzeltmez.
- **Hollanda'ya özgü satış sonrası ayrı bir ölçüt.** Garanti/servis/iade ayrı ölçütte duruyor. Çoğu genel sistem bunu hiç ele almıyor.
- **Satıcı güvenliği hesaba katılmış.** Sahte webwinkel dolandırıcılığı Hollanda'da en yaygın tüketici sorunlarından biri. Ölçütün olması bile doğru bir refleks.

## 2. Zayıf yönler ve kör noktalar

**a) Satıcı güvenliği puan olmamalı, eşik (knock-out) olmalı.** 7 puanlık ağırlık hatalı bir telafi mantığı kuruyor. Sahte bir mağaza 0/7 alsa bile, ürün puanları sayesinde toplamda 93 alabilir. Oysa bu senaryoda ürün hiç gelmez: beklenen değer sıfırdır. Dolandırıcılık riski *çarpan* gibi davranır, toplanan bir kalem gibi değil. Bu yüzden kimliği doğrulanamayan satıcı ya da geri alınamayan ödeme **veto** olmalı.

**b) "Garanti" kavramı karışık.** Ölçüt büyük olasılıkla üretici garantisini (fabrieksgarantie) ölçüyor. Hollanda'da asıl koruma ise **yasal uygunluk (conformiteit)** hakkıdır:
- Satıcıya karşı ileri sürülür, üreticiye karşı değil.
- Sabit 2 yıl değildir; ürünün **makul beklenen ömrü** boyunca sürer (ör. bir çamaşır makinesinde 5 yıl ve üzeri).
- Teslimden sonraki **ilk 1 yıl ispat yükü satıcıdadır** (1 Ocak 2022'den beri).
- Ayıp fark edildikten sonra makul sürede (yaklaşık 2 ay) bildirilmelidir.

Buradan kilit sonuç çıkıyor: satıcı AB'de değilse, yasal hak kâğıt üzerinde kalır. Uzun bir üretici garantisinin değeri ise, satıcısı güvenilir ve hakkı uygulanabilir bir alıma göre ikincildir.

**c) Hukuki korumanın uygulanabilirliği ölçülmüyor.** Asıl soru "hakkım var mı?" değil, "hakkımı zorla alabilir miyim?" sorusudur. Bunun ölçülebilir göstergeleri şunlar:
- Satıcı De Geschillencommissie'ye bağlı mı?
- Thuiswinkel Waarborg var mı? (Bu, uyuşmazlık kurulu kararının yerine getirileceği güvencesini de içerir.)
- Satıcının KvK ve BTW numarası, AB'de bir iade adresi var mı?

**d) Pazaryeri (marketplace) ve AB dışı satıcı riski görünmüyor.** Bol.com, Amazon.nl ya da Temu'da sözleşmenin karşı tarafı çoğu zaman **üçüncü taraf satıcıdır**, platform değil. AB dışı satıcıda şu sorunlar ortaya çıkar:
- Cayma hakkında iade kargosu Çin'e gidebilir.
- 1 Temmuz 2026'dan beri 150 €'nun altındaki paketlere kalem başına 3 € gümrük vergisi uygulanıyor.
- CE ve GPSR uygunluğu şüphelidir.

**e) Cayma hakkının (herroepingsrecht) pratik maliyeti yok sayılıyor.** 14 günlük hak B2C mesafeli satışta geçerli. Ancak şu noktalar gerçek değeri değiştiriyor:
- Satıcı önceden bildirmişse iade kargo ücretini alıcı öder.
- İstisnalar vardır: kişiye özel ürün, hijyen mühürü açılmış ürün, dijital içerik.
- Marktplaats'ta özel kişiden alımda **hiç cayma ya da conformiteit hakkı yoktur**.

Bu kalemler "iade kolaylığı"nın gerçek içeriğidir.

**f) Ödeme yöntemi ayrı bir risk kalemi.** Tek başına iDEAL (ve iDEAL | Wero) bir banka transferidir; **chargeback yoktur**. Kredi kartı chargeback'i, PayPal alıcı koruması ve "achteraf betalen" ise geri alma yolu sunar. Aynı satıcıda bile ödeme yöntemi riski değiştirir.

**g) Mükerrer sayım.** "Kalite, dayanıklılık" (20) ile "kullanım ömrü" (5) örtüşüyor. Onarılabilirlik ise 5 puanla çok düşük. AB Onarım Hakkı Direktifi (2024/1799) iki şey getiriyor:
- Yasal garanti süresinde tüketici değişim yerine onarımı seçerse, garanti **12 ay uzar**.
- Belirli ürün grupları için garanti sonrası onarım yükümlülüğü doğar.

Hollanda direktifi 31 Temmuz 2026'ya kadar iç hukuka aktaramadı; tasarı 9 Temmuz 2026'da Meclis'e sunuldu. Yine de yön net: parça ve yazılım desteği artık hukuki değer taşıyor.

## 3. Somut öneriler

**Aşama A — Veto kapıları (herhangi biri "HAYIR" ise ürün elenir ya da başka satıcı aranır):**
- **K1 Kimlik:** Satıcının KvK/BTW numarası ya da doğrulanabilir bir AB şirket adresi var mı? Fraudehelpdesk / Watchlist Internet / Opgelicht kayıtlarında temiz mi? Alan adı 6 aydan eski mi (ya da bilinen bir zincire mi ait)?
- **K2 Ödeme:** Geri alınabilir bir ödeme yolu var mı (kredi kartı, PayPal, sonradan ödeme)? Bilinmeyen bir mağazada tek seçenek iDEAL, havale ya da kripto ise → veto.
- **K3 Ürün güvenliği:** Elektrikli ürünler, çocuk ürünleri ve şarj cihazları CE işaretli mi? AB'de sorumlu bir ekonomik aktör var mı (GPSR)?

**Aşama B — Puanlama. Önerilen "Hukuki koruma ve satış sonrası" ölçütünün 0–10 rubriği:**

| Puan | Ölçüt |
|---|---|
| 0–2 | AB dışı satıcı; iade adresi AB dışında; uyuşmazlık kanalı yok |
| 3–4 | AB'de satıcı, ancak pazaryerinde küçük üçüncü taraf; iade ücretli; NL servisi yok |
| 5–6 | NL/AB satıcı; 14 gün cayma hakkı açıkça belirtilmiş; conformiteit'i reddetmiyor |
| 7–8 | Buna ek olarak Geschillencommissie'ye bağlı ya da Thuiswinkel Waarborg'lu; ücretsiz iade; NL'de servis noktası |
| 9–10 | Buna ek olarak 30 gün ve üzeri iade; ek üretici garantisi; yerinde onarım ya da değişim geçmişi iyi (Consumentenbond / Trustpilot'ta doğrulanmış) |

Uyarı işareti: "Sadece üretici garantisi geçerlidir" diyen satıcı yasaya aykırı davranıyor → en fazla 3 puan.

**"Satıcı ve ödeme güvenliği" 0–10 rubriği (veto kapılarını geçtikten sonra):**

| Puan | Ölçüt |
|---|---|
| 3 | Kapıları zar zor geçiyor |
| 6 | Tanınmış satıcı ya da 2 yıldan uzun geçmiş |
| 8 | Keurmerk (Thuiswinkel / Webshop Keurmerk) ve kartla ödeme |
| 10 | Fiziksel mağazası olan büyük NL zinciri ya da doğrudan üretici |

**"Onarılabilirlik ve ömür" 0–10 rubriği:**
- Yedek parça ve yazılım güncellemesi taahhüdünün yıl sayısı: ≥7 yıl = 4 puan
- iFixit ya da AB onarılabilirlik skoru: yüksek = 3 puan
- Hollanda'da bağımsız onarım veya Repair Café ile uyumluluk: 3 puan

**Toplam sahiplik maliyetine** şunlar eklenmeli: iade kargo riski, gümrük (3 €/kalem) ve BTW, uzatılmış garanti gibi gereksiz ek satışlar. Conformiteit zaten koruduğu için uzatılmış garanti çoğu zaman gereksizdir.

## 4. Kurul 1'in önerdiği ağırlık tablosu

**Ön koşul:** K1–K3 veto kapıları (puansız, geç/kal).

| Ölçüt | Mevcut | Öneri |
|---|---|---|
| Kullanım amacına ve ihtiyaca uygunluk | 30 | 25 |
| Gerçek kullanım koşullarında ölçülen performans | 20 | 17 |
| Kalite, dayanıklılık, güvenilirlik | 20 | 16 |
| Hukuki koruma ve satış sonrası (conformiteit'in uygulanabilirliği, cayma, NL servisi) | 10 | 14 |
| Toplam sahiplik maliyeti (gümrük ve iade dahil) | 8 | 10 |
| Onarılabilirlik, parça ve yazılım desteği, ömür | 5 | 10 |
| Satıcı ve ödeme güvenliği (kapı sonrası nitelik) | 7 | 8 |
| **Toplam** | **100** | **100** |

**Karar kuralı:**
- Veto kapılarından geçmek zorunlu.
- Toplam puan ≥ 70 olmalı.
- "Hukuki koruma" ≤ 3 ise, fiyat avantajı en az %20 değilse aynı ürünü başka bir satıcıdan alın.

Sistem ürün seçiminde iyi, ama satıcı seçiminde kör. Aynı ürün iki farklı satıcıda iki farklı risk profili taşır. Bu yüzden değerlendirme "ürün × satıcı × ödeme" üçlüsüne yapılmalı.

---
Kaynaklar: [Consumentenbond — recht op reparatie komt later](https://www.consumentenbond.nl/acties-claims/nieuws/2026/recht-op-reparatie-komt-later); [Ondernemersplein — recht op reparatie](https://ondernemersplein.overheid.nl/wetswijzigingen/recht-op-reparatie-product-repareren-aantrekkelijker-voor-consumenten/); [Consilium — €3 duty small parcels from 1 July 2026](https://www.consilium.europa.eu/en/press/press-releases/2025/12/12/customs-council-agrees-to-levy-customs-duty-on-small-parcels-as-of-1-july-2026/)

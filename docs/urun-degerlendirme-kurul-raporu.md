# Ürün Satın Alma Değerlendirme Sistemi — Kurul Raporu

*Tarih: 28 Eylül 2026 · Kapsam: Hollanda'da yaşayan bir tüketici için önerilen 100 puanlık sistemin incelenmesi*

---

## 1. Başkanlık Divanı'nın kısa hükmü

**Sisteminiz iyi bir başlangıç. Yaklaşık %70'i doğru, ama olduğu gibi kullanılırsa üç yerde yanıltır.**

Doğru yaptıklarınız:

- Amaca uygunluğu en yükseğe koymuşsunuz (30).
- Kaliteyi ve gerçek kullanım performansını ayrı tutmuşsunuz.
- Hollanda'ya özgü garanti ve iade konusunu açıkça sisteme almışsınız.

Beş kurulun oybirliğiyle tespit ettiği üç yapısal sorun:

1. **Fiyat sistemde görünmüyor.** "Teslim maliyeti ve sahiplik değeri" (8 puan) fiyatı belirsiz bırakıyor. Sonuçta model sessizce pahalı ürüne kayıyor.
2. **Bazı kriterler puan değil, geç/kal kapısı olmalı.** Satıcı güvenliği 7 puan. Sahte bir mağaza bu kalemden 0 alsa bile toplamda 93 puana ulaşabilir, ama ürün hiç gelmeyeceği için gerçek değeri sıfırdır. Güvenlik (CE/geri çağırma), satıcı güvenilirliği ve asgari ihtiyaç "puan toplanarak telafi edilemeyecek" koşullardır.
3. **Onarılabilirlik ve ömür 5 puanla fiilen etkisiz.** 5 puanlık bir ağırlık, 0–10 ölçeğindeki normal puanlama hatasından küçük kalıyor. Bu kalem sonucu neredeyse hiç değiştiremiyor.

Kurullar sonunda **3 aşamalı bir sistemde** uzlaştı: önce veto kapıları, sonra fiyat hariç kalite puanı, en son fiyat/değer aşaması. Ağırlıklar da yeniden dağıtıldı (Bölüm 4).

---

## 2. Süreç

| Kurul | Uzmanlık | 1. tur | 2. tur |
|---|---|---|---|
| K1 | Hollanda tüketici hukuku ve satıcı güvenliği | Görüş raporu | Çapraz itiraz ve oy |
| K2 | Karar bilimi ve metodoloji (çok kriterli karar analizi, AHP) | Görüş raporu | Çapraz itiraz ve oy |
| K3 | Ürün mühendisliği, kalite ve bağımsız test | Görüş raporu | Çapraz itiraz, mevzuat doğrulaması ve oy |
| K4 | Hane finansı, toplam sahip olma maliyeti (TCO) ve sürdürülebilirlik | Görüş raporu | Çapraz itiraz ve oy |
| K5 | Kullanıcı deneyimi (şeytanın avukatı) | Görüş raporu | Çapraz itiraz ve oy |

- **1. tur:** Her kurul sistemi bağımsız olarak inceledi.
- **2. tur:** Her kurul diğer dört kurulun raporunu okudu, onlara itirazlarını yazdı, ikna olduğu noktalarda pozisyonunu değiştirdi ve revize ağırlık oyu verdi.
- **Sentez:** Başkanlık Divanı oyları birleştirdi.

Bütün tutanaklar `docs/kurul-tutanaklari/` klasöründe.

---

## 3. Oybirliğiyle kabul edilenler

| # | Karar |
|---|---|
| U1 | Satıcı kimliği ve güvenliği, ürün güvenliği (CE, GPSR, geri çağırma) ve asgari ihtiyaç **puan değil, veto kapısıdır**. |
| U2 | Onarılabilirlik, yedek parça ve yazılım desteği 5 puandan **en az 10'a** çıkmalı. |
| U3 | Süreç **tutara göre katmanlı** olmalı (50 € altı, 50–300 €, 300 € üstü). |
| U4 | Kanıtın kalitesi puana yansımalı. **5 puandan küçük farklar beraberlik** sayılır. |
| U5 | **Fiyat 100 puanın içinde değil, ayrı bir aşamada** değerlendirilir. 1. turda 4 kurul fiyatı toplamın içine koymuştu; 2. turda beşi de ayrı aşamada birleşti. |
| U6 | Ekosistem uyumu (mevcut cihazlarla uyum) ayrı bir kriter değildir, **"amaca uygunluk"un alt göstergesidir**. |
| U7 | **"Tek kanıt, tek kriter" kuralı:** aynı kanıt iki kalemde puanlanmaz. |

---

## 4. Oylama sonuçları ve nihai ağırlıklar (fiyat hariç kalite puanı)

| Ölçüt | Sizin | K1 | K2 | K3 | K4 | K5 | Ortalama | **Nihai** |
|---|---|---|---|---|---|---|---|---|
| Amaca/ihtiyaca uygunluk (ekosistem dahil) | 30 | 30 | 28 | 27 | 30 | 30 | 29,0 | **29** |
| Ölçülen performans (bağımsız test) | 20 | 19 | 22 | 22 | 20 | 20 | 20,6 | **21** |
| Kalite, dayanıklılık, güvenilirlik (zaman içinde) | 20 | 18 | 20 | 18 | 18 | 20 | 18,8 | **19** |
| Onarılabilirlik, parça, yazılım desteği, ömür | 5 | 12 | 12 | 14 | 14 | 10 | 12,4 | **13** |
| NL hukuki koruma: garanti, servis, iade | 10 | 15 | 13 | 13 | 13 | 12 | 13,2 | **13** |
| Satıcı niteliği (veto kapısından sonra) | 7 | 6 | 5 | 6 | 5 | 0 | 4,4 | **5** |
| Teslim maliyeti ve sahiplik değeri | 8 | — | — | — | — | — | — | **Aşama 3'e taşındı** |
| Kişisel tercih/estetik | — | 0 | 0 | 0 | 0 | 8 | 1,6 | **0 (beraberlikte karar verdirir)** |
| **Toplam** | 100 | 100 | 100 | 100 | 100 | 100 | 100 | **100** |

> **Kategoriye göre ayar:** Ağırlıklar en fazla ±5 puan kaydırılabilir. Ayar, **ürünlere bakmadan önce** yapılıp yazılır. Örnekler:
> - Telefon ve akıllı cihazda onarım/yazılım +2, performans −2.
> - Çamaşır makinesinde kalite/dayanıklılık +3, performans −3.
> - Kablo ya da aksesuarda tam tablo gerekmez.

---

## 5. Nihai sistem: 3 aşama

### Aşama 1 — Veto kapıları (geç/kal, her tutarda uygulanır)

| Kapı | Geçme koşulu |
|---|---|
| **K-İhtiyaç** | Olmazsa olmaz özellikler (en fazla 3–5 madde) ürünlere bakmadan önce yazılır. Bunlardan birini karşılamayan ürün elenir. |
| **K-Güvenlik** | CE işareti var, AB'de sorumlu bir ekonomik aktör var (GPSR) ve Safety Gate/NVWA'da geri çağırma kaydı yok. |
| **K-Kimlik** | Satıcının KvK/BTW numarası ya da AB'de bir şirket adresi var. Fraudehelpdesk kayıtlarında temiz. |
| **K-Ödeme** | Geri alınabilir bir ödeme yolu var: kredi kartı, PayPal ya da sonradan ödeme. ⚠️ **iDEAL anlık banka transferidir, chargeback yoktur.** Bilinmeyen bir mağazada tek seçenek iDEAL ise satıcı elenir. |
| **K-Bütçe** | Toplam sahip olma maliyeti, önceden yazılmış bütçe tavanının altında. Kontrol yalnızca etiket fiyatıyla yapılmaz. |

### Aşama 2 — Kalite puanı Q (0–100, fiyat hariç)

Her kriter 0–10 arasında puanlanır, ağırlığıyla çarpılır ve sonuçlar toplanır.

**Kriterler nasıl ayrışır (çift sayımı önlemek için):**

| Kriter | Cevapladığı soru | Kanıt türü |
|---|---|---|
| Uygunluk | "Benim senaryoma uyuyor mu?" | Teknik özellikler. **İncelemeleri okumadan önce** puanlanır. |
| Performans | "İlk gün ölçülen sonuç ne?" | Bağımsız laboratuvar testi |
| Kalite | "Zamanla bozuluyor mu?" | Arıza oranı, sahip anketleri, uzun dönem yorumlar |
| Onarım | "Bozulunca ne olur?" | Parça ve yazılım desteğinin süresi, onarılabilirlik puanı, parça fiyatı |
| NL koruma | "Bozulunca bedelini kim öder?" | Satıcının NL/AB konumu, uyuşmazlık kanalı, iade koşulları |
| Satıcı | "Bu satıcı iyi hizmet veriyor mu?" | Güven damgası (keurmerk), geçmiş, fiziksel mağaza |

**Kanıt güveni.** Veri zayıfsa puan, varsayılan bir değere doğru çekilir:

```
s' = c · s + (1 − c) · p
```

- `s`: ham puan (0–10)
- `c`: kanıt güveni. Değerleri:
  - 1,0 — bağımsız laboratuvar testi, EPREL enerji veritabanı
  - 0,8 — sahip anketi, arıza verisi, iFixit
  - 0,6 — uzman incelemesi
  - 0,4 — en az 6 aylık doğrulanmış kullanıcı yorumu
  - 0,2 — yıldız ortalaması, üretici beyanı
- `p`: veri yokken varsayılan puan. Önceki neslin puanının %20–30 indirimli hali alınır; önceki nesil verisi de yoksa **p = 4**.
- Consumentenbond, Stiftung Warentest ve Which? çoğu zaman aynı ICRT test verisini kullanır. Bu yüzden **tek kaynak sayılır**.

K3, K4 ve K2'nin düzeltilmiş hali bu formülde birleşti. Nötr 5 yerine 4 kullanılmasının sebebi, kanıtı olmayan ürünün kanıtlanmış orta bir ürünü yenmemesi.

### Aşama 3 — Fiyat ve değer (yıllık maliyet, €/yıl)

```
Yıllık maliyet = [ Fiyat + Teslim + N × (Enerji + Sarf + Abonelik) + Gümrük/iade riski − İkinci el değeri ] / N
```

- `N`: beklenen kullanım yılı. Enerji hesabında Hollanda'da 2026 için yaklaşık 0,26–0,29 €/kWh kullanılır.
- **Karar kuralı:**
  1. Q < 60 olan ürünler elenir.
  2. **Hem daha pahalı hem daha düşük puanlı** olan ürünler elenir.
  3. Kalan ürünler arasında Q farkı 5 puandan azsa **yıllık maliyeti düşük olan kazanır**.
  4. Daha pahalı bir ürün yalnızca iki koşul birlikte sağlanırsa seçilir: en az 5 puan daha iyi olmalı ve her +10 Q için yıllık maliyet artışı, **önceden yazdığınız sınırı** aşmamalı. Varsayılan sınır %20.
- **Duyarlılık kontrolü:** Elektrik fiyatını 0,22–0,35 €/kWh arasında, ömrü ±%30 oynatın. Sıralama değişiyorsa ucuz ve onarılabilir aday seçilir.

---

## 6. Tutara göre katmanlar

| Tutar | Uygulanacak süreç | Tahmini süre |
|---|---|---|
| **< 50 €** | Yalnızca veto kapıları. Ek olarak tek soru: "Sarf malzemesi ya da abonelik tuzağı var mı?" | 5 dk |
| **50–300 €** | Kapılar + 3 çekirdek kriter (uygunluk, performans, kalite) + basit fiyat karşılaştırması | 20–30 dk |
| **> 300 € veya güvenlik açısından kritik ürün** | Tam 3 aşamalı sistem | 1–2 saat |

---

## 7. Muhalefet şerhleri (azınlık görüşleri)

- **K5, kişisel tercih/estetik için ayrı 8 puan istedi.** Gerekçe: gizli tercih ayrı bir puan olarak görünmezse sessizce veto gibi işler. Diğer dört kurul, bunun sonucu önceden istenen ürüne doğru çekmeyi kolaylaştıracağını söyledi. Karar: tercih yalnızca **beraberlikte** karar verdirir. K5'in "**bağırsak kontrolü**" önerisi ise kabul edildi: kazanan açıklandığında hayal kırıklığı hissediyorsanız, yazmadığınız bir kriter var demektir. O kriteri yazın ve süreci baştan yapın, puanları oynamayın.
- **K5, formüllerin sıradan tüketici için fazla karmaşık olduğunu savundu.** Bu itiraz Bölüm 6'daki katmanlarla ve Bölüm 9'daki tek sayfalık listeyle kısmen karşılandı. Rubrikler ve formüller yalnızca 300 €'nun üstünde kullanılır.
- **K1, veri yokluğunda daha sert bir ceza istedi.** Gerekçe: bilgi eksikliğinin maliyetini alıcı değil, ürün taşımalı. Uzlaşma olarak p = 4 kabul edildi.
- **K5, veto sonrası satıcı puanını 0 önerdi.** Gerekçe: NL koruma rubriği aynı göstergeleri zaten ölçüyor. Çoğunluk 5 puanda kaldı.

---

## 8. Tartışmada düzeltilen olgusal hatalar ve doğrulanan mevzuat

**Düzeltilenler**

- **iDEAL korumalı ödeme değildir.** Anlık banka transferidir, chargeback yoktur. K2'nin 1. turdaki hatasını K1 düzeltti.
- **Hollanda'da yasal garanti "2 yıl" değildir.** BW 7:17'ye göre (conformiteit) ürünün **makul beklenen ömrü boyunca** sürer ve satıcıya karşı ileri sürülür. Bu yüzden çoğu durumda **uzatılmış garanti satın almak gereksizdir**.

**Kurulların web kaynaklarıyla doğruladığı güncel bilgiler (Eylül 2026)**

- 1 Temmuz 2026'dan beri AB dışından gelen 150 €'nun altındaki paketlerde kalem başına **3 € gümrük vergisi** alınıyor. 1 Kasım 2026'dan itibaren buna **2 € işlem ücreti** ekleniyor (douane.nl).
- AB **Onarım Hakkı Direktifi**'ne göre, değişim yerine onarım seçilirse yasal garanti 12 ay uzuyor. Hollanda direktifi 31 Temmuz 2026 tarihine kadar iç hukuka aktaramadı; tasarı mecliste bekliyor (Consumentenbond).
- **Telefonlar** (Tüzük 2023/1670, 20 Haziran 2025 sonrası piyasaya çıkan modeller): en az 7 yıl yedek parça, 5 yıl yazılım güncellemesi. Süre, modelin son biriminin piyasaya sürüldüğü tarihten başlar.
- **Çamaşır makineleri** (Tüzük 2019/2023): 10 yıl yedek parça. Ancak kapı, conta ve menteşe gibi bazı parçaları yalnızca tüketici alabiliyor; motor ve pompa gibi parçalar yalnızca profesyonel tamircilere veriliyor.
- **Değiştirilebilir pil zorunluluğu** 18 Şubat 2027'de başlıyor (Pil Tüzüğü md. 11). Kapsamı dar ve dayanıklı pili olan telefonlar için bir istisna var. Bu yüzden rubrikte "kullanıcı pili değiştirebilir mi?" yerine **pil değişiminin maliyeti ve erişimi** ölçülmeli.

Kaynak bağlantıları tutanaklarda: `r1_kurul1_hukuk.md`, `r1_kurul4_finans.md`, `r2_kurul3_muhendislik.md`.

---

## 9. Tek sayfalık uygulama listesi (300 € üstü)

**Ürünlere bakmadan önce:**

1. Olmazsa olmaz 3–5 maddeyi yazın.
2. Bütçe tavanını yazın.
3. Ağırlık ayarını (en fazla ±5) yazın.
4. "+10 puan için en fazla % kaç fazla öderim?" sorusunun cevabını yazın.

**Kısa liste:**

5. 3–5 aday seçin. En az birinin **refurbished veya ikinci el** olmasına dikkat edin.
6. Aynı ürünün farklı satıcılarını ayrı satır olarak listeleyin (ürün × satıcı × ödeme).

**Kapılar:**

7. Beş veto kapısını uygulayın. Elenen ürün puanlanmaz.

**Puanlama:**

8. Her kriteri **bütün ürünler için tek seferde** puanlayın. Uygunluğu incelemeleri okumadan önce puanlayın.
9. Her puanın yanına kaynağını ve güven düzeyini (Y/O/D/Tahmin) yazın.

**Karar:**

10. Q'yu hesaplayın. Q < 60 olanları eleyin. Fark 5 puandan azsa beraberlik sayın.
11. Yıllık maliyeti hesaplayın ve Aşama 3 kuralını uygulayın.
12. Bağırsak kontrolü yapın. Sonra ürünü, en iyi NL koruma ve satıcı puanı olan yerden, **kredi kartı veya PayPal ile** alın.

---

## 10. Bir yapay zekâ asistanıyla (ör. Claude) kullanırken

- Yapay zekâ **kısa liste çıkarır ve soru sorar; nihai puanı siz verirsiniz.**
- Her puan bir kaynakla birlikte gelmeli. **"Veri yoksa boş bırak"** talimatını açıkça verin.
- Fiyat, stok ve kampanya bilgisini tarih damgasıyla **kendiniz kontrol edin**. Model bu bilgilerde güncel olmayabilir.
- AB/NL model varyantını doğrulayın. ABD'deki modelin testi Avrupa varyantına her zaman uymaz.
- Hukuki koruma hücreleri (satıcının AB'de olup olmadığı, Waarborg damgası, iade adresi) kaynaksız doldurulamaz.

---

*Bu rapor 5 yapay zekâ alt ajanından (kurul) ve 2 tur tartışmadan derlenmiştir. Hukuki bilgiler genel bilgilendirme amaçlıdır. Somut bir uyuşmazlıkta Juridisch Loket, ConsuWijzer (ACM) veya Consumentenbond'a danışın.*

# Kurul 3 – Ürün Mühendisliği, Kalite ve Bağımsız Test Kurulu: Görüş (Tur 1)

## 1. Güçlü yönler
- Kalite ve performansa toplam 40 puan verilmesi, fiyatın ve pazarlamanın öne geçmesini engelliyor. Yalnızca spesifikasyona bakan bir sistemden daha sağlam.
- "Gerçek kullanım koşullarında **ölçülen**" ifadesi doğru bir ilke. Üretici beyanı ile kanıtı birbirinden ayırıyor.
- Ömür ve onarımın ayrı bir kalem olması, AB'nin yönü (Ekotasarım, Onarım Hakkı Direktifi 2024/1799) ile uyumlu.

## 2. Zayıf yönler ve kör noktalar
1. **Kanıt tanımı yok.** Kalite, satın almadan önce doğrudan gözlemlenemez; yalnızca *vekil kanıtlarla* tahmin edilir. Sistem hangi kanıtın ne kadar değerli olduğunu söylemiyor. Sonuçta 5 yıldızlı 40 yorum ile Stiftung Warentest'in dayanıklılık testi aynı ağırlığı alabiliyor.
2. **Veri yoksa ne olacağı belirsiz.** Yeni modellerde bağımsız test genellikle 6–12 ay gecikmeyle çıkar. Kural konmazsa kullanıcı boşluğu iyimserlikle doldurur. Bu durumda "bilinmeyen" ürün, kanıtlanmış orta ürünü yener.
3. **Çifte sayım.** "Amaca uygunluk (30)" ile "ölçülen performans (20)" büyük ölçüde örtüşüyor: performans, ancak kullanıcının kullanım profiline göre anlamlı. "Kalite" ile "dayanıklılık/ömür" de iki ayrı kalemde (20 ve 5) bölünmüş.
4. **Onarım ve yazılım desteği 5 puanla fazla düşük.** Akıllı cihazlarda güvenlik güncellemesi biterse cihaz fiilen kullanım dışı kalır. Yedek parça yoksa ilk arızada ekonomik ömür biter. Bu, dayanıklılığın *kendisi*dir, yan konu değildir.
5. **Kaynakların birbirine bağımlılığı görülmüyor.** Consumentenbond, Stiftung Warentest, Which?, OCU ve Test-Achats testlerinin çoğu ICRT ortak laboratuvar verisidir. Üç logo, üç bağımsız kanıt anlamına gelmez.
6. **Kullanıcı yorumlarındaki sistematik hatalar.** J-eğrisi dağılım, teşvikli ve sahte yorumlar, varyant birleştirme (farklı modellerin yorumlarının tek sayfada toplanması) ve ilk hafta coşkusu nedeniyle yıldız ortalaması güvenilirlik hakkında neredeyse hiçbir şey söylemez. AB Omnibus kuralları satıcıyı yorum doğrulama yöntemini açıklamaya zorluyor, ama bu yorumların temiz olduğunu garanti etmez.
7. **Güvenlik ve geri çağırma kontrolü yok.** Safety Gate ve NVWA kayıtları puan değil, eleme kriteri olmalı.

## 3. Somut öneriler

### 3.1 Kaynak hiyerarşisi (kanıt katsayısı)
| Seviye | Kanıt | Katsayı |
|---|---|---|
| A | Bağımsız laboratuvar testi, metodolojisi açık: Consumentenbond/ICRT, Stiftung Warentest, Which?, RTINGS (ölçüm verisi); resmi AB verisi: EPREL, enerji etiketi, AB onarılabilirlik sınıfı | 1,0 |
| B | Büyük örneklemli sahip anketleri ve arıza verisi: Consumentenbond/Which? *betrouwbaarheid* anketleri, Consumer Reports, Backblaze (diskler); iFixit sökme incelemesi; Fransız onarılabilirlik/dayanıklılık endeksi | 0,8 |
| C | Uzman editoryal incelemesi (Tweakers, Les Numériques vb.). Genellikle kısa süreli kullanıma dayanır. | 0,6 |
| D | Doğrulanmış alıma dayalı, **6 ay ve üzeri** uzun dönem kullanıcı yorumları; Tweakers/Reddit forumlarındaki tekrarlayan arıza örüntüleri | 0,4 |
| E | Yıldız ortalaması, üretici beyanı, influencer içerikleri | 0,2 |

Kurallar:
- Aynı ICRT verisini kullanan kaynaklar tek kaynak sayılır.
- Yorumlarda 1–3 yıldızlı ve "X ay sonra" ifadesi geçen yorumlar okunur. Arıza türü tekrar ediyorsa (ör. pompa, menteşe, pil şişmesi) bu **negatif A-seviyesi sinyal** kabul edilir.
- Uzun ticari garanti (≥5 yıl) üreticinin kendi arıza verisine güvendiğini gösteren bir sinyaldir; B seviyesinde değerlendirilir.

### 3.2 Alt göstergeler ve 0–10 rubrikler

**a) Ölçülen performans.** Alt göstergeler kullanıcının kullanım profiline göre ağırlıklandırılır. Örnekler: çamaşır makinesinde yıkama etkinliği, durulama, sık kullanılan programda gerçek kWh ve süre, gürültü; dizüstü bilgisayarda standart pil testi, ısıl kısılma (termal throttling), ekran; televizyonda parlaklık, kontrast, giriş gecikmesi.
- 9–10: En az iki bağımsız A kaynağında ana metriklerde kategori üst %20'si.
- 7–8: Bir A kaynağında üst yarı ya da tutarlı C kaynakları.
- 5–6: Yalnızca C kaynakları, ortalama sonuç.
- 3–4: Yalnızca üretici beyanı ve karışık kullanıcı yorumları.
- 0–2: Ölçülmüş zayıflık ya da beyan ile ölçüm arasında çelişki.

**b) Güvenilirlik ve dayanıklılık.** Alt göstergeler: marka/kategori arıza oranı (sahip anketi), laboratuvar dayanıklılık testi (Warentest ve Consumentenbond süpürge, blender, çamaşır makinesi testleri), AB etiketindeki düşme ve IP sınıfı, pil döngü ömrü (telefonda en az 800 döngüde %80 kapasite), sökme incelemesinde görülen yapı kalitesi, geri çağırma geçmişi, ticari garanti süresi.
- 9–10: Sahip anketinde üst çeyrek, dayanıklılık testini geçmiş, ≥5 yıl garanti.
- 7–8: Anket verisi ortalamanın üstünde ve olumsuz örüntü yok.
- 5–6: Yalnızca marka düzeyinde veri var ve nötr.
- 3–4: Uzun dönem yorumlarda tekrarlayan arıza.
- 0–2: Sistematik kusur. Geri çağırma varsa ürün elenir.

**c) Onarılabilirlik, yedek parça ve yazılım desteği.** Alt göstergeler: AB onarılabilirlik sınıfı (A–E) veya iFixit/Fransız endeksi; yazılı olarak taahhüt edilmiş güncelleme süresi (telefonlarda AB asgarisi 5 yıl); yedek parça süresi (telefon 7 yıl, çamaşır makinesi 10 yıl); parça fiyatının cihaz fiyatına oranı; pilin kullanıcı tarafından değiştirilebilmesi (AB Pil Tüzüğü, 2027); parça eşleştirme (*parts pairing*) engeli olmaması; bağımsız servis ağına erişim.
- 10: A sınıfı veya iFixit ≥8, en az 7 yıl yazılı güncelleme taahhüdü, parça fiyatları yayımlanmış.
- 7–8: B sınıfı, 5–6 yıl güncelleme.
- 5: C sınıfı, 3–4 yıl güncelleme.
- 2–3: D–E sınıfı, taahhüt belirsiz.
- 0: Yapıştırılmış veya eşleştirilmiş parçalar, parça yok, güncelleme taahhüdü yok.

### 3.3 Veri yoksa
- **Puan hesabı:** Nihai puan = ham puan × (0,5 + 0,5 × kanıt katsayısı).
- **Hiç veri yoksa:** ham puan 4/10 alınır. Nötrün altındadır, çünkü belirsizliğin bir maliyeti vardır.
- **Yeni model:** Önceki nesil veya aynı platform verisi kullanılır, %20–30 indirimle.
- **Belirsizlik bandı:** Sonuç ±aralıkla raporlanır. İki ürünün bantları çakışıyorsa karar puanla değil, garanti ve iade kolaylığı ile fiyat üzerinden verilir.
- **Bekleme seçeneği:** Karar erteleyebiliyorsa, ilk bağımsız test yayımlanana kadar beklemek meşru bir seçenektir.

## 4. Kurul 3'ün önerdiği ağırlık tablosu
| Ölçüt | Puan |
|---|---|
| İhtiyaca uygunluk: eleme kriterleri ve kullanım profiline uyum | 25 |
| Bağımsız ölçülmüş performans (kullanım profiline göre ağırlıklı) | 20 |
| Güvenilirlik ve dayanıklılık | 15 |
| Onarılabilirlik, yedek parça, yazılım destek süresi | 12 |
| Toplam sahip olma maliyeti: fiyat, enerji, sarf malzemesi, parça | 12 |
| Hollanda'da garanti, servis ve iade | 9 |
| Satıcı ve işlem güvenliği | 7 |
| **Toplam** | **100** |

**Ek kurallar**
- Güvenlik, geri çağırma ve CE uygunluğu puan değil, **eleme kriteri**dir.
- Kategoriye göre ayar yapılır:
  - Akıllı cihaz ve telefonda onarım/yazılım 15'e çıkar, performans 17'ye iner.
  - Elektronik olmayan ürünlerde (mobilya, alet) yazılım alt göstergesi düşer ve 12 puanın tamamı dayanıklılık ile parçaya aktarılır.
- 20, 15 ve 12 puanlık kalemlere 3.3'teki kanıt katsayısı uygulanır.

# Kurul 2 — Karar Bilimi ve Metodoloji Kurulu: Birinci Tur Görüşü

**Hüküm:** Sistem iyi bir *kontrol listesi*, ama *karar modeli* olarak kullanılırsa yanıltır. Yapısı tek aşamalı, telafi edici bir ağırlıklı toplam (WSM). Fiyat yok, veto yok, veri güveni yok. Önerimiz üç aşamalı bir modele geçmek: **eleme → kalite puanı → değer**.

## 1. Güçlü yönler

- **İhtiyaç önce geliyor.** En yüksek ağırlık (30) "amaca uygunluk"ta. Karar biliminde ilk ilke de budur: ürün kullanıcının senaryosuna göre değerlendirilir.
- **Kanıt vurgusu var.** "Gerçek kullanım koşullarında ölçülen performans" ifadesi, üreticinin beyanı yerine gözlenmiş veriyi istiyor.
- **Bağlam yerel.** Hollanda'daki garanti, servis ve iade koşulları ayrı bir kriter. Soyut modellerin çoğu satın alma sonrası riski atlar.
- **Toplam sahiplik maliyeti var.** Sahiplik maliyeti ve onarılabilirlik düşünülmüş; bu, yalnız etiket fiyatına bakmaktan daha olgun bir bakış.

## 2. Metodolojik zayıflıklar

1. **Çift sayım ve hale etkisi.** "Uygunluk", "kalite/dayanıklılık" ve "performans" birlikte 70 puan ediyor ve aynı gizli değişkeni ölçüyor: "iyi ürün mü?". Değerlendirici bir üründen hoşlanırsa üç kriterde birden yüksek puan verir. "Kalite, dayanıklılık" ile "kullanım ömrü, onarılabilirlik" de kısmen örtüşüyor. WSM'nin temel varsayımı olan *tercihsel bağımsızlık* burada ihlal ediliyor.
2. **Fiyat görünmüyor.** "Teslim maliyeti ve uzun dönem sahiplik değeri" (8 puan) fiyatı kapsıyor mu, belli değil. Kapsıyorsa, 3 kat pahalı bir ürün yalnızca birkaç puan kaybeder. Kapsamıyorsa, model sistematik olarak pahalı ürünü seçer. İki durumda da maliyet ile fayda aynı toplama karışıyor, oysa bunlar ayrı boyutlardır.
3. **Telafi edici modelin riski.** Güvenlik açığı olan, sahte satıcıdan alınan ya da ihtiyacı karşılamayan bir ürün, diğer kriterlerden puan toplayıp 75/100 alabilir. "Satıcı ve işlem güvenliği" 7 puanlık bir kalem olamaz; ya geçer ya kalır.
4. **Bazı ağırlıklar gürültünün altında.** 0–10 ölçekte ±1'lik tipik bir puanlama hatası, 30 ağırlıklı kriterde ±3 puan eder. Bu durumda 5 puanlık "ömür/onarılabilirlik" kriteri sonuca fiilen etki etmez; yalnızca görüntü için orada durur.
5. **Ölçek tanımsız.** "20 puan" nasıl verilecek, belli değil. Puanı belirleyen çapalar (rubrik) olmadan iki kişi, hatta aynı kişi farklı günlerde, farklı skor üretir.
6. **Ağırlıklar sabit.** Bir USB kablosunda "performans %20" anlamsız. Bir çamaşır makinesinde ise onarılabilirlik %5'ten çok daha önemli.
7. **Belirsizlik yok sayılıyor.** Bağımsız laboratuvar testinden gelen 8 ile tek bir YouTube yorumundan gelen 8 aynı muameleyi görüyor.
8. **Bilişsel yük yüksek.** 7 kriteri 15 €'luk bir alışverişte uygulamak gerçekçi değil. Kullanıcı ya sistemi bırakır ya da puanları uydurur.

## 3. Somut öneriler

### Aşama 1: Eleme kapıları (veto, evet/hayır)
- İhtiyacın asgari gereksinimleri karşılanıyor (ör. ölçü, uyumluluk, kapasite).
- Güvenlik ve uyumluluk: CE işareti var, bilinen bir geri çağırma yok.
- Satıcı güvenilir: kayıtlı işletme; iDEAL veya kredi kartı gibi korumalı ödeme; AB içinden satış (14 günlük cayma hakkı ve 2 yıllık yasal uygunluk garantisi geçerli).
- Toplam sahip olma maliyeti (TCO) bütçe tavanının altında.

Bir kapıdan geçemeyen ürün puanlanmaz.

### Aşama 2: Kalite puanı Q (0–100, fiyat hariç)

**Rubrik.** Her kriter 0–10 arasında puanlanır ve her seviye tanımlıdır:

| Puan | Anlamı |
|---|---|
| 0 | Kabul edilemez |
| 2 | Belirgin eksik |
| 4 | Asgari yeterli |
| 6 | Kategori ortalaması |
| 8 | Ortalamanın belirgin üstü |
| 10 | Kategorinin en iyisi, bağımsız kaynakla doğrulanmış |

**Veri güveni katsayısı c.** Her puana bir güven düzeyi atanır:

| Kaynak | c |
|---|---|
| Bağımsız test (Consumentenbond, Tweakers vb.) | 1,0 |
| Çok sayıda doğrulanmış kullanıcı yorumu | 0,8 |
| Tek kaynak | 0,6 |
| Yalnız üretici beyanı | 0,4 |

Düzeltilmiş puan şöyle hesaplanır: *s' = c·s + (1−c)·5*. Yani belirsiz puan, katsayıyla çarpılıp cezalandırılmak yerine nötr değere (5) doğru çekilir. Bu "büzülme" yaklaşımı, bilgisi az olan ürünü haksız yere sıfıra itmez ama abartılı iddiayı da ödüllendirmez.

**Kategoriye göre ağırlık.** Aşağıdaki bölüm 4'teki taban tablo, kategoriye göre ±5 puan aralığında ayarlanır. Örnekler:
- Elektronikte yazılım desteği ön plana çıkar.
- Beyaz eşyada onarılabilirlik ve servis ön plana çıkar.
- Sarf malzemesinde amaca uygunluk ve fiyat ön plana çıkar.

### Aşama 3: Değer ve karar
- Karar TCO üzerinden verilir: satın alma fiyatı + teslimat + işletme maliyeti (enerji, sarf, abonelik) − ikinci el değeri.
- Önce Pareto elemesi yapılır: hem daha pahalı hem daha düşük Q'lu ürünler atılır.
- Kalan ürünler için şu soru sorulur: *"Ek her 10 Q puanı için ödenen ek € makul mü?"*
- **Q/€ oranı tek başına kullanılmaz.** Bu oran çok ucuz ve vasat ürünü ödüllendirir. Oran ancak bir kalite eşiğinden (ör. Q ≥ 60) geçen ürünler arasında anlamlıdır.

### Duyarlılık ve beraberlik kuralı
- Ağırlıklar ±%20 oynatıldığında sıralama değişiyorsa, sonuç "istatistiksel beraberlik" sayılır.
- Aynı şekilde, Q farkı 5 puanın altındaysa sonuç beraberlik sayılır.
- Beraberlik varsa karar ucuz olanın ya da iade koşulu daha iyi olanın lehine verilir.

### Katmanlı uygulama (bilişsel yükü azaltmak için)

| Fiyat | Süreç |
|---|---|
| < 50 € | Yalnız Aşama 1 kapıları, ardından en ucuz güvenilir seçenek |
| 50–300 € | Kapılar + 3 ana kriter (uygunluk, performans, güvenilirlik) + TCO |
| > 300 € veya uzun ömürlü ürün | Tam model + duyarlılık kontrolü |

## 4. Kurulumuzun önerdiği ağırlıklar (Aşama 2, fiyat hariç, toplam 100)

| Kriter | Ağırlık | Kategoriye göre aralık |
|---|---|---|
| İhtiyaca/kullanım senaryosuna uygunluk | 30 | 25–40 |
| Ölçülmüş performans (bağımsız test) | 20 | 10–25 |
| Güvenilirlik ve dayanıklılık (arıza oranı, malzeme) | 20 | 15–25 |
| Ömür: onarılabilirlik, yedek parça, yazılım destek süresi | 15 | 5–20 |
| Hollanda'da garanti, servis ve iade süreci | 10 | 5–15 |
| Satıcı hizmet kalitesi (vetodan sonra kalan fark) | 5 | 0–10 |
| **Toplam** | **100** | |

Ağırlıklarda neler değişti:
- **Fiyat ve teslim maliyeti tablodan çıkarıldı**, Aşama 3'e (TCO) taşındı.
- **Satıcı güvenliği ikiye ayrıldı.** Güvenlik kısmı artık Aşama 1'de bir veto kapısı. Satıcının hizmet kalitesindeki fark ise tabloda 5 puanlık bir kriter olarak kaldı.
- **"Ömür" kriteri 5'ten 15'e çıkarıldı.** Yeni tanımı ölçülebilir göstergelere dayanıyor: yedek parça bulunabilirliği, yazılım güncelleme süresi ve AB onarılabilirlik endeksi (reparability score).
- **"Güvenilirlik" kriteri yalnız arıza ve dayanıklılık verisine sınırlandı.** Böylece performans ve uygunluk kriterleriyle çift sayım azaltıldı.

## Kurulun üç ana tezi

1. **Maliyet ile faydayı aynı toplama koymayın.** Önce kalite puanını hesaplayın, sonra TCO ile ayrı bir aşamada karşılaştırın.
2. **Telafi edilmemesi gereken koşullar veto olmalı.** Güvenlik, satıcı güvenilirliği, asgari ihtiyaç ve bütçe tavanı puan kalemi değil, eleme kapısıdır.
3. **Puan, kanıt ve bağlam kadar güvenilirdir.** Çapalı rubrik, veri güveni katsayısı, kategoriye göre ayarlanan ağırlıklar, duyarlılık kontrolü ve fiyata göre katmanlı süreç olmadan 100 puanlık bir skor sahte bir kesinlik üretir.

# Kurul 5: Kullanıcı Deneyimi ve Şeytanın Avukatı — 1. Tur

**Genel hüküm:** Sistem, pahalı ve uzun ömürlü alımlar için iyi bir **düşünme iskeleti**. Ama bir **karar makinesi** olarak kullanılırsa sahte kesinlik üretir, zaman yer ve kullanıcının zaten vermiş olduğu kararı "bilimsel" gösterip meşrulaştırır. Sorun ölçütlerde değil, sistemin nasıl kullanılacağında.

## 1. Sistemin gerçekten işe yaradığı durumlar

- **Yüksek tutar, düşük sıklık:** Çamaşır makinesi, dizüstü bilgisayar, bisiklet (NL'de fiilen ulaşım aracı) gibi alımlarda hata pahalıya patlar. Burada 30–60 dakikalık yapılandırılmış düşünmeye değer.
- **Pazarlama gürültüsüne karşı:** "Gerçek kullanım performansı" ve "Hollanda'da servis/iade" ölçütleri, spec tablosu ile indirim etiketinin büyüsünü kırar. Ucuz ama NL'de servisi olmayan bir marketplace ürününü eler.
- **Ortak kararlar:** Eş veya aile birlikte karar verirken ağırlıkları önceden konuşmak tartışmayı somutlaştırır.
- **Unutulan boyutlar:** Onarılabilirlik, iade kolaylığı ve satıcı güvenliği gibi ölçütler içgüdüsel alışverişte hiç akla gelmez. Liste bunları hatırlatır.

## 2. En güçlü itirazlar

1. **Sahte kesinlik.** 72,4 ile 71,8 puan arasındaki fark gürültüdür. Her ölçüt tahmine dayalı ve ±3–5 puan oynuyor. Ondalıklı sonuç, olmayan bir ölçüm hassasiyeti izlenimi verir. Farkı 5 puandan az olan seçenekler **beraberlik** sayılmalı.
2. **Motivated reasoning.** İnsan çoğu zaman önce kalbiyle seçer, sonra puanları buna göre ayarlar. "Amaca uygunluk 30 puan" en öznel ölçüt ve en yüksek ağırlık da onda. Bu, sonucun yönünü değiştirmek için ideal bir kaldıraç. Sistem kendini yanıltmayı kolaylaştırabilir.
3. **Fiyatın kendisi yok.** Tabloda "teslim maliyeti ve sahiplik değeri" var ama satın alma fiyatı açıkça yer almıyor. 400 € ile 900 € arasındaki fark bu sistemde görünmez kalabilir. Bu tasarım açığıdır. Ya fiyat bir ölçüt olmalı ya da "puan/€" oranı hesaplanmalı.
4. **Ölçekleme yok.** 20 €'luk bir şarj kablosu için 7 ölçütlük analiz, kablonun değerinden daha pahalı bir zaman harcamasıdır. Schwartz'ın bulgusu açık: her kararda en iyiyi arayanlar (maximizers) ortalamada daha iyi seçenek bulsa da daha az tatmin olur ve daha çok pişmanlık yaşar. Çoğu alım için "yeterince iyi" (satisficing) doğru stratejidir.
5. **Duygu, estetik ve ekosistem görünmez.** iPhone kullanan biri için AirPods ile rakibi arasındaki fark büyük ölçüde ekosistem uyumudur. "Bu ürünü sevecek miyim?" sorusu, kullanım sıklığını ve memnuniyeti belirleyen gerçek bir değişkendir. Bunu puanlamaya almamak, onu gizli bir veto hâline getirir.
6. **Yapay zekâ riskleri.** Bir asistana puanlatıldığında şu riskler doğar: uydurulmuş test sonuçları, eski fiyatlar, NL'de satılmayan modeller, ABD'ye özgü garanti bilgisi. Hepsi eşit güvenle yazılır. Yapay zekâ 7 ölçütün hepsini doldurur, "bilmiyorum" demez. **Kesin görünen bir tablo, belirsiz bir veriden daha tehlikelidir.**
7. **Karar yorgunluğu.** 5 ürün × 7 ölçüt = 35 ayrı yargı demektir. Bu kadar yargıdan sonra verilen son kararlar özensizleşir.

## 3. Somut öneriler

**a) Tutara göre mod:**
| Tutar | Mod | Süre |
|---|---|---|
| < 50 € | Puanlama yok. İyi yorumlu, iadesi kolay satıcıdan al. | 2 dk |
| 50–300 € | 5 dakikalık kontrol listesi | 5–15 dk |
| > 300 € veya güvenlik/sağlık ürünü | Tam 100 puanlık sistem | 30–60 dk |

**b) 5 dakikalık kontrol listesi (geçti/kaldı):**
1. Zorunlu 2–3 ihtiyacımı karşılıyor mu? (Hayırsa elenir.)
2. Bağımsız bir kaynakta (Consumentenbond, Tweakers, RTINGS vb.) olumsuz bir bulgu var mı?
3. Satıcı NL/AB'de mi? 14 günlük cayma hakkı ve kolay iade var mı?
4. Toplam maliyet (kargo, aksesuar, sarf malzemesi) bütçemde mi?
5. Mevcut cihazlarımla uyumlu mu ve onu kullanmak istiyor muyum?
Beşi de "evet" ise en ucuz ya da en sevdiğin seçeneği al ve aramayı bırak.

**c) Önyargıya karşı koruma:**
- **Ağırlıkları, aday ürünlere bakmadan önce yaz ve sabitle.** Sonradan değişiklik yapılmaz.
- **Önce zorunlu gereksinim kapısı:** Amaca uygunluğun bir kısmı "olmazsa olmaz" filtresine dönüşür. Kalan puan, gerçekten derecelendirilebilen yönler içindir.
- **Kör puanlama:** Mümkünse marka ve fiyatı gizleyerek puanla. En azından her ölçütü tüm ürünler için tek seferde puanla, ürün ürün değil.
- **1–5 ölçeği kullan:** Ağırlıkla çarp ve sonucu 5'in katına yuvarla.
- **Duyarlılık testi:** Ağırlıkları ±5 oynattığında kazanan değişiyorsa sonuç kırılgandır. Bu durumda karar, kişisel tercihe veya fiyata bırakılır.
- **Bağırsak kontrolü:** Kazanan ürün açıklandığında hayal kırıklığı hissediyorsan, bu gizli bir ölçütün habercisidir. O ölçütü görünür yap, kendini kandırma.

**d) Yapay zekâ ile kullanım kuralları:**
- **Kaynak zorunluluğu:** Her performans ve güvenilirlik iddiası link veya kaynak adıyla gelmeli. Kaynağı olmayan iddia puanlamaya girmez.
- **Veri güveni işareti:** Her hücre için Yüksek/Orta/Düşük/Tahmin. "Düşük" ve "Tahmin" hücrelerinin sayısı fazlaysa toplam puan raporlanmamalı.
- **Fiyat ve stok:** Yapay zekâya asla güvenme. Tarih damgalı olarak kendin kontrol et (Tweakers Pricewatch, satıcı sitesi).
- **Model kodu kontrolü:** AB/NL varyantı ile ABD varyantı aynı mı?
- **"Bilmiyorum" izni:** Asistana açıkça "veri yoksa boş bırak, uydurma" talimatı ver.
- Yapay zekânın rolü **kısa liste çıkarmak ve soru sormak** olmalı, nihai puanı vermek değil.

## 4. Kurul 5'in önerdiği ağırlık tablosu

Ön kapılar (puan dışı, geçti/kaldı): zorunlu ihtiyaçlar, güvenilir satıcı, bütçe tavanı.

| Ölçüt | Orijinal | Kurul 5 |
|---|---|---|
| Amaca uygunluk (kapı sonrası derecelendirilebilen kısım) | 30 | 25 |
| Kalite, dayanıklılık, güvenilirlik | 20 | 18 |
| Gerçek kullanım performansı | 20 | 17 |
| **Fiyat + toplam sahip olma maliyeti** (satın alma, kargo, sarf malzemesi, enerji) | 8 | 12 |
| **Ekosistem uyumu ve kişisel tercih** (estetik, kullanım keyfi) | — | 10 |
| NL'de garanti, servis, iade | 10 | 8 |
| Satıcı ve işlem güvenliği (kapıyı geçenler arasında) | 7 | 5 |
| Ömür, onarılabilirlik, sürdürülebilirlik | 5 | 5 |
| **Toplam** | 100 | **100** |

**Gerekçe:** Satıcı güvenliği ve temel uygunluk puan değil eşik meselesidir. Dolandırıcı bir satıcı, başka alanlardan puan toplayarak telafi edilememeli. Fiyat açıkça görünür olmalı. Kişisel tercih masaya konmalı ki gizli bir veto olmaktan çıksın. Ağırlıklar, tutar kademesine göre değil **ürün kategorisine göre** de ayarlanabilir (ör. elektronikte ekosistem ağırlığı daha yüksek), ama bu ayar **puanlamadan önce** yapılmalıdır.

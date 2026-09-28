# Kurul 4 (Finans/TCO) — 2. Tur

**Uzlaşı maddeleri:** U1–U4'ü kabul ediyoruz. U1'e bir ek öneriyoruz: bütçe tavanı kapısı etiket fiyatına değil, **TCO**'ya uygulanmalı. U3'e bir ek öneriyoruz: 50 €'nun altındaki alımlarda hesap yapılmaz, yalnızca "sarf malzemesi veya abonelik tuzağı var mı?" diye sorulur. Yazıcı ve robot süpürge bu tuzağın tipik örnekleri.

## 1. İtirazlarımız

1. **Kurul 2'ye:** Aşama 3'teki "Ek € makul mü?" sorusu kararı yeniden sezgiye bırakıyor. Değer aşaması da çapalı olmalı ve kullanıcı ödeme istekliliğini ürünlere bakmadan önce yazmalı. İki ayrıntı daha var:
   - Kurul 2, iDEAL'i "korumalı ödeme" saymış. Kurul 1 haklı: iDEAL'de chargeback yok.
   - Karşılaştırma etiket fiyatıyla değil, **€/yıl** ile yapılmalı. Aksi hâlde 12 yıl dayanan ürün, 5 yıl dayanan ürüne karşı haksızlığa uğrar.
2. **Kurul 3'e:** Performans rubriğine "gerçek kWh" koymuşsunuz, oysa enerji zaten TCO'nun içinde. Bu **çift sayım**. Enerjinin ölçümü performansa ait olabilir, ama €'ya çevrilmiş hâli yalnızca TCO'da yer almalı. Ayrıca veri eksikliğinde önerdiğiniz çarpımsal ceza, ham×(0,5+0,5c), yüksek puanlı yeni ürünü düşük puanlı ürünlerden daha fazla cezalandırıyor. Yani ceza, belirsizliğin büyüklüğüne değil ürünün ham puanına göre artıyor.
3. **Kurul 5'e:** 10 puanlık "kişisel tercih" kalemi, kendi 2. itirazınızla (motivated reasoning) çelişiyor, çünkü sonucu yönlendirmek için en kolay kaldıraç bu. Ekosistemin ise ölçülebilir bir karşılığı var:
   - Uyum, uygunluk kalemine girer.
   - Geçiş ve kilitlenme maliyeti TCO'ya girer. Örneğin şarj cihazını ya da aboneliği yeniden almak gerekir.

## 2. İkna olduğumuz ve pozisyon değiştirdiğimiz noktalar

- **Kurul 2 — fiyat ayrı bir aşama olmalı. Bu noktada pozisyonumuzu değiştirdik.** 1. turdaki formülümüz `18 × (en düşük €/yıl ÷ aday)` göreliydi: aday setine bağlıydı. Kümeye alakasız bir ucuz ürün eklenince diğer adayların puanı ve sıralaması değişebiliyordu (sıra dönmesi). Formül ayrıca "1 puan = X €" şeklinde, kullanıcıya hiç sorulmamış gizli bir kur dayatıyordu. Maliyet ile fayda ayrı tutulursa ikisi de görünür kalır. Tek şartımız var: Aşama 3 TCO/yıl ile ve açık bir kuralla çalışmalı.
- **Kurul 1 — değerlendirme birimi "ürün × satıcı × ödeme" olmalı.** Finansal açıdan da doğru: aynı ürünün TCO'su satıcıya göre değişiyor. Değiştiren kalemler iade kargosu, gümrükte kalem başına 3 € + 2 € ve risk payı (R_risk).
- **Kurul 3'ün onarım rubriği bizimkinden daha iyi.** Parça fiyatının cihaz fiyatına oranı ve parça eşleştirme engeli (parts pairing) doğrudan B'yi (bakım/onarım maliyeti) ve N'yi (ömür) belirliyor. Rubriği benimsiyoruz.

**Önerdiğimiz Aşama 3 kuralı:**
1. Kapılardan geçen ve Q ≥ 60 olan adaylar alınır.
2. Pareto elemesi yapılır: hem daha pahalı hem daha düşük Q'lu adaylar çıkarılır.
3. En düşük €/yıl'a sahip aday referans olur.
4. Daha pahalı bir aday ancak iki koşul birlikte sağlanırsa seçilir:
   - ΔQ ≥ 5, yani fark beraberlik eşiğinin üstünde.
   - Her +10 Q için €/yıl artışı, kullanıcının önceden yazdığı sınırı aşmıyor. Varsayılan sınır %20.
5. Duyarlılık testi: elektrik 0,22–0,35 €/kWh ve ömür ±%30 aralığında denenir. Sonuç değişiyorsa ucuz ve onarılabilir aday seçilir.

## 3. Oylarımız

- **S1:** Fiyat **ayrı aşamada** değerlendirilmeli (Kurul 2). Şartımız: TCO/yıl kullanılmalı, kural açık olmalı, bütçe tavanı TCO üzerinden bir kapı olmalı.
- **S2:** Kurul 2'nin büzülme formülünü destekliyoruz, ama nötr 5 yerine öncül değer olarak **4** kullanılmalı: s′ = c·s + (1−c)·4. Önceki nesil verisi varsa öncül o olmalı. Belirsizliğin finansal bir maliyeti var, ama bu maliyet ürünün ham puanıyla orantılı olmamalı.
- **S3:** Satıcıya veto sonrası **5 puan** kalmalı. Kurul 1'in "ürün × satıcı × ödeme" birimini destekliyoruz.
- **S4:** Ayrı bir kriter olmamalı. Ekosistem uyumu uygunluğa, geçiş maliyeti TCO'ya girmeli. Kişisel tercih yalnızca beraberlik (<5 puan fark) durumunda karar kırıcı olmalı.
- **S5:** Kalemler şöyle ayrılmalı:
   - Uygunluk: senaryo ve özellik uyumu (kapı sonrası).
   - Performans: ölçülen sonuç.
   - Kalite: zaman içindeki arıza oranı.
   - € cinsinden her şey (enerji, sarf, ömür) yalnızca Aşama 3'te.
- **S6:** Onarılabilirliğe **14 puan** verilmeli. Fiyat Q'nun dışına çıktığı için ömrü güvenceye alan bu kalemin payı artmalı.

## 4. Revize nihai ağırlık oyumuz (Q, fiyat hariç)

| Kalem | Puan |
|---|---|
| Uygunluk (ekosistem uyumu dahil) | 30 |
| Ölçülen performans | 20 |
| Kalite/dayanıklılık | 18 |
| Onarım/parça/yazılım/ömür | 14 |
| **TCO/fiyat** | **0 (ayrı Aşama 3: €/yıl + açık kural)** |
| NL garanti-servis-iade (hukuki koruma) | 13 |
| Satıcı (veto sonrası) | 5 |
| Ekosistem/tercih | 0 (uygunluk içinde; tercih yalnızca beraberlik kırıcı) |
| **Toplam** | **100** |

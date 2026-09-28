# Kurul 2 — Karar Bilimi ve Metodoloji: 2. Tur

**Uzlaşı maddeleri:** U1–U4'e itirazımız yok. U4 için bir not: 5 puandan küçük farkların beraberlik sayılması kuralı, yalnızca tek bir kalite toplamı hesaplanıyorsa anlamlıdır. Maliyet de aynı toplamın içine girerse bu 5 puanlık eşiğin ne ölçtüğü belirsizleşir.

## 1. En güçlü itirazlarımız

**a) Kurul 4: `TCO puanı = 18 × (en düşük €/yıl ÷ adayın €/yıl)` formülü sıralama tersinmesi (rank reversal) üretir.**
- Bu oran normalizasyonu aday kümesine bağlıdır. Listeye çok ucuz bir aday eklendiğinde bütün adayların TCO puanı orantılı olarak düşer. Diğer kriterler değişmediği için, A ile B'nin kendi aralarındaki sıralaması bile yer değiştirebilir.
- Ayrıca ölçek doğrusal değildir: €/yıl iki katına çıktığında TCO puanı yarıya iner, üç katına çıktığında ancak üçte birine iner. Yani pahalılaştıkça ek ceza giderek azalır.
- Kurul 4'ün kendi "azalan getiri" kuralı, yani "ek maliyet puanda aynı oranda artış sağlamıyorsa ucuz model seçilir", zaten ayrı bir fiyat aşaması demektir. Bu aşama doğru olduğuna göre fiyatı toplamın içine ayrıca koymak gereksizdir.

**b) Kurul 1: Satıcı 8 + hukuki koruma 14 = 22 puan, aynı değişkeni iki kez sayıyor.**
- Conformiteit hakkı satıcıya karşı ileri sürülür. Geschillencommissie üyeliği, Thuiswinkel Waarborg ve iade koşulları da satıcının nitelikleridir. Dolandırıcılık riski ise zaten veto kapısında eleniyor.
- Kurul 1'in "ürün × satıcı × ödeme" tezini destekliyoruz, ama bir fark koyuyoruz. Bu tez, satıcının iki ayrı satırda puanlanmasını değil, kararın iki adımda verilmesini gerektirir:
  1. Önce ürün seçilir.
  2. Sonra o ürün için en iyi satıcı ve ödeme kombinasyonu seçilir.
- Satıcı, ürünün kalitesini değiştirmez. Değiştirdiği şey riskin kendisi ve TCO'dur.

**c) Kurul 5: 10 puanlık "ekosistem/kişisel tercih" kriteri, Kurul 5'in kendi 2. itirazını, yani güdülenmiş akıl yürütme riskini büyütüyor.**
- Ölçülemeyen ve en öznel bu kalem, sonucu istenen yöne çekmek için en uygun kaldıraçtır.
- Ekosistem uyumu nesnel olarak kontrol edilebilir (örneğin cihaz iOS ile çalışıyor mu?). Bu yüzden "uygunluk" kriterinin alt göstergesi olmalı.
- Beğeni ise puan olmamalı. Yalnızca beraberlik bandında kararı bozan ölçüt (tie-breaker) olarak kullanılmalı.

## 2. İkna olduğumuz noktalar

- **Kurul 3 haklı: saf nötre çekme bilinmeyen ürünü ödüllendiriyor.** Birinci tur formülümüzde (s' = c·s + (1−c)·5), üreticinin "9" dediği ve güveni c = 0,4 olan bir ürün 6,6 alıyor. Bu, kanıtlanmış bir 5'i yeniyor. Formülü şöyle düzelttik:
  - Yeni formül: **s' = c·s + (1−c)·p**. Buradaki p, "önsel" değerdir: veri yokken başlangıçta varsayılan puan.
  - p, önceki nesil veya marka verisinden alınır ve Kurul 3'ün önerdiği gibi %20–30 indirimle kullanılır. Böyle bir veri yoksa p = 4 alınır, yani belirsizliğin bir maliyeti vardır.
  - Kurul 3'ün "ham × (0,5 + 0,5c)" çarpanını ise kabul etmiyoruz. Bu çarpan puanı sıfıra doğru çekiyor ve "veri yoksa 4" kuralıyla birlikte aynı belirsizliği iki kez cezalandırıyor.
  - Kurul 3'ün belirsizlik bandı ve "bekleme seçeneği" önerilerini aynen benimsiyoruz.
- **Kurul 4'ün €/yıl metriği (TCO/N), bizim 3. aşamamızın ölçüsü olmalı.** Etiket fiyatından üstündür. Ömrü, enerjiyi ve ikinci el değerini tek bir sayıda topluyor.
- **Uygunluk kriterinin ağırlığı düşürülmeli (Kurul 3, 4 ve 5).** Uygunluğun "olmazsa olmaz" kısmı artık veto kapısına taşındı. Kalan, derecelendirilebilir kısım 30 puanı hak etmiyor.
- **Onarılabilirlik için 15 puan fazla.** Kurul 3'ün ürün kategorisine göre ayar önerisi (elektronik olmayan ürünlerde yazılım alt göstergesinin düşmesi) karşısında taban değeri 12'ye çekiyoruz.

## 3. S1–S6 oylarımız

- **S1 Fiyat:** Fiyat ayrı bir aşama olmalı. Aşama 2'de kalite puanı Q hesaplanır. Aşama 3'te Q'su 60 ve üzeri olan adaylar arasında önce Pareto elemesi yapılır (hem daha pahalı hem daha zayıf olanlar atılır). Sonra €/yıl üzerinden marjinal karar verilir: "ek her 10 puan için ödenen ek € makul mü?". Kurul kararı fiyatın toplamın içinde olması yönünde çıkarsa, bölüm 4'teki yedek tabloyu ve 1a'daki formül yerine min–max normalizasyonunu öneriyoruz.
- **S2 Veri yokluğu:** Belirsiz puan, bir önsel değere doğru çekilir: s' = c·s + (1−c)·p. Önsel p, önceki nesil ya da marka verisinden gelir; bu veri yoksa p = 4'tür. Çarpımsal ceza uygulanmaz. Sonuç bir belirsizlik bandıyla raporlanır.
- **S3 Satıcı:** Veto kapısından sonra satıcıya 5 puan kalmalı. Kurul 1'in "ürün × satıcı × ödeme" tezi, kararın iki adımda verilmesi (önce ürün, sonra satıcı) biçiminde uygulanmalı.
- **S4 Ekosistem:** Ayrı bir kriter olmamalı. Ekosistem uyumu "uygunluk" altında bir alt gösterge olmalı. Kişisel beğeni yalnızca beraberlik bandında karar bozucu olarak kullanılmalı.
- **S5 Çift sayım:** "Tek kanıt, tek kriter" kuralı uygulanmalı:
  - **Uygunluk:** özelliklerin ve kullanım senaryosunun ihtiyaçla eşleşmesi.
  - **Performans:** bağımsız ölçüm, kullanıcının kullanım profiline göre ağırlıklı.
  - **Kalite:** yalnızca zaman içindeki veri (arıza oranı, dayanıklılık testi).

  Bir kanıt yalnızca bir kriterde kullanılabilir.
- **S6 Onarılabilirlik:** 12 puan (fiyat hariç tabloda). Kategoriye göre 5–20 aralığında ayarlanabilir.

## 4. Revize nihai ağırlık oyumuz (TCO = 0, fiyat ayrı aşamada)

| Uygunluk | Ölçülen performans | Kalite/dayanıklılık | Onarım/parça/yazılım/ömür | TCO/fiyat | NL garanti-servis-iade (hukuki koruma) | Satıcı (veto sonrası) | Toplam |
|---|---|---|---|---|---|---|---|
| 28 | 22 | 20 | 12 | **0** (Aşama 3) | 13 | 5 | 100 |

**Yedek tablo (kurul fiyatın toplamın içinde olmasına karar verirse):**

| Uygunluk | Performans | Kalite | Onarım | TCO | NL koruma | Satıcı | Toplam |
|---|---|---|---|---|---|---|---|
| 24 | 19 | 17 | 10 | 15 | 11 | 4 | 100 |

Yedek tabloda TCO puanı şöyle hesaplanır: 15 × (€/yıl_maks − €/yıl) ÷ (€/yıl_maks − €/yıl_min). Maksimum ve minimum değerler, bütçe bandının sınırları olarak aday ürünlere bakmadan önce sabitlenir. Böylece aday kümesi değiştiğinde puanlar değişmez ve sıralama tersinmesi oluşmaz.

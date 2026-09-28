# Kurul 5 (Şeytanın Avukatı) — 2. Tur

**Uygulanabilirlik testi:** Nihai sistem tek sayfaya sığmalı. En fazla **bir** hesap içermeli (ağırlıklı toplam), gerisi evet/hayır listesi olmalı. Bir tüketici bunu mağazada, telefondan, 10 dakikada uygulayabilmeli. 1. tur önerilerinin çoğu bu testi geçemiyor.

## 1. Diğer kurullara en güçlü itirazlar

**K4 (Finans): TCO formülü sahte kesinliğin karesi.** `P + T + N×(E+S+A+B) + R_risk − V_N` formülünde 9 değişken var. Bunların en az 4'ü tahmin: arıza olasılığı × onarım bedeli, 12 yıl sonraki Marktplaats değeri, risk payı, ömür. Bu tahminleri tam sayı gibi toplamak belirsizliği gizler. Ayrıca iki sorun var:
- `18 × (min €/yıl ÷ aday €/yıl)` doğrusal değil. Aday setine tek bir ucuz ürün eklenmesi herkesin puanını değiştirir.
- Ömür (N) hem TCO'da hem dayanıklılıkta sayılıyor. Bu çift sayım.

Kabul ettiğim kısım: enerji ve sarf gerçek bir maliyet. Sadeleştirilmiş hâli: **"fiyat + 5 yıllık enerji ve sarf"**, yalnızca enerji tüketen ve 300 €'nun üstündeki ürünlerde.

**K2 ve K3 (Metodoloji ve Mühendislik): üst üste binen belirsizlik mekanizmaları.** K3'te 5 seviyeli kanıt katsayısı, üstüne `×(0,5+0,5c)` cezası, üstüne 4/10 varsayılan puan, üstüne yeni model için %20–30 indirim var. Aynı belirsizlik dört kez cezalandırılıyor. K2'de de büzülme formülü, Pareto elemesi, Q ≥ 60 eşiği ve ±%20 duyarlılık testi var. Bunlar metodolojik olarak doğru ama tüketici için uygulanamaz. Hiçbir tüketici her hücre için `c·s+(1−c)·5` hesaplamaz. Hesaplasa da c değerini istediği sonuca göre seçer; motivated reasoning bir kat yukarı taşınır.

**K1 (Hukuk): "ürün × satıcı × ödeme" birimi.** Tez ilkede doğru, ama pratikte kombinasyon patlaması yaratır: 4 ürün × 3 satıcı × 2 ödeme = 24 satır. Bunun yerine sıralı bir süreç öneriyorum: **önce ürünü seç, sonra satıcıyı kapı listesiyle seç.**

Ayrıca kurullar arasında bir çelişki var. K2 iDEAL'i "korumalı ödeme" sayıyor, K1 ise iDEAL'de chargeback olmadığını söylüyor. Burada K1 haklı. Nihai metinde bu düzeltilmeli.

## 2. İkna olduğum ve pozisyonumu değiştirdiğim noktalar

- **Fiyat ayrı aşama olmalı (K2).** 1. turda fiyatı 12 puanla toplama katmıştım. Vazgeçiyorum. "Önce kaliteye göre kısa liste yap, sonra bu listede fiyata bak" hem formülsüz hem de insanların doğal düşünme sırasına uygun. Fiyatı puana çevirmek için oran formülü gerekiyor (bkz. K4'e itiraz). Ayrı aşama bu formüle gerek bırakmıyor.
- **Onarılabilirlik 5 puan az (K3, K4).** Yazılım desteği bittiğinde cihaz fiilen ölür. Bu argüman ikna edici.
- **Ekosistem uyumu nesnel bir konu.** "Telefonumla çalışıyor mu?" sorusu uygunluğa ya da kapıya aittir. Ayrı kriterde bıraktığım yalnızca **kişisel tercih ve estetik** olacak.

## 3. S1–S6 oyları

- **S1 Fiyat:** Ayrı aşama. Kalite puanı farkı 5 puandan az olan adaylar arasında en ucuz olan kazanır. Daha pahalı olan ancak ≥10 puan önde ise ve fark bütçeye sığıyorsa seçilir. TCO hesabı yalnızca 300 €'nun üstündeki enerji veya sarf tüketen ürünlerde yapılır.
- **S2 Veri yokluğu:** İki formüle de hayır. Veri yoksa **5 puan ve "kanıtsız" etiketi** verilir. Üç çekirdek kriterin ikisinde kanıt olmayan bir ürün ancak **≥10 puan farkla** kazanabilir. Yoksa kanıtlı ürün seçilir ya da bağımsız test çıkana kadar beklenir (K3'ün bekleme seçeneği).
- **S3 Satıcı:** Vetodan sonra **0 puan**. K1'in "hukuki koruma" rubriği zaten Thuiswinkel Waarborg, Geschillencommissie ve keurmerk'i puanlıyor; ayrı bir satıcı puanı çift sayım olur. Satıcı ürün seçildikten sonra kapı listesiyle seçilir.
- **S4 Ekosistem / kişisel tercih:** Ekosistem uyumu uygunluğun ve kapının içine girer. **Kişisel tercih ayrı ve açık 8 puan** olarak kalır. Görünür olmayan tercih, gizli veto olarak işler.
- **S5 Çift sayım:** Tanımlar şöyle ayrılır: uygunluk = özellik ve senaryo uyumu, performans = bağımsız ölçüm, kalite = zaman içindeki arıza. Buna bir sıralama disiplini eklenir: **uygunluk, inceleme ve yorum okunmadan önce, yalnızca teknik özelliklere bakılarak puanlanır.** Böylece hale etkisi kırılır.
- **S6 Onarılabilirlik:** **10 puan.** 15 puan, sıradan ürünlerde (ör. su ısıtıcısı) aşırı kalır. Kategori ayarını kullanıcıya bırakmak ise sonucu manipüle etmesine kapı açar.

## 4. Revize nihai ağırlık oyu (fiyat ayrı aşama, TCO = 0)

| Kriter | Puan |
|---|---|
| Uygunluk (ekosistem uyumu dahil) | 30 |
| Ölçülen performans | 20 |
| Kalite / dayanıklılık | 20 |
| Onarım / parça / yazılım / ömür | 10 |
| TCO / fiyat | 0 (ayrı aşama) |
| NL garanti–servis–iade (hukuki koruma + satıcı hizmet farkı) | 12 |
| Satıcı (vetodan sonra) | 0 (kapı + hukuki korumada) |
| Kişisel tercih / estetik | 8 |
| **Toplam** | **100** |

Her kriter 1–5 ölçeğinde puanlanır, ağırlıkla çarpılır ve sonuç 5'in katına yuvarlanır. Kategoriye göre ağırlık ayarı yapılacaksa **ürünlere bakmadan önce** ve en fazla ±5 puan olmalı. Rubrikler (K1, K3) formül olarak değil, **puan verirken bakılacak referans** olarak kullanılmalı. 50 €'nun altındaki alımlarda yalnızca kapılar kullanılır. 50–300 € arasında kapılar + üç çekirdek kriter + fiyat yeterlidir. Tam tablo 300 €'nun üstü içindir.

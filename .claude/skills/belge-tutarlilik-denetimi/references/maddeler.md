# 26 Denetim Maddesi

Her madde: **neden önemli** · **kontrol soruları** · **nasıl tespit edilir** · **örnek** · **düzeltme kuralı** · **tipik risk**.

İçindekiler: [01](#madde-01) [02](#madde-02) [03](#madde-03) [04](#madde-04) [05](#madde-05) [06](#madde-06) [07](#madde-07) [08](#madde-08) [09](#madde-09) [10](#madde-10) [11](#madde-11) [12](#madde-12) [13](#madde-13) [14](#madde-14) [15](#madde-15) [16](#madde-16) [17](#madde-17) [18](#madde-18) [19](#madde-19) [20](#madde-20) [21](#madde-21) [22](#madde-22) [23](#madde-23) [24](#madde-24) [25](#madde-25) [26](#madde-26) · [Ağırlıklandırma](#belge-türüne-göre-ağırlıklandırma)

---

## Madde 01
### Tarihsel Tutarlılık · Yüksek risk
Tarih hataları en kolay fark edilen ama en sık gözden kaçan tutarsızlıktır; hukuki geçerliliği, zamanaşımı sürelerini ve sorumluluk zincirini doğrudan etkiler.

- Kronolojik sıra mantıklı mı (başlangıç < bitiş, tebligat < itiraz, imza < yürürlük)?
- Belgenin düzenlenme tarihi, atıf yaptığı olaylardan sonra mı?
- Belirtilen gün adı o takvim tarihine denk geliyor mu?
- Süre ifadeleri ("3 ay", "45 gün") iki tarih arasındaki farkla örtüşüyor mu?
- Gün/ay sırası, saat dilimi ve takvim her yerde aynı mı — "03/04/2025" bir yerde 3 Nisan, başka yerde 4 Mart mı okunuyor?
- Aynı veri bir yerde tek yıl, başka yerde dönem olarak mı veriliyor ("2025 yılı" ↔ "2024–2025 dönemi")?

**Tespit:** Tüm tarihleri kronolojik bir olay tablosuna dök; bağıntıları zamansal kısıt olarak doğrula (bitiş − başlangıç = süre).

**Örnek:** Sözleşme "14.03.2024'te imzalanmıştır" diyor; ekteki fatura 22.06.2024 tarihli olduğu hâlde "işbu sözleşmenin imza tarihinde tanzim edilmiştir" ibaresini taşıyor.

**Düzeltme:** Olaylar bir zaman çizgisine oturtulmalı; fatura tanzim tarihi ile imza tarihi arasındaki illiyet bağı düzeltilmelidir.

---

## Madde 02
### Sayısal ve Matematiksel Tutarlılık · Yüksek risk
Toplam ve alt kalemler arasındaki uyumsuzluk, mali ve istatistiksel raporların denetlenebilirliğini yok eder.

- Alt kalemlerin toplamı genel toplamla kuruşuna kadar eşleşiyor mu?
- Yüzde dağılımları %100'ü buluyor mu?
- Aynı veri farklı yerlerde tekrarlanıyorsa rakamlar birebir aynı mı?
- Ölçü ve para birimleri (TL/USD, kg/adet, net/brüt) tutarlı mı?
- Adet × birim fiyat = toplam tutar mı; başlangıç + artış = sonuç mu?
- "%20 artış" ile "20 puan artış" karıştırılmış mı; yüzde hangi payda üzerinden, pay ve payda aynı evren mi?
- "Milyon/bin" ölçekleri, ondalık/binlik ayraçları ve yuvarlama hassasiyeti metin, tablo ve ekte aynı mı?
- Negatif değerler, eksi işaretleri ve parantezli muhasebe gösterimi doğru okunmuş mu?

**Tespit:** Her toplamın alt kalemlerini ayrı tabloya çıkarıp küçük bir yuvarlama toleransıyla yeniden topla (çapraz toplama).

**Örnek:** Yönetici özeti "toplam 128 çalışan" derken, ek tablodaki departman satırlarının toplamı 121 çıkıyor.

**Düzeltme:** Eksik 7 personelin hangi birimde olduğu eklenmeli ya da genel toplam 121'e revize edilmelidir.

---

## Madde 03
### Referans ve Çapraz Atıf Tutarlılığı · Orta risk
Kırık veya yanlış iç atıflar, okuyucuyu belgede var olmayan ya da alakasız bir hükme yönlendirir.

- "Madde X'te belirtildiği üzere" gibi atıflar gerçek içerikle örtüşüyor mu?
- Ek, tablo, şekil, dipnot referansları var olan bir öğeye işaret ediyor mu?
- Tanımlar bölümündeki terimler metin boyunca aynı anlamda mı kullanılmış?
- Kısaltmalar ilk geçtiği yerde açılmış ve sonrasında tutarlı mı?

**Tespit:** Tüm "Madde X", "Ek Y", "bkz." ifadelerini listeye çıkar; var olan bölüm indeksiyle küme farkını alarak hedefsiz atıfları bul.

**Örnek:** Metin "gecikme cezaları için bkz. Ek-3" diyor; belgede yalnızca Ek-1 ve Ek-2 var.

**Düzeltme:** Ek-3 eklenmeli veya atıf doğru ek numarasıyla güncellenmelidir.

---

## Madde 04
### Taraf ve Varlık Tutarlılığı · Yüksek risk
Taraf kimliğindeki belirsizlik, belgenin hangi tüzel veya gerçek kişiyi bağladığını tartışmalı hâle getirir.

- Kişi/kurum adlarının ticari unvan yazımı birebir aynı mı?
- Taraf tanımları ("Alıcı", "Yüklenici", "İdare") tutarlı kullanılmış mı?
- Vergi no, MERSİS, TC kimlik, tebligat adresi her geçtiği yerde aynı mı?
- Unvan ve sıfatlar çelişiyor mu?

**Tespit:** Varlık tanıma (NER) ile tüm isim varyasyonlarını listele; unvan, sicil ve adres farklarını eşleştirme matrisinde karşılaştır.

**Örnek:** Başta "ABC İletişim ve Ticaret Ltd. Şti." tanımlanan taraf, Madde 8'de "ABC A.Ş." olarak anılıyor — iştirak mi, unvan değişikliği mi, farklı şirket mi belirsiz.

**Düzeltme:** İlk maddedeki tanımlı kısaltma metnin tamamında kullanılmalıdır.

---

## Madde 05
### Mantıksal ve Anlamsal Tutarlılık · Yüksek risk
Birbirini tekzip eden hükümler, hangi kuralın uygulanacağını imkânsız kılar.

- Doğrudan birbirini yalanlayan iki ifade var mı?
- Şart ile sonuç arasındaki bağ tutarlı mı?
- Özet/giriş, detay ve sonuç bölümleriyle aynı karara mı varıyor?
- İş adımlarında döngüsel önkoşul (tavuk-yumurta kilitlenmesi) var mı?

**Tespit:** İddiaları tek cümlelik önermelere indir; çelişen önerme çiftlerini ve döngüsel bağımlılıkları bir bağımlılık grafiğinde (çevrim tespiti) ara.

**Örnek:** Raporun girişi "talebin reddine karar verilmiştir" derken hüküm bölümü "talebin kısmen kabulü ile 50.000 TL ödenmesine" diye bitiyor.

**Düzeltme:** Karar tek yönde netleştirilmelidir.

---

## Madde 06
### Sınıflandırma ve Gruplandırma Tutarlılığı · Orta risk
Aynı kritere göre kategorize edilmeyen veriler, karşılaştırma ve toplulaştırmaları anlamsız kılar.

- Aynı sınıflandırma ölçütü belge boyunca değişmeden uygulanmış mı?
- Bir öğe çelişen iki kategoriye birden atanmış mı?
- Üst-alt kategori (parent-child) ilişkisi korunmuş mu?
- Kategoriler tüm evreni kapsıyor mu — hiçbir gruba girmeyen öğe var mı?
- Aynı öğe birden fazla grupta sayılarak toplamı şişiriyor mu (çift sayım)?
- Kategori ile kategori örneği, bütün-parça ile tür-alt tür ilişkisi karıştırılmış mı?

**Tespit:** Her öğeyi kategorisiyle tabloya dök; aynı öğenin farklı yerde farklı kategoriye düşüp düşmediğini küme karşılaştırmasıyla kontrol et.

**Örnek:** Yazılım lisans bedeli girişte "operasyonel gider (OPEX)", mali analiz tablosunda "yatırım harcaması (CAPEX)" olarak sınıflandırılıyor.

**Düzeltme:** Muhasebe standardına göre doğru sınıf teyit edilip metin genelinde tekleştirilmelidir.

---

## Madde 07
### Format ve Yazım Tutarlılığı · Düşük risk
Format karışıklığı, özellikle tarih ve para biriminde, yanlış okumaya zemin hazırlar.

- Tarih formatı sabit mi (GG.AA.YYYY ↔ AA.GG.YYYY karışıklığı)?
- Ondalık ve binlik ayracı standart mı?
- Madde/fıkra/bent numaralandırma hiyerarşisi tutarlı mı?

**Tespit:** Aynı veri türünün tüm örneklerini yan yana dizip düzenli ifadelerle format varyansını tara.

**Örnek:** İlk yarıda "04.05.2024", ikinci yarıda "05/04/2024" — 4 Mayıs mı 5 Nisan mı belirsizleşiyor.

**Düzeltme:** Tek format standardı belirlenip tüm tarihler dönüştürülmelidir.

---

## Madde 08
### Görsel-Metin Tutarlılığı · Orta risk
Grafik ile anlatı arasındaki uyumsuzluk, karar alıcıyı yanlış sonuca götürür.

- Tablo/grafik verileri metindeki sayılarla örtüşüyor mu?
- Şekil/tablo başlıkları ve eksen etiketleri açıklamalarla uyumlu mu?
- Görsele yapılan atıf doğru trendi mi tarif ediyor?

**Tespit:** Tablo/grafik verilerini yapısal forma aktarıp metindeki her sayısal iddiayla teker teker eşleştir (tie-out).

**Örnek:** Metin "üçüncü çeyrekte pazar payı %15 arttı" diyor; grafikte ilgili çeyrek sütunu aşağı yönlü.

**Düzeltme:** Kaynak veri ile metin mutabık hale getirilmeli, yön göstergesi düzeltilmelidir.

---

## Madde 09
### Hak ve Yükümlülük Tutarlılığı · Yüksek risk
Çelişen hak ve borçlar sözleşmenin icrasını kilitler; temerrüt ve tazminat uyuşmazlığı doğurur.

- Bir maddede tanınan hak, başka maddede zımnen iptal ediliyor mu?
- Zorunluluk bildiren ifadeler ile takdire bırakanlar çakışıyor mu?
- Fesih, bildirim süresi, cezai şart ve teminat koşulları uyumlu mu?
- Yetki ve sorumluluk dağılımı tekil ve net mi?
- Bir bölümde öneri olan husus ("önerilir", "yapılabilir") başka bölümde zorunluluğa mı dönüşmüş?

**Tespit:** Her tarafa yüklenen fiilleri ZORUNLU / SERBEST / YASAK olarak etiketle; birbirini geçersiz kılan hüküm çiftlerini ara.

**Örnek:** Madde 5 "taraflar 30 gün önceden bildirimle tek taraflı feshedebilir" derken Madde 14 "3 yıllık süre dolmadan hiçbir surette feshedilemez" diyor.

**Düzeltme:** İstisna ilişkisi açıkça kurulmalı ("Madde 14 hükümleri saklı kalmak kaydıyla…").

---

## Madde 10
### Versiyon ve Revizyon Tutarlılığı · Orta risk
Revizyon geçmişiyle uyumsuz içerik, hangi sürümün yürürlükte olduğunda hukuki şüphe yaratır.

- "Son güncelleme" tarihi en güncel değişiklikle uyumlu mu?
- Revizyon tablosunda "değiştirildi" denilen bölümler metne yansımış mı?
- Sabit kalması gereken temel tanımlar yetkisizce değişmiş mi?

**Tespit:** Revizyon tablosundaki her kaydı ilgili bölümle metinsel karşılaştırmaya (diff) sok.

**Örnek:** "v2.1 — Ek-B fiyat listesi güncellendi" yazıyor; Ek-B fiyatları v1.0 ile birebir aynı.

**Düzeltme:** Ya liste güncellenmeli ya revizyon açıklaması düzeltilmelidir.

---

## Madde 11
### Dilbilimsel ve Üslup Tutarlılığı · Düşük risk
Zaman kipi, anlatıcı kişisi ve resmiyet düzeyindeki ani savrulmalar, belgenin farklı taslaklardan birleştirildiğinin işaretidir.

- Fiil kipleri bağlamsal olarak tutarlı mı?
- Anlatım kişisi (biz / şirketimiz / taraflar) sabit mi?
- Resmiyet düzeyi homojen mi?

**Tespit:** Zamir ve fiil çekimlerini izleyerek kaymanın başladığı cümleyi işaretle — genellikle bölüm sınırlarında olur.

**Örnek:** İlk dört bölüm "Taraflar mutabakata varmışlardır" biçiminde; beşinci bölüm "biz bu kararı verirken maliyetleri düşürmeyi hedefledik" diyor.

**Düzeltme:** Anlatım tek bir resmi kişiye dönüştürülmelidir.

---

## Madde 12
### Dış Kaynak ve Mevzuat Atıf Tutarlılığı · Yüksek risk · Katman 3
Mülga, yanlış veya hatalı fıkra atıfları belgenin hukuki zeminini ortadan kaldırabilir.

- Atıf yapılan kanun/yönetmelik/tebliğ güncel ve yürürlükte mi?
- Alıntılanan hüküm orijinal metinle birebir örtüşüyor mu?
- Aynı kaynağa farklı yerlerde farklı madde numarasıyla mı atıf yapılmış?

**Tespit:** Dış atıfları listeye çıkarıp yürürlük ve alıntı doğruluğunu orijinal kaynağa karşı teyit et. Erişim yoksa `DIŞ DOĞRULAMA GEREKLİ` etiketiyle bırak.

**Örnek:** Madde 4'te "6698 sayılı Kanun m.11 uyarınca" denirken, aynı hak için Madde 19'da "8. maddesi kapsamındaki haklar" deniyor.

**Düzeltme:** Doğru madde numarası belge genelinde tekleştirilmelidir.

---

## Madde 13
### Meta-veri ve Kapak Bilgisi Tutarlılığı · Düşük risk
Kapak, üstbilgi/altbilgi ve dosya adının gövdeyle çelişmesi evrak kaydı ve arşivlemede karışıklık yaratır.

- Kapaktaki başlık, tarih, proje adı ve taraflar gövdeyle aynı mı?
- Üstbilgi/altbilgideki doküman kodu ve revizyon no her sayfada tutarlı mı?
- Dosya adı/sürüm etiketi belge içindeki sürümle örtüşüyor mu?

**Tespit:** Kapak ve alt/üstbilgi alanlarını gövdedeki ilk geçiş noktalarıyla yan yana karşılaştır.

**Örnek:** Kapakta "Revizyon No: 4 — 15.08.2025", altbilgilerde "REV-02 / 10.01.2025".

**Düzeltme:** Şablon altbilgisi kapak verisiyle senkronize edilmelidir.

---

## Madde 14
### İmza, Onay ve Yetki Tutarlılığı · Yüksek risk
İmzalayanın unvanı metinle çelişiyorsa belgenin bağlayıcılığı yetkisiz temsil tartışmasına açılır.

- İmza bloğundaki isim/unvan, metinde yetkili olarak anılan kişiyle aynı mı?
- Çift imza / kurul kararı şartı karşılanmış mı?
- Vekâleten imzalarda vekâletname tarihi ve yetki kapsamı belirtilmiş mi?

**Tespit:** İmza bloklarını çıkarıp metindeki temsil ve yetki hükümleriyle yetki matrisinde eşleştir.

**Örnek:** Metinde yetkilinin "Yönetim Kurulu Başkanı" olduğu yazılı; belgeyi "Genel Müdür Yardımcısı" tek başına imzalamış.

**Düzeltme:** İmza bloğu yenilenmeli veya geçerli yetkilendirme metni eklenmelidir.

---

## Madde 15
### İstatistiksel ve Ortalama Tutarlılığı · Orta risk
Türetilmiş göstergeler ham veriyle uyuşmuyorsa okuyucu yanlış büyüklük algısına kapılır.

- Beyan edilen ortalama veri setinden doğrulanabiliyor mu?
- Min-maks aralığı tüm değerleri kapsıyor mu?
- Büyüme/azalış oranı başlangıç ve bitiş değerleriyle tutarlı mı?

**Tespit:** Her türetilmiş istatistiği ham veriden yeniden hesaplayıp beyanla karşılaştır; farkı sayısal yaz.

**Örnek:** "Ortalama yanıt süresi 45 saniye" deniyor; ekteki 7 günlük verinin ortalaması 68 saniye.

**Düzeltme:** Ortalama güncellenmeli veya hangi filtrelenmiş veriye dayandığı dipnotta açıklanmalıdır.

---

## Madde 16
### Eksiklik ve Boşluk Denetimi · Yüksek risk · Katman 2
Belgede *olmayan* şey, olandan tehlikelidir: doldurulmamış bir tutar veya boş imza satırı en sık atlanan kusurdur, çünkü karşılaştırılacak ikinci bir pasaj yoktur.

- Şablondan kalan doldurulmamış alanlar var mı ("………", "XX", "[•]", boş parantez, TBD)?
- Belge türü için zorunlu unsurlar tam mı (taraf, konu, bedel, süre, tarih, imza)?
- "Aşağıda belirtilen şartlar" denip liste verilmemiş mi?
- Atıf yapılan ek/form fiilen mevcut mu?

**Tespit:** Belge türü için zorunlu unsurlar listesini önceden çıkarıp var/yok işaretle; doldurulmamış alan desenlerini düzenli ifadeyle tara.

**Örnek:** Bedel maddesinde "toplam bedel ……… TL'dir" boş bırakılmış; ödeme planı "bedelin %30'u peşin" diyerek var olmayan bir tutara atıf yapıyor.

**Düzeltme:** Boş alan doldurulmalı veya bedelin hangi ekte belirlendiği açık atıfla gösterilmelidir.

---

## Madde 17
### Şablon Kalıntısı ve Kopya Artığı · Yüksek risk
Önceki bir belgeden kopyalanan metinde başka bir işin taraf adı veya yetkili mahkemesi geride kalır. En tehlikeli çelişkilerdir: dil bilgisi kusursuz göründüğü için okurken sırıtmazlar.

- Tanımlanan taraflar dışında bir kurum/kişi adı geçiyor mu?
- Yetkili mahkeme/tahkim, uygulanacak hukuk, para birimi maddesi bağlama uygun mu?
- Başka sözleşme türüne ait madde başlıkları kalmış mı?
- Konu/hizmet tanımı bir maddede farklı mı?

**Tespit:** Varlık tablosundaki tüm adları tanımlar bölümündeki taraf kümesiyle karşılaştır; kümeye ait olmayan her ad kalıntı adayıdır.

**Örnek:** Hizmet sözleşmesinin gizlilik maddesinde taraflar arasında hiç geçmeyen "DEF Lojistik A.Ş." adı yer alıyor.

**Düzeltme:** Kalıntı ad değiştirilmeli ve o madde bütünüyle yeniden okunmalıdır — kalıntı genelde tek kelime değil, tüm paragraftır.

---

## Madde 18
### Koşul Kapsama ve Eşik Tutarlılığı · Yüksek risk
Açıkta kalan veya çakışan aralıklar hangi kuralın işleyeceğini belirsiz bırakır; eşikteki bir birimlik kayma para veya hak kaybı doğurur.

- Koşul dalları tüm olasılıkları kapsıyor mu (tam eşik değeri boşta mı)?
- Aralıklar çakışıyor mu (0–50 ve 50–100 gibi)?
- Kapanış dalı ("aksi hâlde") tanımlı mı?
- Eşikler belge boyunca aynı mı (bir yerde 30 gün, başka yerde 1 ay)?
- Sınır dili doğru mu — "18 yaşından küçük" ile "18 yaş ve altı", "dâhil" ile "hariç" aynı sayılmış mı?

**Tespit:** Şartlı hükümleri koşul → sonuç karar tablosuna dök; aralıkların birleşimi tüm tanım kümesini kapsıyor mu, kesişimleri boş mu kontrol et.

**Örnek:** "Gecikme 30 günden az ise günlük %0,1; 30 günden fazla ise %0,3" — tam 30 gün hiçbir dala girmiyor.

**Düzeltme:** Eşikler kapsayıcı yazılmalı ("30 gün ve altında" / "30 günden fazla").

---

## Madde 19
### Belirsiz ve Ölçülemez Terim Denetimi · Orta risk · Katman 2
"Makul süre", "derhal" tek başına çelişki değildir; ama aynı yükümlülük için hem sayısal hem belirsiz süre varsa hangisinin geçerli olduğu tartışmaya açılır.

- Ölçülemez ifadeler (makul, derhal, uygun, en kısa sürede) sayısal karşılıkla tanımlanmış mı?
- Aynı yükümlülük için hem sayısal hem belirsiz süre mi kullanılmış?
- Kalite ölçütleri (yeterli, tatmin edici) ölçülebilir kritere bağlanmış mı?
- "ve/veya": koşulların hepsi mi, biri mi, herhangi bir bileşimi mi gerekiyor?
- "-abilir" eki izin mi ("yapabilir" = serbesttir) yoksa olasılık mı bildiriyor?
- Zincirleme tamlamada bağlanma belirsiz mi ("şirketin yetkili temsilcisinin onayı")?
- Listelerde gruplama belirsiz mi ("A ve B ile C" → (A ve B) ile C mi)?

**Tespit:** Belirsiz terim sözlüğüyle tara; her bulgunun yanına aynı konuda sayısal hüküm olup olmadığını not et — ikisinin birlikte olduğu yerler çelişki adayıdır.

**Örnek:** Madde 6 "arıza bildirimi derhal yapılır" derken Madde 12 "en geç 5 iş günü içinde" diyor.

**Düzeltme:** Tek ölçülebilir süre benimsenmeli; "derhal" kullanılacaksa tanımlar bölümünde sayısallaştırılmalıdır.

---

## Madde 20
### Çok Dillilik ve Çeviri Tutarlılığı · Yüksek risk
Çeviri kayması, tarafların farklı yükümlülük anladığı iki ayrı sözleşme yaratır.

- Hangi dildeki metnin esas olduğu (asıl metin kaydı) belirtilmiş mi?
- Sayılar, tarihler, süreler ve tutarlar iki dilde birebir aynı mı?
- Hukuki terimler karşılık dilde aynı anlamı taşıyor mu (fesih / termination / rescission)?
- Madde numaralandırması iki dilde örtüşüyor mu?
- Çeviride kip değişmiş mi ("may be used" → "kullanılmalıdır"); olumsuzluk veya istisna kaybolmuş mu?

**Tespit:** İki metni madde madde hizala; önce sayısal değerleri ve tarihleri, sonra yükümlülük fiillerini karşılaştır.

**Örnek:** Türkçe "30 gün içinde teslim eder", İngilizce "within 30 business days" — takvim/iş günü farkı teslimi haftalarca kaydırıyor.

**Düzeltme:** Sapma giderilmeli ve uyuşmazlıkta hangi metnin esas alınacağı ayrı maddeyle belirlenmelidir.

---

## Madde 21
### Para Birimi, Vergi ve Kur Tutarlılığı · Yüksek risk
Aynı tutarın bir yerde KDV dahil, başka yerde hariç yazılması ödeme uyuşmazlıklarının en sık kaynağıdır.

- Tutarlar KDV dahil mi hariç mi, tutarlı belirtilmiş mi?
- Yabancı para varsa hangi kurun hangi tarihte esas alınacağı tanımlı mı?
- Endeksleme/artış formülü hangi döneme ve veri kaynağına bağlı, yazılmış mı?
- Rakamla ve yazıyla yazılan tutarlar aynı mı?

**Tespit:** Tüm parasal ifadeleri birim, vergi durumu, kur kaydı ve tarihle tek tabloya çıkar; aynı kalemin satırlarını karşılaştır.

**Örnek:** Bedel maddesi "120.000 TL (KDV hariç)", ödeme planı toplamı "120.000 TL (KDV dahil)".

**Düzeltme:** Tüm tutarlar tek vergi esasına göre yazılmalı; KDV'nin ayrıca eklenip eklenmeyeceği tek cümlede netleştirilmelidir.

---

## Madde 22
### Nicelik Belirteçleri ve Kapsam Evreni · Yüksek risk · Katman 2
"Tümü", "bazı", "yalnızca" bir hükmün hangi evrene uygulandığını belirler. Aynı hüküm iki bölümde farklı evrene uygulanıyorsa en zor fark edilen çelişki çıkar: cümleler tek tek doğrudur, birlikte değildir.

- "Tümü / bazı / yalnızca / en az biri / hiçbiri / ve-veya" mantıksal olarak uyumlu mu?
- Aynı hüküm farklı bölümlerde farklı kişi grubuna, birime, coğrafyaya veya döneme mi uygulanıyor?
- Bir hükmün kapsamı sonraki cümlelerde sessizce daraltılmış/genişletilmiş mi?
- "Yalnızca A ve B grupları" denip ileride C grubu kapsama alınmış mı?

**Tespit:** Her hüküm için "hangi evren" sütununu ayrı çıkar (kişi grubu, birim, coğrafya, dönem, sürüm) ve aynı konudaki hükümleri bu sütuna göre karşılaştır — çelişki çoğu zaman hükümde değil evrenlerin farkındadır.

**Örnek:** Madde 3 "tüm personel yıllık eğitime katılır" derken Ek-2 tablosu yalnızca merkez personelini listeliyor.

**Düzeltme:** Hükmün evreni tanımlar bölümünde tek yerde tanımlanmalı, tüm bölümler ona atıf yapmalıdır.

---

## Madde 23
### İddia–Kanıt ve Gerekçe–Sonuç Bağlantısı · Yüksek risk · Katman 3
Bir belgenin en kırılgan yeri, verinin desteklediğinden daha güçlü sonuç çıkarılan cümledir. Bu yazım hatası değil, karar hatasıdır.

- Her önemli sonuç önündeki veriyle gerçekten destekleniyor mu?
- Veriler yalnızca birliktelik gösterirken metin nedensellik mi kuruyor?
- Atıf yapılan kaynak iddianın tamamını mı, bir kısmını mı destekliyor?
- Alıntının istisna içeren devamı kesilmiş, bağlamından koparılmış mı?
- Önerilen karar tanımlanan problemden mantıksal olarak çıkıyor mu?

**Tespit:** Her sonucu "iddia → dayanak → dayanağın gücü" üçlüsüne ayır. Dayanak yoksa `BELGEDE BELİRTİLMİYOR`, zayıfsa `DIŞ DOĞRULAMA GEREKLİ` — ikisi de çelişki değildir.

**Örnek:** "Müşteri memnuniyeti eğitim programı sayesinde arttı" deniyor; veri yalnızca aynı dönemde iki değerin birlikte yükseldiğini gösteriyor.

**Düzeltme:** Cümle veriye indirgenmeli ya da nedenselliği taşıyacak karşılaştırma verisi eklenmelidir.

---

## Madde 24
### İzlenebilirlik: Amaç → Gereksinim → Ölçüt → Kanıt · Orta risk · Katman 2
Hiçbir maddeyle ilişkilendirilmemiş bir hedef çelişki üretmez, denetlenemezlik üretir.

- Her amaç en az bir gereksinim/maddeyle ilişkili mi?
- Her gereksinim ölçülebilir kabul kriterine bağlı mı?
- Her kriter için kanıtı kim, ne zaman, hangi yöntemle üretecek belli mi?
- Hiçbir amaca hizmet etmeyen "yetim" madde var mı?

**Tespit:** Amaç · madde · ölçüt · kanıt sütunlu izlenebilirlik matrisi kur; boş her hücre bir eksikliktir.

**Örnek:** Giriş "işlem süresinin kısaltılması" hedefini koyuyor; hiçbir maddede süreye ilişkin ölçüt, hedef değer veya ölçüm yöntemi yok.

**Düzeltme:** Ölçülebilir kriter (ör. "ortalama işlem süresi ≤ 5 iş günü"), yöntem ve sorumlu eklenmeli; ya da hedef kapsam dışı sayılıp çıkarılmalıdır.

---

## Madde 25
### Durum Geçişleri ve Kenar Durumları · Orta risk · Katman 2
Süreçler genellikle yalnızca "her şey yolunda gittiğinde" anlatılır; ret, iptal, gecikme ve tekrar hâlleri tanımsız kalır. Uygulamadaki tıkanmaların çoğu burada doğar.

- Durumlar (taslak, onayda, onaylandı, yürürlükte, iptal) doğru sırada mı; geri dönüş tanımlı mı?
- İptal edilmiş veya süresi dolmuş belge hâlâ yürürlükteymiş gibi kullanılıyor mu?
- Sıfır, boş liste, tek öğe ve azami değer durumları ele alınmış mı?
- Gecikme, itiraz, tekrar başvuru ve hata hâllerinde ne olacağı yazılmış mı?

**Tespit:** Süreci durum → olay → yeni durum tablosuna dök; hedefi olmayan olay veya çıkışı olmayan durum bir kenar durumu boşluğudur.

**Örnek:** Akış "başvuru → inceleme → onay" olarak tanımlı; reddedilen başvurunun düzeltilip yeniden sunulup sunulamayacağı hiçbir maddede yok.

**Düzeltme:** Ret ve yeniden başvuru dalı eklenmeli; her durum için çıkış yolu, sorumlu ve süre tanımlanmalıdır.

---

## Madde 26
### Belge Mimarisi ve Özet–Gövde Uyumu · Orta risk
Yönetici özeti çoğu zaman tek okunan bölümdür. Kritik bir kısıt yalnızca eklerde duruyorsa belge teknik olarak doğru, pratikte yanıltıcıdır.

- Özetteki sonuçlar gövde ve eklerle aynı yönde mi?
- Gövdede/eklerde bulunan kritik kısıt özette hiç geçmiyor mu?
- Başlıklar bölüm içeriğiyle örtüşüyor, içindekiler gerçek yapıyı yansıtıyor mu?
- Sonuç bölümü girişte kurulan soruyu cevaplıyor mu?

**Tespit:** Özet, gövde ve ekleri ayrı iddia listesi olarak çıkarıp üç listeyi karşılaştır; yalnızca tek listede görünen kritik iddia bir mimari uyumsuzluktur.

**Örnek:** Yönetici özeti projeyi koşulsuz öneriyor; Ek-4'teki "yalnızca bütçenin %30 artması hâlinde uygulanabilir" kaydı özette geçmiyor.

**Düzeltme:** Kısıt özete taşınmalı veya öneri, ekteki koşula açık atıf yapacak biçimde yeniden yazılmalıdır.

---

## Belge Türüne Göre Ağırlıklandırma

Süre kısıtlıysa önce öncelikli maddelere odaklan.

| Doküman türü | Öncelikli | İkincil |
|---|---|---|
| Hukuki sözleşme & protokol | 01, 04, 09, 14, 17, 18, 21, 22 | 03, 05, 10, 12, 16, 19, 25 |
| Finansal / faaliyet raporu | 02, 06, 08, 15, 16, 21, 23 | 01, 05, 07, 10, 13, 22, 26 |
| Teknik şartname | 05, 16, 18, 19, 24, 25 | 01, 02, 03, 07, 09, 22 |
| Resmi yazışma / idari karar | 12, 14, 04, 01, 16, 22 | 03, 11, 13, 17, 25 |
| Politika / strateji belgesi | 24, 23, 19, 22, 26 | 01, 06, 09, 15, 16 |
| Çok dilli / sınır ötesi sözleşme | 20, 04, 09, 21, 12 | 01, 07, 18, 19, 22 |

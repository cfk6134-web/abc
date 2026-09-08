---
name: urun-arastir
description: Kullanıcı bu projede bir ürün/marka/model adı yazdığında (ör. "Dyson V15 Detect", "iPhone 16 Pro 256GB", "Bosch SMS4H..." gibi bir soru ya da komut olmayan, kabaca bir satın alma niyeti taşıyan kısa mesaj) veya açıkça /urun-arastir yazdığında tetiklenir. Hollanda → Avrupa → Dünya sırasıyla fiyat, güvenilirlik/yorum, gümrük-vergi ve alternatif ürün araştırması yapıp EUR bazlı, Türkçe bir karşılaştırma raporu (HTML Artifact) üretir.
---

Bu skill, çok pazarlı bir ürün satın alma araştırması yürütür. Aşağıdaki adımları sırayla uygula.

## 0. Ürünü ve gereksinimleri belirle

Kullanıcının mesajından araştırılacak ürünü çıkar (marka + model + varsa spesifik varyant).

- Ürün yeterince spesifikse (marka/model belli) **doğrudan devam et**, ekstra soru sorma —
  bu skill'in bütün amacı sadece ürün adını yazınca sistemin harekete geçmesidir.
- Ürün çok belirsizse (sadece "laptop", "telefon", "kulaklık" gibi kategori adı, marka/model
  yok) `AskUserQuestion` ile **tek bir** soru sor: bütçe aralığı ve en önemli öncelik
  (fiyat / performans / marka güveni). Cevabı alınca devam et.
- Kullanıcı bütçe/özel gereksinim belirtmişse (ör. "600 euro altı", "16GB RAM olsun") bunu
  not al, tüm subagent'lara ileteceğin görev metnine dahil et.

## 0.5. Kriter bazlı ürün seçimi (gerekirse)

Kullanıcı somut bir marka/model değil, bir **seçim kriteri** verdiyse (ör. "en yüksek
besin değerine sahip peynir", "en dayanıklı akıllı saat", "en sessiz bulaşık makinesi")
subagent'ları başlatmadan önce bu kriteri tek bir somut ürüne indirger:

- Kriter birden fazla makul yorumla açılabiliyorsa (ör. "besin değeri" protein mi,
  genel yoğunluk mu?) `AskUserQuestion` ile **tek bir** netleştirme sorusu sor.
- Netleştikten sonra kendi bilgin + gerekirse kısa bir web araştırmasıyla kriteri en
  iyi karşılayan somut ürünü/markayı belirle ve bunu gerekçesiyle (hangi verilere göre
  seçildi) tek paragrafta not al — bu paragraf rapora "Varsayımlar" bölümünde girecek.
- Bu adım sadece kriter belirsizliği varsa çalışır; kullanıcı zaten spesifik bir
  marka/model verdiyse atla.

## 1. Araştırmayı paralel başlat

Kur/veri tutarlılığı için: Dünya pazarı EUR dışı bir para birimi gerektiriyorsa
(USD/GBP/vb.) **önce sen tek bir güncel kur ve tarih belirle**, sonra bunu ilgili
`market-scout` (Dünya) ve `import-advisor` çağrılarının prompt'una aynen yaz — her
subagent'ın kendi kurunu bulmasına izin verme, tutarsız rakamlara yol açar.

Tek bir mesajda, aşağıdaki 5 Agent çağrısını **paralel** (arka planda) başlat:

1. `market-scout` — scope: **Hollanda** (bol.com, Coolblue, MediaMarkt.nl, Amazon.nl vb.)
2. `market-scout` — scope: **Avrupa (Hollanda hariç)**
3. `market-scout` — scope: **Dünya (AB dışı)**
4. `reliability-analyst` — ürünün güvenilirliği/yorumları
5. `alternatives-scout` — alternatif/muadil ürünler

Her çağrının prompt'una ürün adını, varsa bütçe/gereksinim notunu ve tam olarak hangi
pazar kapsamına baktığını yaz. Beşi de bağımsızdır, aynı anda çalışabilirler — hızlı olması
için hepsini tek mesajda fan-out et, sonuçları bekle.

**Hata durumunda:** bir subagent API hatası/rate-limit yüzünden başarısız olursa (ör.
"session limit", 429), kullanıcıya hemen "tamamen başarısız oldu" deme — **aynı görevle
bir kez daha başlat** ve sonucunu bekle. İkinci denemede de aynı subagent başarısız
olursa, o pazar/bölüm için "bu veri alınamadı, tekrar denenebilir" notuyla devam et,
diğer subagent'ların sonuçlarıyla raporu yine de tamamla — tek bir subagent'ın hatası
tüm araştırmayı durdurmasın.

## 2. İthalat maliyetini hesapla (bağımlı adım)

`market-scout` (Dünya) sonucu geldiğinde, onun bulduğu fiyat listesini `import-advisor`
subagent'ına gönder (bu adım öncekilere bağımlı olduğu için diğerleri bittikten/geldikten
sonra ayrıca çağrılır). Sonucunu bekle.

## 3. Sentezle ve raporu yaz

Tüm sonuçlar elindeyken:

- Tüm fiyatları **EUR** bazına göre karşılaştır (her subagent zaten EUR tahmini döndürür;
  tutarsızlık varsa tek bir kur/tarih varsayımında birleştir ve raporda belirt).
- Üç pazardaki (NL / AB / Dünya) en iyi seçenekleri karşılaştıran özet bir tablo çıkar
  (toplam gerçek maliyet — Dünya için gümrük+BTW+kargo dahil).
- Güvenilirlik ve alternatif ürün bulgularını ilgili bölümlere yerleştir — `alternatives-scout`'un
  ürettiği sayısal değer/besin/teknik özellik tablosunu ve puanlama tablosunu (kazanan işaretli)
  olduğu gibi rapora taşı, özetleyip atlama.
- Net bir **nihai tavsiye** oluştur: hangi pazardan, hangi satıcıdan, ne fiyata almalı ve
  neden — tek paragrafta gerekçelendir. Belirsizlik varsa (ör. hız mı ucuzluk mu öncelikli)
  iki seçenekli tavsiye ver ("en hızlı/güvenli seçenek X, en ucuz seçenek Y").

## 4. Raporu Artifact olarak yayınla

Yayınlamadan önce **artifact-design** skill'ini yükle (ve karşılaştırma tabloları/fiyat
görselleştirmesi için **dataviz** skill'ini de yükle). Rapor şu bölümleri sabit sırayla
içermeli:

1. Başlık + tek paragraflık nihai tavsiye özeti (en üstte, göze çarpan bir kutuda)
2. Varsayımlar (kullanılan kur/tarih, kullanıcı bütçe/gereksinim notu, araştırma tarihi,
   varsa 0.5. adımdaki kriter bazlı ürün seçimi gerekçesi)
3. Hollanda Pazarı
4. Avrupa Pazarı
5. Dünya Pazarı + İthalat Maliyeti
6. Güvenilirlik & Kullanıcı Yorumları
7. Alternatif Ürünler — hem tanıtım tablosu, hem **sayısal değer/besin/teknik özellik
   tablosu**, hem de **puanlama tablosu** (her ürün 0-10 puanlanmış, en yüksek puanlı
   ürün "🏆 Kazanan" olarak açıkça işaretli, metodoloji tek cümlede belirtilmiş)
8. Genel Karşılaştırma Tablosu & Sonuç
9. Kaynaklar
10. Uyarı: "Fiyatlar araştırma anındaki taramaya dayanır, satın almadan önce güncel fiyatı
    doğrulayın."

Rapor dili Türkçe, tüm fiyatlar EUR (yerel fiyat parantezde). Artifact başlığı ürün adı
olsun (jenerik "Rapor" değil).

## 5. Kısa sözlü özet

Artifact'i yayınladıktan sonra kullanıcıya 2-3 cümlelik bir sözlü özet ver: nihai tavsiye
ve en dikkat çekici bulgu (ör. büyük fiyat farkı, güvenilirlik uyarısı). Raporun tamamını
sohbette tekrar etme, Artifact zaten linkli.

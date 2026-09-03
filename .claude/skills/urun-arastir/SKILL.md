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

## 1. Araştırmayı paralel başlat

Tek bir mesajda, aşağıdaki 5 Agent çağrısını **paralel** (arka planda) başlat:

1. `market-scout` — scope: **Hollanda** (bol.com, Coolblue, MediaMarkt.nl, Amazon.nl vb.)
2. `market-scout` — scope: **Avrupa (Hollanda hariç)**
3. `market-scout` — scope: **Dünya (AB dışı)**
4. `reliability-analyst` — ürünün güvenilirliği/yorumları
5. `alternatives-scout` — alternatif/muadil ürünler

Her çağrının prompt'una ürün adını, varsa bütçe/gereksinim notunu ve tam olarak hangi
pazar kapsamına baktığını yaz. Beşi de bağımsızdır, aynı anda çalışabilirler — hızlı olması
için hepsini tek mesajda fan-out et, sonuçları bekle.

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
- Güvenilirlik ve alternatif ürün bulgularını ilgili bölümlere yerleştir.
- Net bir **nihai tavsiye** oluştur: hangi pazardan, hangi satıcıdan, ne fiyata almalı ve
  neden — tek paragrafta gerekçelendir. Belirsizlik varsa (ör. hız mı ucuzluk mu öncelikli)
  iki seçenekli tavsiye ver ("en hızlı/güvenli seçenek X, en ucuz seçenek Y").

## 4. Raporu Artifact olarak yayınla

Yayınlamadan önce **artifact-design** skill'ini yükle (ve karşılaştırma tabloları/fiyat
görselleştirmesi için **dataviz** skill'ini de yükle). Rapor şu bölümleri sabit sırayla
içermeli:

1. Başlık + tek paragraflık nihai tavsiye özeti (en üstte, göze çarpan bir kutuda)
2. Varsayımlar (kullanılan kur/tarih, kullanıcı bütçe/gereksinim notu, araştırma tarihi)
3. Hollanda Pazarı
4. Avrupa Pazarı
5. Dünya Pazarı + İthalat Maliyeti
6. Güvenilirlik & Kullanıcı Yorumları
7. Alternatif Ürünler
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

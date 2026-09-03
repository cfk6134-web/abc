# Ürün Araştırma Sistemi

Bu proje, bir ürün satın alma kararı öncesinde **derin, çok pazarlı piyasa araştırması**
yapıp Türkçe, EUR bazlı, görsel bir rapor üreten bir sistemdir. Odak: önce **Hollanda**,
sonra **Avrupa**, sonra **Dünya** geneli — bu sıra sabittir ve değiştirilmez.

## Nasıl çalışır

Kullanıcı bu projede sohbete sadece araştırmak istediği ürünü/modeli yazar
(ör. "Dyson V15 Detect", "iPhone 16 Pro 256GB", "Bosch bulaşık makinesi SMS4H..."),
komut yazmasına gerek yoktur. Bu, `.claude/skills/urun-arastir/SKILL.md` altındaki
`urun-arastir` skill'ini tetiklemelidir — mesaj bir soru/komut değil de kabaca bir
ürün/marka/model adıysa bu skill'i çağır. Kullanıcı isterse açıkça `/urun-arastir <ürün>`
yazarak da tetikleyebilir.

Skill, `.claude/agents/` altındaki 4 özel subagent'ı kademeli olarak (NL → EU → Dünya)
çalıştırır, sonuçları EUR bazında birleştirir ve bir HTML Artifact raporu yayınlar.

## Bileşenler

- `.claude/skills/urun-arastir/SKILL.md` — orkestrasyon akışının tam tarifi.
- `.claude/agents/market-scout.md` — belirli bir pazar bölgesinde fiyat/satıcı/teslimat araştırması.
- `.claude/agents/reliability-analyst.md` — ürün/marka güvenilirliği, yorumlar, şikayetler.
- `.claude/agents/import-advisor.md` — AB dışı alımlarda gümrük/BTW/kargo maliyet hesabı.
- `.claude/agents/alternatives-scout.md` — muadil/alternatif ürün taraması.
- `reports/` — geçmiş araştırmaların Markdown özetleri (kullanıcı isteğiyle kaydedilir).

## Sabit kurallar

- Rapor dili: **Türkçe**.
- Para birimi: tüm fiyatlar **EUR**'ya çevrilir (yerel fiyat parantezde belirtilir),
  kullanılan kur ve tarih raporda açıkça belirtilir.
- Pazar sırası: **Hollanda → Avrupa → Dünya**, her zaman bu sırayla, hiçbir zaman atlanmaz.
- Kapsam: fiyat karşılaştırma + güvenilirlik/yorumlar + gümrük-vergi-lojistik + alternatifler
  (dördü de her araştırmada yer alır).
- Çıktı: görsel HTML Artifact (karşılaştırma tabloları + net tavsiye ile).

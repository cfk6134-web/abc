# Sonraki adım: resmî fotoğrafları eklemek

`stabilite.html` beş stabilite ayakkabısını (ASICS GEL-Kayano 32, New Balance 860 v14, HOKA Gaviota 6,
Brooks Glycerin GTS 23, Saucony Hurricane 26) teknoloji, ölçü ve ayak profiline göre karşılaştırıyor.
Yayınlanmış hali: https://claude.ai/artifact/JFtyumHJy3fkUa99Bf5cZ7

Önceki oturumda ağ politikası marka sitelerini (asics.com, newbalance.com, hoka.com, brooksrunning.com,
saucony.com ve görsel sunucuları nb.scene7.com, dms.deckers.com, images.asics.com) engellediği için
orijinal fotoğraflar eklenemedi. Araştırma verisi: `arastirma/stabilite-ayakkabilari.json`.

Ağ erişimi açık yeni oturumda yapılacaklar:
1. Her modelin resmî ürün sayfasından (bağlantılar sayfada ve JSON'da) yan, iç yan, üst, taban ve
   arka açılardan ürün fotoğraflarını indir; boyutları küçült (≈1200 px, JPEG/WebP).
2. Fotoğrafları `stabilite.html` içindeki her ayakkabı bölümüne, şema çizimlerinin yanına açı sekmeli
   bir galeri olarak ekle; teknolojileri (4D Guidance, Stability Plane, H-Frame, GuideRails, CenterPath vb.)
   fotoğraf üzerinde numaralı işaretlerle göster. Kaynağı ve markayı belirt.
3. Artifact'i aynı URL'ye yeniden yayınla (url parametresiyle, önce read).

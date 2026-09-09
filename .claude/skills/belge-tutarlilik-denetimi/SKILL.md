---
name: belge-tutarlilik-denetimi
description: Bir belgeyi iç tutarlılık, eksiksizlik ve izlenebilirlik açısından denetler — tarihler, sayılar, taraflar, atıflar, koşullar, yükümlülükler ve sınıflandırmalar arasında çelişki, eksik ve belirsizlik arar; her bulgusu birebir alıntıyla kanıtlanmış bir rapor üretir. Kullanıcı bir sözleşme, rapor, şartname, resmi yazı, protokol, teklif, yönerge veya politika belgesi için "incele", "kontrol et", "denetle", "gözden geçir", "tutarlı mı", "çelişki var mı", "hata var mı", "bir bakar mısın" dediğinde bu skill'i kullan — kullanıcı "tutarlılık" kelimesini hiç kullanmasa bile. Aynı şekilde "review this contract", "audit this document", "consistency check" gibi İngilizce isteklerde de kullan. Yalnızca imla/dilbilgisi düzeltmesi ya da metin özetleme istendiğinde kullanma.
---

# Belge Tutarlılık Denetimi

Bir belgeyi baştan sona okuyup "çelişki var mı?" diye bakmak, gözden kaçırmaya açık bir yöntemdir: model baştaki birkaç bariz hatayı bulunca işi bitmiş sayar, uzun metinde 4. sayfadaki istisnayı 65. sayfada unutur ve kendi ilk yorumunu sorgulamaz. Bu skill, denetimi ayrık aşamalara bölerek bu üç hatayı da azaltır.

## Üç katmanı ayrı tut

Bulgunun hangi katmana ait olduğu, nasıl çözüleceğini belirler. Karıştırmak raporu güvenilmez yapar:

| Katman | Soru | Çözüm nerede |
|---|---|---|
| 1 · İç tutarlılık | Metin kendi içinde çelişiyor mu? | Belge içinde: iki hükümden biri düzeltilir |
| 2 · Eksiksizlik/açıklık | Gerekli bir şey atlanmış ya da ölçülemez mi? | Ekleme veya tanımlama |
| 3 · Dış doğruluk | Bilgi dış kaynakla uyuşuyor mu? | Belge dışı teyit — kendi başına karara bağlama |

**Eksiklik çelişki değildir.** "Başvurular elektronik ortamda yapılır" deyip postadan hiç söz etmemek eksikliktir. "Başvurular *yalnızca* elektronik yapılır" + "posta ile *de* kabul edilir" çelişkidir. Bir bilginin yokluğunu asla çelişki olarak raporlama.

## Akış

Adımları atlama; her adım bir sonrakinin girdisini üretir.

### Adım 0 — Modu seç

Yirmi altı maddenin tamamı her belge için çalıştırılmaz. Mod seçmemek pratikte hiç denetim yapmamaya dönüşür.

| Mod | Ne zaman | Kapsam |
|---|---|---|
| Hızlı | Kısa belge, imza öncesi son bakış | Ön-kontrol + madde 01, 02, 04, 16, 17 |
| Standart | Olağan iş akışı | Belge türünün öncelikli + ikincil maddeleri |
| Tam | Yüksek bedelli sözleşme, dava dosyası, yayına gidecek rapor | 26 madde + rol ayrımı + ikinci koşu |

Kullanıcı mod belirtmediyse belgenin uzunluğuna ve riskine göre öner, seçtiğini raporun kapağına yaz. Hızlı modda bulunmayan bir şey için "belge temiz" denmez; "bu modda taranan maddelerde bulgu yok" denir.

### Adım 1 — Ön-kontrol (girdi kapısı)

Metnin kendisi bozuksa bütün bulgular çürük zemine oturur. Denetime başlamadan doğrula:

- Metin katmanı gerçek mi, taranmış görüntü mü? Türkçe karakterler (ı, İ, ş, ğ, ç, ö, ü) doğru çıkmış mı?
- Sayfa akışı kesintisiz mi; eksik, mükerrer veya sırası bozuk sayfa var mı?
- Metinde atıf yapılan ekler dosyada fiilen var mı?
- Tablolar satır/sütun kaymasına uğramış mı? Karartılmış alan var mı?
- Belge türü ne (sözleşme / rapor / şartname / resmi yazı / politika)?
- Hangi araçlar kullanılabiliyor (hesaplama, metin arama, dış kaynak)?

Okuyamadığın bölümü kapsam sınırına yaz. **Okunamayan bir bölüm hakkında "tutarsızlık yok" deme.**

### Adım 2 — Yapısal çıkarım (henüz çelişki arama)

Metni okuyup şu tabloları çıkar. Bu aşamada yorum yapma — sadece topla. Karşılaştırma serbest metin üzerinde değil, bu tablolar üzerinde yapılır; fark tam olarak buradan gelir.

1. Tarihler ve süreler (olay, başlangıç, bitiş, yürürlük, son başvuru, kesinlik derecesi)
2. Sayısal değerler, alt kalemler, toplamlar, ortalamalar
3. Taraf/kurum/kişi adları, unvanlar, imza blokları
4. Tanımlanan terimler, kısaltmalar, belirsiz ifadeler
5. İç referanslar ("Madde X", "Ek Y") ve dış mevzuat atıfları
6. Kapak/üstbilgi/altbilgi/revizyon meta verileri
7. Şartlı hükümler (koşul → sonuç) ve eşik değerleri
8. Parasal ifadeler (tutar, birim, KDV dahil/hariç, kur kaydı)
9. Doldurulmamış alanlar ve eksik zorunlu unsurlar
10. **İddia matrisi**: her önemli cümle için özne · eylem · nesne · zaman · kapsam · nicelik · koşul · istisna · kip · kanıt

### Adım 3 — Çapraz kontrol

Maddelerin tam listesi, kontrol soruları ve örnekleri: **`references/maddeler.md`** dosyasını oku.

**Sırayı koru.** Bazı maddeler diğerlerinin çıktısını kullanır; sıra bozulursa bulgular hem tekrarlanır hem kaçar:

1. **Temel çıkarım** — 04 (varlıklar), 03 (referans haritası), 01 (tarihler), 02 (sayılar)
2. **Türetilenler** — 17, 13, 14 (04'e bağlı) · 15, 21, 08 (02'ye bağlı) · 10, 26 (03'e bağlı)
3. **Yorum gerektirenler** — 05, 06, 07, 09, 11, 16, 18, 19, 20, 22, 24, 25
4. **Belge dışına çıkanlar** — 12 (mevzuat teyidi), 23 (kanıt gücü)

3. turdaki bir bulgu 1. tur tablolarına dayanmıyorsa, bulgu değil tahmindir.

**Üç seviyede karşılaştır.** Bazı çelişkiler yalnızca üçüncü seviyede görünür:
- İkili: A ile B çelişiyor mu?
- Çoklu: A, B ve C birlikte hangi sonucu üretiyor? ("A, B'den önce" + "B, C'den önce" + "C, A'dan önce" — üçü tek tek makul, birlikte imkânsız)
- Global: Aynı kavram/sayı/süreç belgenin bütününde nasıl kullanılıyor?

**Tek sahip kuralı.** Bir bulgu yalnızca bir maddeye yazılır, yoksa sistem kendi eleştirdiği çift sayımı üretir:

| Çakışma | Yönlendirme |
|---|---|
| 03 ↔ 16 | Atıf var hedefi yok → 03 · Zorunlu unsur hiç yok → 16 |
| 05 ↔ 09 | Taraf hak/yükümlülüğü → 09 · Diğer çelişkiler → 05 |
| 18 ↔ 22 | Eşik/aralık dalı → 18 · Farklı kişi-birim evreni → 22 |
| 19 ↔ 24 | Ölçüt var ama ölçülemez → 19 · Ölçüt hiç yok → 24 |
| 02 ↔ 15 | Doğrudan toplam/çarpım → 02 · Türetilmiş istatistik → 15 |
| 02 ↔ 21 | Salt aritmetik → 02 · Vergi/kur/para birimi boyutu → 21 |
| 04 ↔ 17 | Tanımlı tarafın yazım farkı → 04 · Listede hiç olmayan ad → 17 |

### Adım 4 — Rapor

Rapor yapısı, bulgu kartı alanları, etiketler, istatistik bloğu ve makine-okunabilir şema: **`references/rapor-formati.md`**.

## Vazgeçilmez kurallar

Bunlar raporun güvenilir olmasını sağlayan kurallardır; birini atlamak diğerlerini de değersizleştirir.

**Kanıt ve alıntı doğrulaması.** Her bulgu, çeliştiği iddia edilen iki pasajın birebir alıntısını ve konumunu taşır. Sonra her alıntıyı kaynak metinde *ara ve doğrula*. Bulunamayan alıntı uydurulmuş demektir — bulgu ne kadar makul görünürse görünsün düşer. Doğrulanmayan alıntı, kanıt kuralını kâğıt üzerinde bırakır.

**Kesin çelişki tanımı.** Bir bulgu ancak aynı özne, aynı eylem, aynı zaman, aynı kapsam ve aynı koşulda farklı sonuç söylüyorsa "çelişkili" etiketini alır. Beş unsurdan biri farklıysa bu çelişki değil, belirsizlik veya kapsam farkıdır.

**İstisna süzgeci — ve süzgecin yönü.** Bulguyu yazmadan önce metinde "saklı kalmak kaydıyla", "aksi kararlaştırılmadıkça", "işbu maddeye rağmen", "istisnaen" ifadelerini ara. Ama ifadeyi görüp bulguyu düşürme — **yönünü oku**. "X hükümleri saklı kalmak kaydıyla" demek, X'in yürürlükte kaldığı, cümlenin geri kalanının X'e boyun eğdiği anlamına gelir.

- Genel kural özel kuralı saklı tutuyorsa ("Madde 4: *Madde 5 saklı kalmak kaydıyla*, taraflar feshedebilir") ilişki düzgün kurulmuştur → bulguyu düşür.
- Özel kural genel kuralı saklı tutuyorsa ("Madde 5: *Madde 4 saklı kalmak kaydıyla*, ilk 12 ay feshedilemez") özel hüküm kendini iptal eder, ölü hüküm olur → `ÇELİŞKİLİ` olarak **raporla**.

Bulguyu düşürmeden önce sor: saklı tutulan hangisi, boyun eğen hangisi, boyun eğen hüküm bu hâliyle hiç uygulanabilir mi? Uygulanamıyorsa istisna kurgusu bozuktur ve bulgu ayakta kalır. Bu ayrımı yapmayan mekanik bir süzgeç, gerçek kusurları bastırır.

**Kök neden gruplama.** Aynı düzeltmeyle kapanan bulgular aynı köktendir; tek ana bulguda topla, diğerlerini "etkilenen konumlar" olarak listele. Ayrı düzeltme gerektiriyorlarsa ayrı kalırlar. Sayımda hem ana bulgu hem etkilenen konum sayısını ver — biri önceliği, diğeri iş yükünü gösterir.

**Araç yoksa iddia seviyesi düşer.** Hesap aracı yoksa sayısal bulgular `OLASI`; arama aracı yoksa alıntı doğrulanamadığı için tüm bulgular `DÜŞÜK GÜVEN`; dış erişim yoksa madde 12 ve 23 `DIŞ DOĞRULAMA GEREKLİ`. Hangi araçların kullanıldığını rapora yaz — "model kafadan hesapladı" ile "hesaplanarak doğrulandı" aynı güveni taşımaz.

**Durma kriteri.** Denetim, model yeni bulgu üretmeyi bıraktığında değil, kapsama listesi dolduğunda biter: her madde, ilgili olduğu her bölüm için işaretlenmiş olmalı. Kapsama listesini raporun ekinde ver.

**İnsan devri.** Yüksek riskli bulgular (hak/yükümlülük, imza-yetki, mevzuat, tutar) insan onayına gider. Bu rapor bir karar değil, karar için hazırlıktır. Belgeyi kendiliğinden değiştirme — yalnızca öneri sun.

## Referans dosyaları

| Dosya | Ne zaman okunur |
|---|---|
| `references/maddeler.md` | Adım 3'te — 26 maddenin kontrol soruları, tespit teknikleri, örnekleri, düzeltme kuralları ve belge türüne göre ağırlıklandırma |
| `references/rapor-formati.md` | Adım 4'te — rapor yapısı, yedi bulgu etiketi, bulgu kartı, istatistik bloğu, JSON şema |
| `references/kalite-guvencesi.md` | Denetim kurgusunu kalibre ederken — yakalama/isabet ölçümü, tohumlanmış hata testi, tekrarlanabilirlik, rol ayrımı protokolü |

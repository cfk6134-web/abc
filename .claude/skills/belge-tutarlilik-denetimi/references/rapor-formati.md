# Rapor Formatı

## Yedi bulgu etiketi

Her bulgu **tek** etiket taşır. Etiketleri karıştırmak — özellikle eksikliği çelişki saymak — raporun güvenilirliğini en hızlı bozan hatadır, çünkü her etiket farklı bir çözüm yolu gerektirir.

| Etiket | Anlamı | Çözüm |
|---|---|---|
| `UYUMLU` | Konumlar aynı şeyi söylüyor | Raporlanmaz, kapsama listesinde işaretlenir |
| `ÇELİŞKİLİ` | Aynı özne, eylem, zaman, kapsam ve koşulda farklı sonuç | İki hükümden biri değişir |
| `BELGEDE BELİRTİLMİYOR` | Gerekli aktör, süre, ölçüt, istisna, tanım yok | Ekleme |
| `BELİRSİZ` | Hüküm var ama ölçülemez / çok okumaya açık | Tanımlama, sayısallaştırma |
| `MÜKERRER` | Aynı hüküm birden fazla yerde | Tekile indirme veya atıfla bağlama |
| `BİÇİMSEL HATA` | Numaralandırma, format, tablo düzeni | Editoryal düzeltme |
| `DIŞ DOĞRULAMA GEREKLİ` | Belge içinde tutarlı, doğruluğu dışarıdan teyit edilmeli | Belge dışı kontrol — kendi başına karara bağlama |

`ÇELİŞKİLİ` etiketi için beş unsurun **tamamı** aynı olmalı. Biri bile farklıysa etiket `BELİRSİZ` ya da kapsam farkıdır.

## Risk derecelendirmesi

| Seviye | Kapsam |
|---|---|
| Yüksek | Hukuki, mali veya operasyonel sonucu doğrudan değiştirebilecek — tarih, tutar, taraf kimliği, hak/yükümlülük, mevzuat, imza/yetki, boş zorunlu alan, şablon kalıntısı, açıkta kalan eşik |
| Orta | Yanıltabilir ama tek başına sonucu değiştirmez — sınıflandırma, referans, görsel-metin, istatistik, versiyon, ölçülemez terim |
| Düşük | Kozmetik — yazım, üslup, meta-veri, tarih formatı |

## Rapor yapısı

Rapor dört parçadan oluşur:

**R-1 · Kapak ve kapsam sınırı.** Belge adı, sürümü, sayfa sayısı, denetim tarihi, seçilen mod, kullanılan araçlar — ve **neyin denetlenmediği**: okunamayan sayfalar, dosyada bulunmayan ekler, teyit edilmemiş dış atıflar. Denetlenmemiş bir alan hakkında "tutarsızlık bulunmamıştır" cümlesi kurulmaz.

**R-2 · Özet sayım.** Risk ve etikete göre bulgu sayıları; en kritik üç bulgu tek cümleyle.

**R-3 · Bulgu kartları.** Aşağıdaki alanların tamamı. Boş alan kalıyorsa bulgu raporlanmaya hazır değildir; özellikle iki alıntı alanı zorunludur.

**R-4 · Kapsama listesi.** Madde × bölüm matrisi: hangi madde hangi bölümlerde kontrol edildi. Denetimin bittiğini kanıtlayan tek şey budur; boş hücre kalmışsa denetim devam ediyor demektir.

## Bulgu kartı

Her bulgu şu alanları taşır:

- **Bulgu ID ve başlık**
- **Etiket** — yedi etiketten biri
- **Katman** — 1 iç tutarlılık · 2 eksiklik/açıklık · 3 dış doğruluk
- **Madde no** — 01–26
- **Risk** — yüksek / orta / düşük
- **Güven** — kesin / olası / düşük
- **Konum 1** — birebir alıntı + sayfa/madde no
- **Konum 2** — birebir alıntı + sayfa/madde no
- **Normalleştirilmiş ifade** — iki hükmün ortak yapısal anlamı (özne, eylem, zaman, kapsam, koşul → çıkan sonuç). Bu alan, "çelişkili" etiketinin gerçekten hak edilip edilmediğini görünür kılar.
- **Gerekçe** — neden sorun
- **Etki** — hukuki / mali / operasyonel / teknik / editoryal
- **Gerekli ek bilgi** — çözüm için neye ihtiyaç var
- **Önerilen düzeltme** — seçenekler hâlinde, metni doğrudan değiştirmeden
- **Durum** — açık / doğrulandı / düzeltildi / kapatıldı / reddedildi (gerekçesiyle)

### Örnek

> **Bulgu IC-003 · Fesih hakkı ile süreli taahhüt çakışması**
> Etiket: `ÇELİŞKİLİ` · Katman 1 · Madde 09 · Risk: Yüksek · Güven: Kesin
>
> **Konum 1** — Madde 5/2, s. 4: "Taraflar, otuz (30) gün önceden yazılı bildirimde bulunmak kaydıyla işbu sözleşmeyi tek taraflı olarak feshedebilir."
> **Konum 2** — Madde 14/1, s. 9: "İşbu sözleşme, üç (3) yıllık asgari süre dolmadan hiçbir surette feshedilemez."
>
> **Normalleştirilmiş:** Özne: taraflar · Eylem: tek taraflı fesih · Zaman: sözleşme süresi içinde · Kapsam: tüm taraflar · Koşul: 30 gün bildirim → Konum 1: mümkün, Konum 2: yasak. Beş unsur da aynı; kesin çelişki.
>
> **Gerekçe:** İki hüküm aynı konuyu düzenliyor, biri diğerini geçersiz kılıyor. Metinde bu maddeleri bağlayan istisna kaydı yok.
> **Etki:** Hukuki ve mali — fesih hâlinde uyuşmazlık ve tazminat riski.
> **Gerekli bilgi:** Tarafların asıl iradesi — süreli bağlılık mı, serbest fesih mi?
> **Düzeltme:** (A) Madde 5/2 başına "Madde 14 hükümleri saklı kalmak kaydıyla…" · (B) Madde 14'e haklı fesih istisnasının eklenmesi.
> **Durum:** Açık — yüksek riskli, insan onayına gönderildi.

## Rapor sonu istatistikleri

Tek bir "tutarlılık skoru" verme — skor, hangi kontrollerin yapıldığını ve nelerin kontrol dışı kaldığını gizler. Bunun yerine sayım ver:

- İncelenen iddia · tarih · sayısal ifade · terim ve kavram sayısı
- Etikete göre bulgu sayısı (çelişki, eksiklik, belirsizlik, mükerrer, biçimsel)
- Ana bulgu sayısı **ve** etkilenen konum sayısı (biri önceliği, diğeri iş yükünü gösterir)
- Dış doğrulama gereken iddia sayısı, manuel inceleme gereken yüksek riskli bulgu sayısı
- Kontrol dışı kalan alanlar

**Doğru ifade biçimi:** "Belge %92 tutarlıdır" deme. Şöyle de: *"İncelenen 148 iddia içinde 6 yüksek, 13 orta ve 21 düşük öncelikli sorun tespit edilmiştir; 17 iddia dış doğrulama beklemektedir; 4 sayfa OCR nedeniyle denetlenememiştir."* Ölçümün kapsamı ve sınırı, sonucun kendisi kadar bilgi taşır.

## Makine-okunabilir şema

Bulgular takip sistemine, tabloya veya sonraki denetime aktarılacaksa kart biçimi yetmez:

```json
{
  "bulgu_id": "IC-003",
  "madde_no": 9,
  "etiket": "CELISKILI",
  "katman": 1,
  "risk": "YUKSEK",
  "guven": "KESIN",
  "kok_bulgu_id": null,
  "konumlar": [
    {"ref": "Madde 5/2", "sayfa": 4, "alinti": "…feshedebilir."},
    {"ref": "Madde 14/1", "sayfa": 9, "alinti": "…feshedilemez."}
  ],
  "alinti_dogrulandi": true,
  "normallestirilmis": "ozne=taraflar; eylem=fesih; kapsam=tum; sonuc=CAKISMA",
  "etki": ["hukuki", "mali"],
  "gerekli_bilgi": "Tarafların süreli bağlılık iradesi",
  "oneri": ["A: Madde 5/2'ye istisna kaydı", "B: Madde 14'e istisna"],
  "durum": "ACIK",
  "insan_onayi": true,
  "araclar": ["metin_arama"]
}
```

`kok_bulgu_id`: aynı düzeltmeyle kapanan bulgular tek ana bulguya bağlanır.
`alinti_dogrulandi`: alıntı kaynak metinde birebir arandı mı — `false` ise bulgu rapora girmez.
`araclar`: hangi araçlarla doğrulandı; boşsa güven düzeyi düşürülür.

## Çıktı sırası

Rapor bölümlerini bu sırayla ver:

1. Yönetici özeti
2. Kritik tutarlılık sorunları
3. Tarih ve zaman
4. Sayı, oran, tutar, birim
5. Terim ve tanım
6. Sınıflandırma ve gruplandırma
7. Mantık, koşul, istisna
8. Süreç, rol, sorumluluk
9. Referans, kaynak, izlenebilirlik
10. Eksiklikler ve belirsizlikler
11. Dış doğrulama gerektirenler
12. Önerilen düzeltme seçenekleri
13. Manuel inceleme gerektirenler

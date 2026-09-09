# Kalite Güvencesi ve İşletim Protokolü

Bu dosya, denetimin kendi güvenilirliğini ölçen ve yürütmesini düzenleyen kuralları içerir. SKILL.md'deki akış "ne aranacağını" söyler; burası "çıkan raporun güvenilir olduğunu nasıl bileceğimizi" söyler.

## KG · Kalite güvencesi

### KG-1 · Kanıt kuralı ve alıntı doğrulaması
Her bulgu, çeliştiği iddia edilen iki pasajın birebir alıntısını ve konumunu taşır. Alıntı üretilemiyorsa bulgu rapora girmez.

Kural burada bitmez: **her alıntı kaynak metinde birebir aranarak doğrulanır** — metinsel arama ile, göz kararıyla değil. Aranan dizge bulunamıyorsa alıntı uydurulmuş demektir ve bulgu, içeriği ne kadar makul görünürse görünsün düşer. Doğrulanmamış alıntı, kanıt kuralını kâğıt üzerinde bırakır.

### KG-2 · Yanlış pozitif süzgeci — ve süzgecin yönü
Görünürdeki her çelişki hata değildir; bilinçli bir istisna olabilir. Bulguyu raporlamadan önce metinde şu ifadeleri ara: `saklı kalmak kaydıyla`, `aksi kararlaştırılmadıkça`, `işbu maddeye rağmen`, `istisnaen`, `bu hükmün istisnası olarak`.

**Ancak ifadenin varlığı yetmez — yönünü de oku.** "X hükümleri saklı kalmak kaydıyla" demek, *X'in yürürlükte kaldığı, cümlenin geri kalanının X'e boyun eğdiği* anlamına gelir. Süzgeci mekanik uygularsan — ifadeyi görüp bulguyu düşürürsen — gerçek bir kusuru bastırırsın. Üç olasılığı ayır:

| Kurgu | Anlam | Karar |
|---|---|---|
| Genel kural, özel kuralı saklı tutuyor ("Madde 4: *Madde 5 saklı kalmak kaydıyla*, taraflar feshedebilir") | Özel kural genel kuralı sınırlıyor | Kural-istisna ilişkisi kurulmuş → bulguyu **düşür** |
| Özel kural, genel kuralı saklı tutuyor ("Madde 5: *Madde 4 saklı kalmak kaydıyla*, ilk 12 ay feshedilemez") | Genel kural korunuyor, özel kural kendini iptal ediyor | Özel hüküm **ölü hüküm** hâline geliyor → `ÇELİŞKİLİ` olarak **raporla** |
| İki hüküm arasında hiçbir bağlayıcı ifade yok | Bağ kurulmamış | `ÇELİŞKİLİ` olarak raporla |

İkinci satır gerçek bir kaleme alma kusurudur ve mekanik süzgeç tam olarak bunu kaçırır. Bulguyu düşürmeden önce sor: *saklı tutulan hüküm hangisi, boyun eğen hangisi, ve boyun eğen hüküm bu hâliyle hiç uygulanabilir mi?* Uygulanamıyorsa istisna kurgusu bozuktur, bulgu ayakta kalır.

### KG-3 · Tohumlanmış hata testi: yakalama ve isabet
Belgenin bir kopyasına bilerek 10 hata yerleştirip denetimi bu kopya üzerinde çalıştır. **İki oranı birlikte ölç:**

- **Yakalama (recall):** 10 tohumun kaçı bulundu?
- **İsabet (precision):** Raporlanan bulguların kaçı gerçek (tohum ya da doğrulanmış hata), kaçı uydurma?

Yalnızca yakalamayı ölçmek, her cümleye çelişki diyen bir kurgunun mükemmel görünmesine yol açar. Denetimde yanlış alarm, kaçırmadan daha hızlı güven kaybettirir.

**Standart tohum listesi** (tekrarlanabilirlik için sabit tut — her tohum farklı bir maddeyi hedefler):

| # | Tohum | Hedef madde |
|---|---|---|
| 1 | Bir tarihi kaydır | 01 |
| 2 | Bir alt toplamı boz | 02 |
| 3 | Var olmayan bir eke atıf ekle | 03 |
| 4 | Bir taraf adının unvanını değiştir | 04 |
| 5 | Bir gider kalemini iki farklı kategoriye koy | 06 |
| 6 | Bir yükümlülüğü öneriye çevir | 09 |
| 7 | Bir zorunlu alanı boşalt | 16 |
| 8 | Başka bir sözleşmeden kurum adı bırak | 17 |
| 9 | Bir eşiği açıkta bırak (tam sınır değeri) | 18 |
| 10 | Özetteki bir kısıtı sil | 26 |
| 11 | Ters yönlü istisna kaydı ekle: özel hüküm genel hükmü saklı tutsun | 09 + KG-2 |

Bulunmayan tohum, o maddenin kurgusundaki zayıflığı adresler — oran düşükse sorun belgede değil, kurguda.

### KG-4 · Durma kriteri
Denetim, "model yeni bulgu üretmiyor" diye bitmez — bu, ajan tembelliğinin ta kendisidir. Denetim **kapsama listesi dolduğunda** biter: her madde, ilgili olduğu her bölüm için işaretlenmiş olmalıdır. Kapsama listesi raporun eki olarak sunulur.

### KG-5 · Kapsam sınırı beyanı
Raporun ilk bölümü *neyin denetlenmediğini* yazar: okunamayan sayfalar, dosyada bulunmayan ekler, dış kaynağa karşı teyit edilmemiş mevzuat atıfları, görsel içeriği çözülemeyen grafikler. Denetlenmemiş bir alan hakkında "tutarsızlık bulunmamıştır" cümlesi kurulmaz.

### KG-6 · Tekrarlanabilirlik kontrolü
Aynı belge, aynı talimatla iki kez denetlenir ve bulgu listeleri karşılaştırılır. Her iki koşuda da çıkan bulgular `KESİN`, yalnızca birinde çıkanlar `OLASI` etiketiyle raporlanır. Bu, modelin dalgalanmasını gizlemek yerine ölçülebilir hâle getirir.

### KG-7 · Araçsız denetim kuralı
Bu rehber yer yer hesaplama, metinsel arama veya dış kaynak sorgusu varsayar. Araçlar yoksa denetim durmaz, ama **iddia seviyesi düşer**:

| Eksik araç | Sonuç |
|---|---|
| Hesaplama | Madde 02, 15, 21 bulguları `OLASI` |
| Metinsel arama | Alıntı doğrulanamadığı için tüm bulgular `DÜŞÜK GÜVEN` |
| Dış kaynak erişimi | Madde 12 ve 23 `DIŞ DOĞRULAMA GEREKLİ` |

Hangi araçların kullanıldığı raporda listelenir. "Model kafadan hesapladı" ile "hesaplanarak doğrulandı" aynı güven düzeyini taşımaz; bunu gizlemek raporu güvenilmez kılar.

## İP · İşletim protokolü

### İP-1 · Roller ve devir formatı
- **Çıkarıcı** yalnızca tabloları üretir; yorum yapmaz.
- **Denetçi** tablolardan aday bulguları kanıtlı biçimde çıkarır.
- **İtirazcı** her aday bulgu için metinde istisna/gerekçe arar ve düşürülmesini önerir.
- **Karar verici** ikisini karşılaştırıp bulguyu kabul, ret veya "insana götür" olarak işaretler.

Devirde yalnızca yapılandırılmış çıktı aktarılır — ham metin sonraki role yeniden verilmez. Böylece önceki rolün yorumu sonrakini yönlendirmez. Tek oturumda çalışıyorsan bu rolleri ayrı geçişler olarak sırayla üstlen; en azından "iddia" ve "itiraz" geçişlerini ayır.

### İP-2 · Parçalama kuralları
Bölme daima **madde/bölüm sınırından** yapılır, cümle ortasından değil. Her parçadan ayrı varlık tablosu çıkarılır; tablolar birleştirildikten sonra *parçalar arası* kontrol ayrıca çalıştırılır — kaçırılan çelişkilerin çoğu tam olarak iki parçanın arasında oturur.

### İP-3 · İnsan devir noktası
Yüksek riskli her bulgu (hak/yükümlülük, imza-yetki, mevzuat atfı, tutar) insan onayına gider. Yapay zekâ raporu bir **karar değil, karar için hazırlıktır**; hukuki sonuç doğuran hiçbir düzeltme onaysız uygulanmaz.

### İP-4 · Bulgu yaşam döngüsü
`Açık` → `Doğrulandı` → `Düzeltildi` → `Kapatıldı`. Beşinci durum `Reddedildi`, yalnızca gerekçesiyle kaydedilir — reddedilen bulgular silinmez, çünkü sonraki denetimde aynı tartışma yeniden açılır.

### İP-5 · Düzeltme sonrası regresyon denetimi
Düzeltmeler yeni çelişki doğurur: bir tarihi düzeltmek, ona atıf yapan üç maddeyi bozabilir. Düzeltilen her bölüm, **ona atıf yapan tüm bölümlerle birlikte** yeniden denetlenir. Çapraz referans haritası tam olarak bu listeyi verir.

### İP-6 · Kök neden gruplama
Kırk bulgunun on ikisi tek kök hatadan geliyorsa — bir taraf adının baştan yanlış tanımlanması gibi — ayrı ayrı raporlamak okuyucuyu boğar ve gerçek önceliği gizler. Aynı kökten doğan bulgular **tek ana bulgu** altında toplanır; diğerleri "etkilenen konumlar" olarak listelenir.

**Gruplama kuralı:** İki bulgu *aynı düzeltmeyle birlikte kapanıyorsa* aynı köktendir. Ayrı düzeltme gerektiriyorlarsa ayrı kalırlar. Sayımda hem ana bulgu hem etkilenen konum sayısı verilir.

## Kavramsal dayanaklar

Bu sistem şu çerçevelerden beslenir: normatif kip ayrımı için RFC 2119'un zorunluluk/tavsiye/izin kademesi; ölçümün kapsamının ve kontrol dışı kalan alanların raporlanması için ISO 8000 veri kalitesi yaklaşımı; zaman ilişkileri için OWL-Time'ın önce/sonra/örtüşür modeli; kavram hiyerarşisi için SKOS'un tercih edilen ad / alternatif ad / daha geniş-dar kavram yapısı; kaynak izlenebilirliği için PROV provenans modeli; açıklık, eksiksizlik, çelişkisizlik ve doğrulanabilirliğin ayrı kalite ölçütleri olarak ele alınması için NASA'nın gereksinim kalitesi ölçütleri.

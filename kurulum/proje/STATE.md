# STATE.md — <proje adı>

Bu dosya projenin tek doğruluk kaynağıdır. Oturum başında okunur, oturum sonunda yazılır.
Çelişki çıkarsa bu dosya kazanır.

## 1. Doğrulanmış gerçekler
<!-- Kontrol edilmiş, artık tahmin edilmeyecek bilgiler.
     Her satırda NASIL doğrulandığı, NE ZAMAN ve KAYNAĞIN GÜVENİLİRLİĞİ yazar.
     TAZELİK: dayandığı şey değiştiyse veya kayıt 10 koşudan eskiyse, kullanmadan önce yenile.
     Tazelenmemiş gerçek, "doğrulanmış" etiketi taşıdığı için tahminden daha tehlikelidir.
     kaynak: KARANTİNALI ise §11.1'in ek doğrulama şartı uygulanmadan bu satır kullanılamaz. -->
- …  (doğrulama: …, tarih: …, kaynak: güvenilir | KARANTİNALI)

## 2. Genel kurallar
<!-- Yeniden türetmeden önce buraya bak. Projeler arası geçerliyse ~/.claude/KURALLAR.md'ye taşı. -->
- …

## 3. Açık başarısızlıklar
<!-- Henüz çözülmemiş. Yeniden üretim adımı zorunlu. ÖZ-DENETİM blokları da buraya. -->
- …  (hipotez: …, yeniden üretim: …)

## 4. Öğrenilen dersler
<!-- Kök-neden kurullarından damıtılmış kalıcı kurallar. -->
- …

## 5. Kararlar ve gerekçeleri
<!-- "Neden böyle yaptık" sorusunun tek cevabı.
     DİKKAT: Doğrulayıcı ve Final Kurulu üyelerine bu bölüm VERİLMEZ (§6.1 körlük istisnası). -->
- …

## 6. Kapsam kayıtları
<!-- Ölçü ESERDEN okunur, ajanın beyanından değil. Yalnız Kapsam Uyumu Denetçisi yazar.
     Sonraki listeleri buradan boyutlandır.
     Süre yazılmaz: ajanın kendi süre beyanı yaptırıma bağlanamaz (§5.1).
     Ebeveyn damgası ayrı dosyada: ~/.claude/ajan-telemetri.log -->
- koşu: … | görev tipi: … | ajan: … | listelenen: … | işlenen: … | liste dışı: …
  | kalite: GEÇTİ/KALDI | hüküm: … | not: …

## 7. Son oturum
<!-- Devam et, yeniden başlama. Kademe kaydı da buraya.
     DİKKAT: karantinalı kaynaktan türeyen bir EYLEM CÜMLESİ buraya yazılamaz (§11.1);
     yalnız nötr işaretçi: "karantinalı girdi bekliyor: <konum>". -->
- <tarih> · kademe: S<n>, gerekçe: … · yapılanlar: … · sıradaki adım: …

## 8. Kapanmış başarısızlıklar
<!-- §3 yalnız AÇIK olanları tutar. Tekrarı görmek ve kural etkinliğini ölçmek için
     kapanmış hatalar kimliğiyle burada kalır. §4.2 ve §10.4'ün "aynı hatanın 2. tekrarı"
     tetikleyicisi ve §12 adım 6'nın kural etkinlik ölçümü BU TABLOYA bakar;
     tutulmazsa ikisi de ölür. -->
- hata sınıfı: … | ilk görülme: … | kapanma: … | ürettiği kural: … | sonraki tekrarlar: […]

## 9. Koşu ölçüleri
<!-- §14.4'ün DBO/ZKO/KEO'su buradan hesaplanır. Koşu başına tek satır; hepsi mevcut
     çıktılardan doldurulur, ek ölçüm işi yoktur. -->
- koşu: <no> | kademe: S<n> | 1. turda kalite kapısı: geçti/kaldı
  | teslim sonrası kullanıcı düzeltmesi: var/yok | zincir kaçırma: evet/hayır
  | final kurulu RET: <n> | N_FİNAL: <n> | çapraz denetim çelişkisi: <n>

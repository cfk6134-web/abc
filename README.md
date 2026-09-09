# Belge Tutarlılık Denetimi

Bir belgeyi yapay zekâya iç tutarlılık, eksiksizlik ve izlenebilirlik açısından incelettirmek için kurulmuş bir denetim sistemi.

## İçerik

| Yol | Ne |
|---|---|
| `.claude/skills/belge-tutarlilik-denetimi/` | Skill — Claude Code'da bir belge incelemesi istendiğinde otomatik devreye girer |
| `docs/tutarlilik-denetim-rehberi.html` | Aynı sistemin insan tarafından okunan hâli (tek sayfalık rehber) |

## Skill nasıl çalışır

Kullanıcı bir sözleşme, rapor, şartname veya resmi yazı için "incele / kontrol et / çelişki var mı" dediğinde skill devreye girer ve şu akışı yürütür:

1. **Mod seçimi** — Hızlı (5 madde) · Standart (belge türünün öncelikli maddeleri) · Tam (26 madde + rol ayrımı + ikinci koşu)
2. **Ön-kontrol** — metin katmanı, sayfa ve ek bütünlüğü, belge türü, kullanılabilir araçlar
3. **Yapısal çıkarım** — tarihler, sayılar, taraflar, atıflar, koşullar ve iddia matrisi ayrı tablolara çıkarılır; bu aşamada çelişki aranmaz
4. **Çapraz kontrol** — 26 madde, bağımlılık sırasına göre ve tek sahip kuralıyla uygulanır
5. **Rapor** — her bulgu birebir alıntıyla kanıtlanır, yedi etiketten biriyle sınıflandırılır, risk ve güven düzeyi taşır

## Sistemin dayandığı üç ayrım

- **İç tutarlılık** — metin kendi içinde çelişiyor mu? Çözüm belge içinde.
- **Eksiksizlik ve açıklık** — gerekli bir şey atlanmış veya ölçülemez mi? Çözüm ekleme.
- **Dış doğruluk** — bilgi dış kaynakla uyuşuyor mu? Çözüm belge dışı teyit.

Bir bilginin belgede bulunmaması çelişki değildir. "Başvurular elektronik yapılır" deyip postadan söz etmemek eksikliktir; "yalnızca elektronik yapılır" + "posta ile de kabul edilir" çelişkidir.

## Vazgeçilmez kurallar

- **Kanıt ve alıntı doğrulaması** — her bulgu iki birebir alıntı taşır, her alıntı kaynak metinde aranarak doğrulanır; bulunamayan alıntı bulguyu düşürür
- **Kesin çelişki tanımı** — aynı özne, eylem, zaman, kapsam ve koşulda farklı sonuç; beş unsurdan biri farklıysa çelişki değildir
- **Tek sahip kuralı** — bir bulgu yalnızca bir maddeye yazılır, yoksa çift sayım olur
- **Kök neden gruplama** — aynı düzeltmeyle kapanan bulgular tek ana bulguda toplanır
- **Araç yoksa güven düşer** — hesap veya arama aracı yoksa bulgular OLASI / DÜŞÜK GÜVEN olarak işaretlenir
- **Durma kriteri** — denetim, model yorulunca değil kapsama listesi dolunca biter
- **İnsan devri** — yüksek riskli bulgular onaya gider; rapor karar değil, karar için hazırlıktır

## Kalibrasyon

Sistemin kendi performansı `references/kalite-guvencesi.md` içindeki tohumlanmış hata testiyle ölçülür: belgenin bir kopyasına on bilinen hata yerleştirilir, hem yakalama (kaçı bulundu) hem isabet (kaçı uydurma) oranı hesaplanır. Yalnızca yakalamayı ölçmek, her cümleye çelişki diyen bir kurgunun mükemmel görünmesine yol açar.

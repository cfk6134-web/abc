---
name: ajan-isletim
description: Çok adımlı, çok ajanlı veya denetim gerektiren işler için tam işletim protokolünü açar — kademe seçimi (S1/S2/S3), paralellik kurulu, kapsam sınırı, doğrulama zinciri, kurullar, çapraz denetim, karantina ve öğrenme döngüsü. Şu durumlarda kullan: iş birden fazla alt göreve bölünüyorsa, birden fazla ajan paralel koşacaksa, geri dönüşü zor bir karar veya eylem varsa (veri silme, üretime çıkış, şema değişikliği), kullanıcı tam denetim veya oy birliği istediyse, bir doğrulayıcı RET verdiyse, ya da bir hatanın kök nedeni aranıyorsa. Kısa ve tek adımlık işlerde AÇMA — çekirdek kurallar CLAUDE.md'de zaten yüklü.
---

# Ajan işletim protokolü — v1.5

Tam metin: `~/.claude/AJAN-ISLETIM-TALIMATI.md` (sürümü bu dosyanınkiyle aynı olmalı — §15.2 adım 6)

> Aşağıdaki bölüm numaraları kayabilir. Bulamazsan numarayla değil **başlık metniyle** ara:
> `grep -n '^#\+ .*<anahtar kelime>' ~/.claude/AJAN-ISLETIM-TALIMATI.md`

## Bu skill tetiklendiğinde

1. **Kademeyi doğrula.** Çekirdekteki tabloya göre S2 mi S3 mü? Bu skill açıldıysa iş büyük
   ihtimalle S2'nin üstünde. Kademeyi `STATE.md` §7'ye yaz.

2. **Tam belgeyi oku — ama tamamını değil.** İhtiyacın olan bölümü aç:

| Ne yapacaksın | Oku |
|---|---|
| Kademe ve akış | §0.1, §2 |
| Kaç ajan paralel koşacak | §4.1 Paralellik Kurulu |
| İş nasıl sınırlanacak | §5.1 sınır biçimi, §5.2 kapsam planı, §5.3 tıkanma, §5.5 keşif işi |
| Alt görevlere bölme | §7 (4 testli bölme) |
| Ajan tanımı yazma | §3 (9 zorunlu alan), §13.1 şablon |
| Doğrulama kurma | §10.1 zincir, §10.2 rubrik, §13.2 şablon |
| Paralel ajanların çıktısını birleştirme | §10.5 çapraz denetim |
| Bir şey bozuldu, kök neden | §4.2 Kök-Neden Kurulu |
| Teslim öncesi | §4.4 Final Kurulu, §13.7 şablon |
| Dışarıdan gelen veri | §11.1 karantina |
| Hata → kalıcı kural | §12 |

3. **Bölüm okurken tamamını bağlama alma.** Belge 1400 satır; grep ile ilgili bölümü çek.

## Sık yapılan hatalar

- **Kurul kurup kör oylatmamak.** Final Kurulu üyeleri ayrı bağlamlarda, eşzamanlı ve birbirinin
  oyunu görmeden oylar. Sıralı oylama çapa etkisi yaratır ve bağımsızlığı yok eder.
- **Doğrulayıcıya gerekçeyi göstermek.** Doğrulayıcı yalnız eseri ve rubriği görür; `STATE.md`'nin
  §5'i (kararlar ve gerekçeleri) ona verilmez.
- **İzolasyonu varsaymak.** Paralel ajanlar aynı dosyaya yazacaksa izolasyon fiilen kurulmalı
  (worktree veya ayrı çıktı dosyası). Kurulmadıysa N=1.
- **Ölçemediğin eşiğe karar bağlamak.** "İlerleme %50" gibi bir eşik ancak alt adım sayısı
  önceden yazılmışsa ölçülebilir. Ölçülemiyorsa o kontrol noktasını atla, uydurma.

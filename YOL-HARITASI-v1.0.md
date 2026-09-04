# BİRLEŞİK AJAN SİSTEMİ — YOL HARİTASI v1.0

Dinamik iş akışları (dynamic workflows) ile döngü mühendisliğinin (loop engineering) iç içe geçtiği, birbirini denetleyen, hatalardan öğrenen ve kendini geliştiren çok-ajanlı sistem.

**Amaç:** Bundan sonra sistem olarak kullanılacak tek referans belge. Tüm kaynak metinler eksiltilmeden tek çatı altında kaynaştırılmış, tekrarlar tek sese indirgenmiş, çelişen hiçbir madde atılmamıştır.

**Kaynak dokusu:** Kişisel tasarım notları (Frk, 03-07-2026) · Shadow Agent spesifikasyonu (WrongStack) · Anthropic "Dynamic Workflows" lansman yazısı · "Seeing like an Agent" (Claude Code mühendislik dersleri) · Loop Engineering makalesi · "Agentic workflows 100x cheaper" (Melbourne Üniversitesi çalışması rehberi) · 25 Claude Projects tekniği · Claude Code Oturum Yönetimi & 1M Bağlam · Fable 5 ile kendini geliştiren sistem (14 adım) · 20 gelir odaklı Claude Code iş akışı · Dynamic Workflows ustalık rehberi (14 adım, 6 desen) · Subagents vs Agent Teams.

**Not:** Ürün/özellik adları ve tarihler kaynak metinlerdeki haliyle korunmuştur; bu alan hızlı değiştiği için kritik uygulamalardan önce güncel resmi dokümantasyonla teyit edin.

---

## KULLANICININ ÇEKİRDEK TALİMATLARI (belgenin türetildiği ham kurallar)

1. Maksimum verim için kaç agentin aynı anda çalışacağına karar veren bir kurul oluşturulsun ve kuruldan çıkan karara göre hareket edilsin.
2. Büyük hedefi küçük, izole alt görevlere ayırın.
3. Sistemin omurgası ve tek doğruluk kaynağı (Single Source of Truth) olsun.
4. Her adımı ilgili uzman alt-ajana verin.
5. Her yeni büyük adımda alt-ajan doğurarak veya sohbeti temizleyerek bağlam şişmesini önleyin.
6. Sana verilen süreye göre akıllıca ve düzgünce sub agentlerin sürelerini dağıtan bir ekstra ajan.
7. Daha sonra verilen süreleri asgari olarak kullandığına dair kontrol eden ayrı bir sub agent.

---

## İÇİNDEKİLER

- Bölüm 0 — Çıkış Noktası ve Sistem Anayasası
- Bölüm 1 — Zihinsel Model: Prompt Mühendisliğinden Döngü Mühendisliğine
- Bölüm 2 — Mimari: Dört Katmanlı Bileşik Yığın ve Model Kademeleri
- Bölüm 3 — Ajan Taksonomisi ve Roller
- Bölüm 4 — Koordinasyon Desenleri: Dinamik İş Akışları (6 desen + kompozisyon)
- Bölüm 5 — Döngünün Yapı Taşları (5+1) ve Otomasyon Katmanı
- Bölüm 6 — Bellek ve Kendini Geliştirme Katmanı
- Bölüm 7 — Bağlam ve Oturum Yönetimi
- Bölüm 8 — Araç ve Aksiyon Alanı Tasarımı
- Bölüm 9 — Maliyet Mühendisliği ve Derlenmiş İş Akışları (100x)
- Bölüm 10 — Claude Projects: Sohbet Tarafındaki Sistem (25 teknik)
- Bölüm 11 — Güvenlik, Denetim ve Sınırlar
- Bölüm 12 — Uygulamalı İş Akışı Kütüphanesi (20 gelir odaklı akış)
- Bölüm 13 — Birleşik Hata Kataloğu (H1–H26)
- Bölüm 14 — Aşamalı Uygulama Yol Haritası (Faz 0–7)
- Ek — Hızlı Sözlük

---

## BÖLÜM 0 — ÇIKIŞ NOKTASI VE SİSTEM ANAYASASI

### 0.1 Temel gözlem ve çekirdek yöntem

Claude Code'a büyük bir iş verildiğinde sona doğru sapıtır (kalite düşer, hedeften sapar). Test edilmiş çözüm — hata payını neredeyse sıfıra indiren beş adımlı çekirdek yöntem:

1. İşi parçalara böl.
2. Bir master doküman oluştur (sistemin omurgası, tek doğruluk kaynağı).
3. Adım adım her işi ayrı bir ajana ver.
4. İşi bitiren ajan master dokümanı güncellesin.
5. Her işi yeni (temiz) bir bağlam penceresinde aç.

Master doküman = Bölüm 6'daki durum dosyası; adım-ajan eşlemesi = Bölüm 3–4'teki delege desenleri; temiz bağlam = Bölüm 7'deki oturum disiplini.

### 0.2 Sistem Anayasası — tasarım maddeleri

- **Madde 1 — Karşılıklı denetim, alan dokunulmazlığı.** Alt-ajanlar birbirini denetler; ancak hiçbir ajan bir diğerinin alanına ve yetkilerine müdahale edemez.
- **Madde 2 — Hatalardan öğrenen dinamik iş akışı.** Sistemin yanında, hatalardan öğrenen ve kendini geliştiren bir dinamik workflow katmanı bulunur; döngü mühendisliği dahildir.
- **Madde 3 — Uzmanlık ve sınırlı yetki.** Her ajanın farklı bir uzmanlığı olacak; yetkileri belirli ve sınırlı olacak.
- **Madde 4 — Yapan ≠ denetleyen.** İşi yapan ile denetleyen aynı ajan olamaz.
- **Madde 5 — Denetleyeni denetleyen.** Denetleyicinin de bir üst denetleyicisi (meta-doğrulayıcı) olacak.
- **Madde 6 — Kurullar.** Sorun çıkan noktalarda kurullar oluşturulur: hataları tespit eden, raporlayan, hatalardan öğrenen ve ilgili ajanlara öğreten ajanlar; durumu tespit edip ilgili yere bildiren ajanlar.
- **Madde 7 — Nihai test.** Zincirin en sonunda mutlaka bağımsız bir test eden ajan bulunur.
- **Madde 8 — Beyin ajanı müdahale hakkı.** Beyin ajanı, bir alt-ajanın görevinde sıkıntı fark ederse alt-ajanı derhal durdurur ve görevi ya kaldığı yerden yeniden delege eder ya da parçalara bölüp 2–3 ajana devreder.
- **Madde 9 — Dinamik + statik karma.** Birbirinden bağımsız çalışan dinamik ajanların yanında, sırayla çalışan statik ajan zincirleri de olacaktır.
- **Madde 10 — Görev tanımı netliği.** Her ajanın görev tanımı belirli olacak; tam olarak neyi çözmesi gerektiği netleştirilecek.
- **Madde 11 — Boşluk-tespit ve planlama ajanı.** Ayrı bir ajan, sistemdeki boşluk noktalarını tespit eder, kendi başına karar alır; gerekirse yeni ajanlar oluşturur veya var olan ajanlara görev dağılımı yaparak planlama yapar.
- **Madde 12 — Karar-destek protokolü #1 (A/B simülasyonu).** İki karar-destek ajanı: biri A senaryosunu, diğeri B senaryosunu simüle eder; karar buna göre verilir.
- **Madde 13 — Karar-destek protokolü #2 (üç perspektif).** Üç ayrı perspektiften bakan ajan devreye sokulur; farklı senaryolar uygulatılır, doğru çözüm takım halinde bulunur.
- **Madde 14 — Karar-destek protokolü #3 (ileri simülasyon).** Test yapmadan önce mevcut akış ileri doğru çalıştırılır ve muhtemel hatalar listelenir (pre-mortem).

### 0.3 Anayasadan mimariye eşleme

| Anayasa maddesi | Bu belgedeki gerçekleme |
|---|---|
| M1 karşılıklı denetim / alan dokunulmazlığı | §3 alt-ajan izolasyonu, §3.6 Gözcü (Shadow), §4 adversarial verification |
| M2 hatalardan öğrenen dinamik workflow | §4 dinamik iş akışları, §6 5-aşamalı bellek + birikimli skill'ler |
| M3 uzmanlık + sınırlı yetki | §3 ajan tanımları (description/tools/model), §5.5 alt-ajan TOML/MD tanımları |
| M4 yapan ≠ denetleyen | §4.2 adversarial verification, §5 /goal (ayrı model puanlar), §6.6 verifier > öz-eleştiri |
| M5 denetleyeni denetleyen | §4.6 deep verification (meta-doğrulayıcı), M6 kurulları |
| M6 kurullar / öğreten ajanlar | §4.6 kök-neden panelleri, §6 ders damıtma → skill'e yazma |
| M7 nihai test | §4 eval deseni, §5 /goal bitiş koşulu, §14 faz çıkış kriterleri |
| M8 Beyin müdahalesi | §3.6 Gözcü hoop komutu + terminate_subagent; yeniden delege / parçalama |
| M9 dinamik + statik karma | §4.1 pipeline() (statik sıra) + agent() dinamik doğuş |
| M10 görev tanımı netliği | §3.1 description = yönlendirme sinyali; §3.8 belirsiz görev = başarısızlık modu |
| M11 boşluk-tespit/planlayıcı | §3.7 rol kaydı; §4 classify-and-act + planner |
| M12–M14 karar protokolleri | §4.4 generate-and-filter, §4.5 tournament, §4.3 fan-out perspektifleri, §4.6 kök-neden |

---

## BÖLÜM 1 — ZİHİNSEL MODEL

### 1.1 Prompt mühendisliği bitti

Gerçek iş Loop Engineering. Bir ajana "landing page yap" demek yerine:

```
Orchestrator hedefi parçalar
  → Uzman (specialist) ajanlar paralel çalışır
    → Doğrulayıcı (verifier) ajan işi kontrol eder
      → Döngü, iş bitene YA DA maliyet/adım limitine ulaşana kadar döner
```

Bu döngülerle bazı insanlar günde 20+ PR atıyor; bazıları sınırsız döngü yüzünden gece 3'te "neden 400$ yaktı bu şey" diye uyanıyor.

### 1.2 Döngü mühendisliği nedir

Ajanı promptlayan kişi olarak kendini sistemle değiştirmektir. Döngü = özyinelemeli bir hedef: amacı tanımlarsın, yapay zekâ tamamlanana kadar yineler.

- Steipete: kodlama ajanlarını promptlamayı bırak; ajanlarını promptlayan döngüler tasarla.
- Boris Cherny (Claude Code ekip lideri): artık Claude'u doğrudan promptlamıyor; Claude'u promptlayan ve ne yapılacağını çözen döngüler çalıştırıyor.

Kavramsal katmanlar: harness mühendisliği ve fabrika modeli bunun kuzenleridir. Döngü mühendisliği harness'ın bir kat üstünde oturur: harness ama zamanlayıcıda çalışır, küçük yardımcılar doğurur, kendi kendini besler.

### 1.3 Tek bağlam penceresinin üç başarısızlık modu

- **Ajan tembelliği (agentic laziness):** Çok parçalı işte kısmi ilerlemeden sonra "bitti" ilan etmek — 50 maddelik incelemenin 20'sini yapıp kalanını "hallettim" saymak.
- **Kendi çıktısını kayırma (self-preferential bias):** Kendi sonuçlarını doğrularken kendine iltimas geçmek. Oyunda payı olan doğrulayıcı adil doğrulayıcı olamaz.
- **Hedef kayması (goal drift):** Çok tur boyunca — özellikle sıkıştırma sonrası — asıl hedefe sadakatin kademeli kaybı. "X yapma" kısıtları 47. turda sessizce kaybolur.

Çözümün yapısı: kendi bağlam pencereleri ve odaklı, izole hedefleri olan ayrı Claude'lar orkestre etmek.

### 1.4 Görev değil, tamamlanma durumu tanımla

```
"bitti"yi sen tanımlarsın
  → Claude oraya nasıl varacağını çözer
  → bitene kadar çalışır
  → kendi hatalarını yakalar
  → teslim eder
```

- ❌ "bana rakip araştırması yaz" → liste alırsın.
- ✅ "Şunlar olmadan durma: her rakibin fiyatlandırması haritalanmış, gerçek yorumlardan en büyük zayıflıkları bulunmuş ve sömürebileceğim 3 boşluk tanımlanmış olacak" → kullanılabilir strateji alırsın.

Çıktı (output) değil, sonuç (outcome). Kanıt ölçeği: Bun, Zig'den Rust'a bu yöntemle yeniden yazıldı — 750.000 satır, %99,8 test uyumluluğu, 11 gün.

### 1.5 Döngü seni sistemden silmez — üç kalıcı sorumluluk

- **Doğrulama hâlâ sende.** Gözetimsiz çalışan döngü, gözetimsiz hata yapan döngüdür. "Bitti" bile iddiadır, kanıt değil.
- **Kavrayış borcu (comprehension debt).** Döngü yazmadığın kodu ne kadar hızlı gönderirse, var olanla anladığın arasındaki boşluk o kadar büyür.
- **Bilişsel teslimiyet (cognitive surrender).** Fikir sahibi olmayı bırakıp geleni almak cazipleşir. Döngüyü muhakemeyle tasarlamak ilaçtır; düşünmekten kaçmak için tasarlamak zehri hızlandırır.

---

## BÖLÜM 2 — MİMARİ: DÖRT KATMANLI BİLEŞİK YIĞIN VE MODEL KADEMELERİ

### 2.1 "Kendini geliştiren" ≠ "kendi kendine öğrenen"

- **Self-learning:** Ajan öğrendiklerine göre kendi ağırlıklarını günceller. Üretimde hiçbir kamuya açık model bunu yapmaz.
- **Self-improving:** Ajanın etrafındaki sistem birikir. Her oturum belleğe ders yazar; skill'ler keskinleşir; durum dosyaları doğrulanmış gerçek biriktirir; eval döngüleri prompt ve rubrikleri rafine eder. Model aynı kalır; koştuğu ortam keskinleşir.

Anthropic mühendislik ekibinin formülasyonu: modeli doğrudan promptlayıp yönlendirmek yerine, modelin ortam geri bildirimine göre kendini düzelttiği döngüler (/goal, Outcomes) tasarlamak ve belleği kendi kendine yönetmesine izin vermek daha iyidir.

### 2.2 Bileşik yığın: dört katman, tek geri besleme döngüsü

| Katman | İçerik | İşlev |
|---|---|---|
| K1 · İlkeller | Model, alt-ajanlar, worktree'ler, araçlar | Etrafında sistem olmayan ham yetenek. Çoğu kullanıcı bugün burada. |
| K2 · Orkestrasyon | /goal ve Outcomes, Dynamic Workflows, Routines | İlkelleri iş akışına çevirir. |
| K3 · Bellek | Durum dosyaları (STATE.md), Skill'ler, bilgi tabanları | Yarınki oturumun sıfırdan başlamak yerine devam etmesini sağlar. |
| K4 · Kendini geliştirme | Görsel öz-kontroller, eval döngüleri, kural damıtma | Ajan kendi çıktısını puanlar, skill'i rafine eder, dersi belleğe geri yazar. Döngü kapanır. |

Bileşme mekanizması: K1'in her çıktısı K4'e akar, orada puanlanır, damıtılır ve K3'e geri yazılır. Model durumsuzdur; etrafındaki sistem değildir.

### 2.4 Model kademelendirme matrisi

| Model | Rol | Ne zaman |
|---|---|---|
| Fable 5 | Orkestratör / Beyin | Günlerce planlama, delegasyon, görüyle iş kontrolü, kural damıtma |
| Opus 4.8 | Zor-ama-sınırlı alt görev + geri düşüş | Mimari kararlar, karmaşık debug, derin inceleme; sınıflandırıcı bloklarında fallback |
| Sonnet 4.6 | Yüksek hacimli işçi | Lint, basit refactor, test iskeleleri, dok güncellemeleri |
| Haiku 4.5 | Puanlayıcı, ucuz sınıflandırıcı | Bağımsız bağlam penceresi, düşük maliyet — doğrulayıcı rolü için ideal |

Üretimde ekonomik kılan desen: orkestratör en üst, işçiler orta, puanlayıcılar ucuz kademe.

---

## BÖLÜM 3 — AJAN TAKSONOMİSİ VE ROLLER

Doğru soru "birden fazla ajan mı kullanmalıyım?" değil, "bu iş hangi tür koordinasyona gerçekten ihtiyaç duyuyor?"

### 3.1 Alt-ajanlar: İzolasyonla paralellik

Her alt-ajan şunları alır: kendi sistem prompt'u; belirli araç seti (M3); temiz izole bağlam penceresi; tek iş.

Bittiğinde ebeveyne yalnızca nihai sonuç döner. **Alt-ajanların asıl amacı paralellik değil sıkıştırmadır (compression):** devasa keşfi temiz sinyale damıtmak.

**Sert kısıtlar:** Alt-ajanlar başka alt-ajan doğuramaz ve birbirleriyle konuşamaz. Her sonuç ebeveyne akar; ebeveyn tek koordinatördür.

`description` alanı yönlendirme sinyalidir; spesifik tut (M10).

### 3.2 Ajan takımları: İletişimle koordinasyon

Üç hareketli parça: takım lideri; takım arkadaşları (her biri kendi bağlam penceresi); paylaşılan görev listesi (bekleyen/devam eden/biten + bağımlılıklar).

`blockedBy` alanı gerçek koordinasyon işidir. Alt-ajanlardan büyük fark: eşler arası doğrudan iletişim.

### 3.3 Çekirdek ayrım

- **Alt-ajan:** at-ve-unut. Görev ver → tamamlar → raporlar. Paylaşılan bellek yok; tek oturumda yaşar ve ölür.
- **Ajan takımı:** işbirlikçi, kalıcı, zamanla bağlam biriktirir.

Seçim kuralı: iş "utanç verecek kadar paralel" ise alt-ajan; sürekli müzakere gerekiyorsa takım.

### 3.4 Bağlam-merkezli ayrıştırma

Çoğu çok-ajanlı tasarım, işi **role göre** böldüğü için başarısız olur (planlayıcı/uygulayıcı/testçi) — her devirde bilginin bozulduğu bir kulaktan kulağa oyunu.

Doğru model: "Bu alt görev hangi bağlama gerçekten ihtiyaç duyuyor?" Örtüşen bilgi = aynı ajan. Bir özelliği uygulayan ajan o özelliğin testlerini de yazmalıdır.

### 3.5 Beş orkestrasyon deseni

1. **Prompt zincirleme** — ardışık adımlar, sıra önemli (M9'un statik tarafı).
2. **Yönlendirme (routing)** — sınıflandırıcı hangi uzmanın alacağına karar verir.
3. **Paralelleştirme** — bağımsız alt görevler eşzamanlı (oylama veya bölümleme).
4. **Orkestratör-işçi** — merkezi ajan parçalar, delege eder, sentezler. Baskın mimari.
5. **Değerlendirici-iyileştirici** — biri üretir, diğeri döngüde değerlendirip geri bildirim verir.

### 3.6 Gözcü Ajan — Shadow Agent tam spesifikasyonu

Filonun arka planda çalışan bekçi köpeği. Kod yazmaz; diğer alt-ajanları izler, anomali yakalar, gerekirse komutla müdahale eder (M1 + M8'in altyapı gerçeklemesi).

- **Filoyu izler:** hangi ajan çalışıyor, hangi görevde, boşta mı, çöktü mü, durdu mu.
- **30 saniyelik heartbeat:** her vuruşta `fleet_status`, `fleet_health`, `mail_inbox` çağırması beklenir.
- **Anomali yakalar:** 5 dakikadan uzun olay üretmeyen takılı ajan; çok hızlı doğup ölen "spike task"lar; sahipsiz atama (orphan assign); mailbox döngüsü; bütçe tükenmesi.
- **Sessiz çalışır:** normalde konuşmaz; problem görünce mailbox üzerinden uyarı yayınlar.
- **Müdahale edebilir:** `hoop <agentId>` veya `hoop all` ile `terminate_subagent`.
- **Durum raporu:** `shadow status` → ajan listesi, heartbeat, son anomaliler, spike geçmişi.
- **Ayar alır:** `shadow mute`, `shadow resume`, `shadow interval <ms>`, `shadow model <model-id>`.

**Kritik nüans:** "asla kendi kendine terminate etme, önce raporla". Shadow otomatik cellat değildir; gözcü + alarm + komutla müdahale eden denetçidir. Sonlandırma yetkisi insana veya Beyin'in açık kararına bağlıdır.

### 3.7 Özel roller kaydı

| Rol | Görev tanımı | Yetki sınırı |
|---|---|---|
| Beyin / Orkestratör | Hedefi parçalar, delege eder, sentezler; sapan alt-ajanı durdurur, yeniden delege eder veya 2–3 ajana böler (M8) | Tam koordinasyon; işçi işi yapmaz |
| Gözcü (Shadow) | Filo izleme, anomali, alarm, komutla müdahale | Kendi başına terminate etmez; önce raporlar |
| Doğrulayıcı | Yapanın çıktısını rubriğe karşı çekişmeli kontrol (M4) | Salt-okur; yalnız rubrik + eser görür |
| Üst-Doğrulayıcı | Doğrulayıcının kaynak/kalitesini denetler (M5) | Salt-okur |
| Kurul (panel) | Hata tespit/raporlama; doğrulayıcı + çürütücü paneli (M6) | Rapor + öneri; uygulama yetkisi yok |
| Öğretmen ajan | Hatalardan ders çıkarır, ilgili ajanlara öğretir (M6) | Skill/bellek yazma |
| Boşluk-Planlayıcı | Boşlukları tespit eder, ajan oluşturur veya görev dağıtır (M11) | Planlama + doğuş; işçi işi yapmaz |
| Nihai Testçi | Zincirin sonunda bağımsız test (M7) | "Geçti" demeden bitiremez |
| Karar-Destek İkilisi | A ve B senaryolarını ayrı ayrı simüle eder (M12) | Salt simülasyon/rapor |
| Perspektif Üçlüsü | 3 yaklaşımı 3 perspektiften işler (M13) | Salt analiz |
| Ön-Simülatör | Testten önce akışı ileri çalıştırıp hataları listeler (M14) | Salt-okur analiz |
| Karantina Okuyucu | Güvenilmeyen içeriği okur; yüksek yetkili eylem alamaz | Salt-okur, izole |

### 3.8 Ne zaman çok-ajan KULLANMA + başarısızlık modları

Çok-ajan maliyetini üç durumda hak eder: **bağlam koruması**; **gerçek paralelleştirme**; **uzmanlaşma** (çelişen sistem prompt'ları veya araç kalabalığı).

Yanlış çağrıdır: ajanlar sürekli bağlam paylaşmak zorundaysa; bağımlılıklar yürütme değerinden fazla yük yaratıyorsa; iş tek ajanın halledeceği kadar basitse.

**Kodlamaya özel uyarı:** Paralel kod yazan ajanlar uyumsuz varsayımlar yapar. Kodlamada alt-ajanlar soru yanıtlamalı ve keşfetmeli, eşzamanlı kod yazmamalı.

Üç başarısızlık modu:
1. **Belirsiz görev tanımları** → ajanlar birbirinin işini kopyalar. Her ajana net hedef, çıktı formatı, araç rehberi, kapsam dışı sınırlar (M10).
2. **Doğrulama ajanları doğrulamadan zafer ilan eder** → "tam test paketini çalıştır, şu vakaları kapsa, her biri geçmeden tamamlandı işaretleme."
3. **Token maliyeti hızla bileşir** → modelleri kademelendir, rutini ucuza yönlendir, kaçamayacak bütçe kontrolleri kur.

**Tek tasarım ilkesi:** Rol veya organizasyon şemasına göre değil, bağlam sınırlarına göre tasarla. Tek ajanla başla, kırıldığı yeri bul.

---

## BÖLÜM 4 — KOORDİNASYON DESENLERİ: DİNAMİK İŞ AKIŞLARI

### 4.1 Dinamik iş akışı = Claude'un kendi yazdığı harness

Varsayılan harness'ın yapamadığı üç şey:
- **Ajan başına izolasyon:** her alt-ajan tek odaklı hedefle kendi bağlam penceresini alır.
- **Ajan başına model seçimi:** zor akıl yürütmeye üst kademe, ucuz keşfe hızlı model.
- **Ajan başına izolasyon seviyesi:** worktree (izole git checkout) veya remote.

Başlatma: "make a workflow that…" veya tetik kelime `ultracode`.

**Statik vs dinamik:** Statikler her uç durumu karşılamak zorunda olduğundan jeneriktir. Dinamik sürüm kendini senin bağlamına göre şekillendirir.

### 4.2 Çekirdek API

- `agent(prompt, opts)` — tek alt-ajan doğurur (model, şema, izolasyon seçilebilir).
- `parallel([...])` — **bariyerdir:** dağıtır, sonra dönmeden önce hepsini bekler.
- `pipeline(...)` — **akıştır:** her öğe her aşamadan bağımsız akar.

Seçim sorusu: "Bir sonraki adımı atmadan önce TÜM sonuçlara ihtiyacım var mı?" Evet → parallel. Hayır → pipeline.

### 4.3 Altı desen

**Desen 1 — Classify-and-act.** Sınıflandırıcı görev türüne karar verir; akış cevaba göre yönlendirir. Pahalı modeli yalnız karmaşıklığın gerektirdiği yerde harca.

**Desen 2 — Fan-out-and-synthesize.** Görevi küçük adımlara böl; paralel ajan çalıştır; sonuçları tek cevapta sentezle. Sentez adımı bariyerdir. Kullan: net sayılabilir iş listesi varsa, öğeler bağımsızsa, sonda tek konsolide cevap istiyorsan.

**Desen 3 — Adversarial verification.** Kendini-kayırmanın yapısal çözümü (M4). Doğan her ajan için, çıktısını rubriğe karşı çekişmeli doğrulayan ayrı ajan çalıştır. **Eşleştirme kuralı:** Doğrulayıcı yalnızca rubriği ve eseri bilmeli, kimin ürettiğini değil.

**Desen 4 — Generate-and-filter.** Çok fikir üret; rubrikle filtrele; kopyaları ayıkla; yalnız en iyileri döndür. En iyi cevabı istemek erken bağlanma yaratır; üret-ve-filtrele geç bağlanma sağlar (M13'ün doğal aracı).

**Desen 5 — Tournament.** Ajanları yarıştır; ikili (pairwise) kıyasla. Karşılaştırmalı yargı mutlak puanlamadan güvenilirdir. Braket deterministik kodda yaşar, bağlamda değil.

**Desen 6 — Loop until done.** Sabit geçiş sayısı yerine durma koşulu sağlanana kadar ajan doğurmaya devam et. /goal ile sert bitiş, /loop ile tempo.

Kendini geliştiren sistemlerde en çok üçü yerini hak eder: fan-out-sentez, çekişmeli doğrulama, bitene-kadar-döngü.

### 4.4 Kompozisyon matrisi

| Kullanım alanı | Desen bileşimi |
|---|---|
| Migrasyon / refactor | Fan-out (worktree'de ajan başına düzeltme) → çekişmeli inceleme → merge → bitene-kadar-döngü |
| Derin araştırma | Aramaları fan-out → kaynakları çek → iddiaları çekişmeli doğrula → atıflı rapor sentezle |
| Derin doğrulama | İddiaları çıkar → her iddiaya doğrulayıcı → **meta-doğrulayıcı kaynağın kalitesini denetler (M5)** |
| Sıralama (1000+ öğe) | Turnuva: ikili kıyas hattı. Asla mutlak skor değil. |
| Bellek/kural uyumu | Kural başına doğrulayıcı; şüpheci persona sahte pozitifleri azaltır |
| Kök-neden araştırması | Ayrık kanıttan hipotez üreten ajanlar → her hipotez doğrulayıcı + çürütücü panelinin (kurul, M6) önüne → biri sağ kalana kadar döngü |
| Ölçekli triyaj | Sınıflandır → kopya ayıkla → düzelt veya insana eskale; karantinayla eşle |
| Keşif ve zevk | Çözüm keşfet; inceleyiciye "iyi çözüm neye benzer" rubriği ver |
| Eval'lar | Worktree'de aday üret → rubriğe karşı puanla → rafine et, yeniden puanla |
| Model yönlendirme | Sınıflandırıcı hangi modelin kullanılacağına karar verir |

**İçselleştirme yolu:** Kayma → fan-out. Kendini-kayırma → çekişmeli doğrulama. Ucu açık → bitene-kadar-döngü. Puanlaması zor → turnuva.

### 4.6 Ne zaman KULLANMA + ipuçları

- İş akışları önemli ölçüde daha fazla token kullanabilir. "Bu iş gerçekten daha fazla hesaplamaya ihtiyaç duyuyor mu?" Normal oturum 5 dakikada bitirecekse gerek yok.
- "quick workflow" isteyebilirsin — bir varsayımın hızlı çekişmeli incelemesi.
- /goal + /loop ile birleştir.
- **Token bütçesi:** Prompt'ta açıkça belirt — "use 10k tokens" tavanı koyar. Bütçesiz iddialı akış beklediğinin 5–10 katına şişer.

### 4.7 Kaydetme ve paylaşma

Çalışan iş akışını kaydet (`~/.claude/workflows`). Skill olarak dağıtırken Claude'a akışı **birebir çalıştırılacak betik değil, şablon** olarak görmesini söyle.

### 4.8 Karantina deseni (güvenilmeyen girdi)

Güvenilmeyen kamu içeriği okuyan her akış prompt injection barındırabileceğini varsaymalıdır. Güvenilmeyen içeriği okuyan ajanları her türlü yüksek yetkili eylemden men et; ham içeriğe hiç maruz kalmamış ayrı ajanlar eylemi yapsın.

**Kural:** girdi sen veya güvendiğin bir ekip arkadaşınca yazılmadıysa karantinala. 30 satırlık salt-okur okuyucu ajan neredeyse bedavadır ve koca bir risk sınıfını kaldırır.

---

## BÖLÜM 5 — DÖNGÜNÜN YAPI TAŞLARI (5+1)

### 5.1 Otomasyonlar — döngünün kalp atışı

Zamanlamayla tetiklenip keşif ve triyaj yaparlar. Bir şey bulan koşular gelen kutusuna gider; bulmayanlar kendini arşivler.

**/goal vs /loop vs Outcomes:**
- `/loop` bir tempoda yeniden çalıştırır (cadence).
- `/goal` yazdığın koşul doğru olana kadar devam eder; her turdan sonra **ayrı küçük bir model** bitip bitmediğini kontrol eder — kodu yazan ajan, notunu veren ajan değildir. /goal, yapan/denetleyen ayrımının durma koşuluna uygulanmış halidir (M4 + M7).
- `Outcomes` — dosya-tabanlı rubrik, alt-ajan puanlayıcı, sert `max_iterations` sınırı. Saatler/günler süren işler için.

### 5.2 Worktree'ler — paralellik kaosa dönmesin

Aynı dosyaya yazan iki ajan, aynı satırlara commit eden iki mühendisle aynı baş ağrısıdır. Git worktree çözer.

Kendini geliştiren sistemlerde worktree opsiyonel değildir: (a) yapan A'da yazar, doğrulayıcı B'de okur; (b) paralel yapısal deneyler her biri kendi worktree'sinde; (c) günler süren koşularda checkpoint.

**Orkestrasyon vergisi:** Worktree mekanik çarpışmayı kaldırır ama tavan hâlâ sensin — kaç paraleli çalıştırabileceğini araç değil, **senin inceleme bant genişliğin** belirler.

### 5.3 Skill'ler

Skill = SKILL.md içeren klasör; talimat + metadata + opsiyonel betikler. Skill'ler **niyet borcunun (intent debt)** kesildiği yerdir: ajan her oturuma soğuk başlar ve niyetindeki her boşluğu kendinden emin bir tahminle doldurur.

Skill'siz döngü tüm projeyi her turda sıfırdan türetir; skill'li döngü birikir. Ayrım: skill = yazım formatı, plugin = dağıtım biçimi.

### 5.4 Plugin'ler ve bağlayıcılar (MCP)

Yalnızca dosya sistemini görebilen döngü küçücük bir döngüdür. MCP bağlayıcıları ajanın issue tracker okumasını, veritabanı sorgulamasını, Slack'e mesaj bırakmasını sağlar. Fark: "işte düzeltme" diyen ajan ile PR'ı açan, bileti bağlayan ve CI yeşile dönünce ping atan döngü.

### 5.5 Alt-ajanlar — yapanı denetleyenden uzak tut

Döngüdeki açık ara en faydalı yapısal şey. Kodu yazan model kendi ödevine not verirken fazla naziktir. Alışıldık bölünme: biri keşfeder, biri uygular, biri spesifikasyona karşı doğrular.

**Döngü sen bakmıyorken döner — gerçekten güvendiğin bir doğrulayıcı, uzaklaşabilmenin tek nedenidir.**

### 5.6 Bellek — altıncı parça, omurga

Model koşular arasında her şeyi unutur, o yüzden bellek diskte olmalı, bağlamda değil. **Ajan unutur; repo unutmaz.**

### 5.7 Bir döngünün anatomisi

1. Sabah otomasyonu her gün çalışır; triyaj skill'ini çağırır; bulguları markdown dosyasına yazar.
2. Her bulgu için izole worktree açılır, düzeltme taslağı için alt-ajan gönderilir; ikinci alt-ajan taslağı skill'lere ve testlere karşı inceler.
3. Bağlayıcılar PR açar, bileti günceller. Halledilemeyen her şey triyaj gelen kutusuna (insana) düşer.
4. Durum dosyası omurgadır: ne denendi, ne geçti, ne açık.

### 5.8 Routines — laptop kapalı, günlerce orkestrasyon

Kaydedilmiş konfigürasyonlar bir tetikleyiciyle bulut altyapısında çalışır. Üç tetikleyici tipi:
- **Zamanlama** — sabah brifingi: dünkü eval paketini yeniden koş, yeni başarısızlık modlarını skill'lere damıt.
- **API** — olayla ateşle: CI düştü → araştırma; alarm → triyaj.
- **GitHub olayı** — PR açıldığında değerlendirme; merge'de yeni desenleri skill'e geri yaz.

---

## BÖLÜM 6 — BELLEK VE KENDİNİ GELİŞTİRME KATMANI

### 6.1 Beş aşamalı bellek ilerlemesi

1. **Fail** — Ajan bir şeyi yanlış yapar ve başarısızlığı sonra işe yarayacak ayrıntıyla belgeler.
2. **Investigate** — Devam etmeden önce nedenini çözer.
3. **Verify** — Teşhisi tahmin değil, kontrol edilmiş gerçeğe çevirir.
4. **Distill** — Doğrulamayı, özgül vakanın ötesine geçen genel kurala dönüştürür.
5. **Consult** — Sonraki görevde gerçeği sıfırdan türetmek yerine kuralı okur.

Ölçülmüş fark: zayıf model 1. aşamada çıkar (doğrulanmamış tahminler listesi, bileşmez); orta model 3. aşamada çıkar (doğrulama kapsamı %7–33); güçlü model ilerlemeyi tamamlar (doğrulama kapsamı %73'e ulaşır ve genel kurallara damıtır).

### 6.2 Durum dosyası (STATE.md)

Beş bölüm, beş aşamaya karşılık gelir:

```
## Doğrulanmış gerçekler        # aşama 3 — bunlar hakkında tahmin etmeyi bırak
## Genel kurallar               # aşama 4 — yeniden türetmeden önce danış
## Açık başarısızlıklar         # aşama 1 → 2 (yeniden üretim adımlarıyla)
## Öğrenilen dersler            # aşama 4 damıtmaları
## Son oturum                   # aşama 5 — devam et, yeniden başlama
```

İki operasyonel kural:
1. **Uzaklaşmadan önce yaz.** Her oturum STATE.md güncellemesiyle biter. Oturum yazmayla bitmezse sıradaki sıfırdan başlar.
2. **Oturum başında oku.** Bunsuz, güçlü modelde bile zayıf-model bellek davranışı ortaya çıkar.

### 6.3 Bileşen skill'ler — dersi sohbete değil, skill'in içine yaz

STATE.md proje belleği içindir; skill'ler prosedürel bellek içindir. **Önemsiz olmayan her başarısızlıktan sonra dersi skill'in kendisine yaz.**

İki haftadır bileşen bir skill'de yeni bölümler belirir: bilinen başarısızlık modları, post-mortem kuralları, üretimde gözlenen anti-desenler.

Örnek anti-desen bölümü:
```
- CI'ı yeşile çevirmek için düşen testi asla devre dışı bırakma. Kaydet.
- .github/workflows/ altını insan onayı olmadan asla değiştirme.
- src/payments/ altına güvenlik incelemesi olmadan dokunma.
```

**Bileşim sözleşmesi:** Onaylanan her ders skill'e gider, sadece STATE.md'ye değil. STATE.md projeyle ölür; skill'ler seninle taşınır.

### 6.4 Görüyle öz-doğrulama

1. Yapan alt-ajan UI kodunu yazar; sonucu ekran görüntüsüne render eder.
2. Doğrulayıcı alt-ajan görüntüyü görüyle okur; hedef tanımına, tasarım token'larına ve önceki görüntüye karşı kıyaslar.
3. Karar döngüye döner: eşleşme → tamamlandı; uyumsuzluk → boşluğu tarif eder, yapılandırılmış diff ile yapana geri verir.

### 6.5 Doğrulayıcı alt-ajan öz-eleştiriyi yener

Mekanizma "daha çok çabalamak" değil, yapısaldır: kendi çıktısını değerlendiren model kendi akıl yürütme izini görür ve zaten yazdığıyla tutarlı sonuçları tercih eder. Ayrı model yalnızca eseri ve rubriği görür — **doğrulayıcının, yapanın oyununda payı yoktur.**

Ölçülen sonuç: bağımsız doğrulayıcılı model ~6 kat daha fazla iyileşme çıkardı; daha büyük yapısal değişiklikler yaptı ve olumsuz ara sonuçlardan toparlandı. Doğrulayıcısız aynı model, ilk "yeterince iyi"nin ötesine zorlanacak hiçbir şeye sahip değildir.

---

## BÖLÜM 7 — BAĞLAM VE OTURUM YÖNETİMİ

### 7.1 Kısa el kitabı

- **Bağlam penceresi:** Modelin bir yanıt üretirken aynı anda görebildiği her şey.
- **Bağlam çürümesi (context rot):** Bağlam büyüdükçe performansın düşmesi — dikkat daha çok token'a yayılır. 1M modelde bir düzeyde çürüme ~300–400k token civarında görülür; göreve bağlıdır, katı kural değildir.
- **Sıkıştırma (compaction):** Pencere sonu yaklaşınca işi daha küçük bir tarife özetleyip devam etmek.

### 7.2 Her tur bir dallanma noktasıdır — beş seçenek

1. **Devam et** — aynı oturumda yeni mesaj.
2. **/rewind (esc esc)** — önceki bir mesaja atla; sonrasındaki mesajlar bağlamdan düşer.
3. **/clear** — yeni oturum, kısa bir briefle.
4. **Compact** — oturumu özetle, özetin üstünde devam et.
5. **Alt-ajanlar** — iş parçasını temiz bağlamı olan ajana delege et; yalnız sonucu geri çek.

### 7.3 Ne zaman yeni oturum

Genel kural: yeni göreve başlarken yeni oturum. Modelin bağlamı bitmedi diye devam etmen gerekmez.

### 7.4 Düzeltmek yerine geri sar (rewind)

Tek bir alışkanlık göstergesi seçilecekse: rewind. Claude beş dosya okur, bir yaklaşım dener, çalışmaz — içgüdün "olmadı, X'i dene" yazmaktır; **daha iyi hamle, dosya okumalarının hemen sonrasına geri sarıp öğrendiklerinle yeniden promptlamak.** Başarısız denemenin gürültüsü bağlamda hiç yer kaplamaz.

Ayrıca "summarize from here": Claude öğrendiklerini özetleyip bir devir mesajı yazar.

### 7.5 Compact vs /clear

- **Compact:** Model özetler, geçmişi özetle değiştirir. Kayıplıdır — neyin önemli olduğuna Claude karar verir. Yönlendirebilirsin: `/compact focus on X, drop Y`.
- **/clear:** Önemli olanı sen yazarsın ve temiz başlarsın. Daha çok emek; ama ortaya çıkan bağlam senin ilgili saydığındır.

**Kötü compact neden olur:** Model işin gideceği yönü tahmin edemediğinde. Özellikle zor, çünkü bağlam çürümesi yüzünden **model tam sıkıştırma anında en az zeki noktasındadır.**

### 7.6 Alt-ajanlar bağlam yönetimi aracıdır

Zihinsel test: "Bu araç çıktısına yine ihtiyacım olacak mı, yoksa sadece sonuca mı?" Sadece sonuç → alt-ajan.

---

## BÖLÜM 8 — ARAÇ VE AKSİYON ALANI TASARIMI ("AJAN GİBİ GÖRMEK")

**Çerçeve:** Kendini modelin yerine koy — zor bir matematik problemi verildi; hangi araçları isterdin? Kâğıt asgaridir; hesap makinesi daha iyi ama fonksiyonları bilmen gerekir; bilgisayar en güçlüsü ama kod yazmayı bilmelisin. **Ajana kendi yeteneklerine göre şekillenmiş araçlar ver.**

### 8.1 AskUserQuestion aracı

Üç deneme: (a) ExitPlanTool'a parametre eklemek — Claude'u karıştırdı; (b) çıktı formatını değiştirmek — garanti yoktu; (c) ayrı araç — yapılandırılmış çıktı + çoklu seçenek garantisi. **En önemlisi: Claude bu aracı çağırmayı sevdi.** En iyi tasarlanmış araç bile Claude nasıl çağıracağını anlamazsa çalışmaz.

### 8.2 Yetenekle birlikte güncelle — Todos → Tasks

Modeller geliştikçe hatırlatmaya ihtiyaç kalmadığı gibi hatırlatma **sınırlayıcı** oldu. TodoWrite, Task Tool ile değiştirildi: Todo'lar modeli rayda tutmakla ilgiliyken Tasks ajanların birbiriyle iletişimiyle ilgilidir.

**Ders:** Model yetenekleri arttıkça bir zamanlar gereken araçlar artık kısıtlıyor olabilir; önceki varsayımları sürekli yeniden ziyaret et.

### 8.3 RAG'den progresif ifşaya

İlk sürüm bağlamı RAG ile buluyordu — güçlüydü ama bağlam Claude'a **veriliyordu**, Claude kendisi bulmuyordu. Grep ile kendi bağlamını kurmaya başladı.

**Desen:** Claude zekileştikçe, doğru araçlar verilirse kendi bağlamını kurmakta giderek iyileşir. Progresif ifşa artık araç eklemeden işlevsellik eklemenin standart tekniğidir.

### 8.4 Araç eklemeden yetenek

Yeni araç ekleme çıtası yüksek — her araç modele düşünülecek bir seçenek daha. Çözüm: dokümanları iyi arayan bir rehber alt-ajan; aksiyon alanına araç eklemeden ekleme yapıldı.

### 8.5 Bilim değil sanat

Katı kural seti yok. Sık deney yap, çıktılarını oku. **Ajan gibi gör.**

---

## BÖLÜM 9 — MALİYET MÜHENDİSLİĞİ VE DERLENMİŞ İŞ AKIŞLARI

Üç alanda 128x, 296x ve 462x daha ucuz; kalitenin %87–98'i korunarak.

### 9.1 Üç barınma yeri

- **A · Orkestrasyon:** yazılım her turda talimat enjekte eder. $0.05–0.17 / konuşma.
- **B · Bağlam-içi:** tüm akışı sistem prompt'una yapıştırırsın. En pahalısı: $0.10–0.33 / konuşma.
- **C · Derlenmiş:** prosedürü küçük bir modele bir kez öğretir, kendin barındırırsın. $0.0003–0.001 / konuşma.

**Alınacak tek fikir:** İş akışının şekli konuşmadan konuşmaya değişmiyorsa, onu her seferinde tarif etmek için neden ödeyesin?

### 9.2 Dört aşama

1. **İş akışını akış şeması olarak çiz** (procedure.json). Ajan/müşteri turları dönüşümlü; her bitiş üç türden biri (başarı / vazgeçti / insana devredildi); her ajan adımı tek seferde tek şey sorsun. Basit akışlar 14 kutu, en karmaşığı 55 kutu / 6 dallanma.
2. **Zeki bir modele binlerce pratik konuşma yaptır (~$40).** 2000–6000 örnek. Bitmiş örnekler tamamen doğal diyalog okunur; akış şeması etiketleri hiç görünmez.
3. **Küçük modeli eğit ($10–40, 1 GPU).** Qwen2.5-3B (basit) / Qwen3-8B (karmaşık); lr 2e-5; 10–20 geçiş; en iyi sürümü held-out skoruyla sakla. **TAM eğitim şart, LoRA DEĞİL** — kısayol çok adımlı prosedürleri öğrenmekte başarısız oldu.
4. **Aç: orkestratör tamamen yok.** vLLM ile self-host; prompt boyutu sabit; yönlendirme hataları tasarım gereği ortadan kalkar.

**Veri üretiminde tuzak:** Basit rastgele yürüyüş kısa "vazgeçti/eskale" rotalarını aşırı-örnekler; tüm yolları dengeli enumerate et.

### 9.3 Tutuyor mu?

Kör AI puanlayıcı (ikinci puanlayıcıyla çapraz kontrol): doğallık %97, zarif hata idaresi %92, görev başarısı %91, bilgi doğruluğu %87. Test edilen üç akışın ikisinde derlenmiş model orkestratör sürümünden **daha az** başarısız oldu.

Başabaş 500 konuşma içinde gelir. Kurulum ~$50–80; prosedür değişirse yenileme 30–50 dakika.

### 9.4 Sana göre mi?

**Güçlü uyum:** prosedürel akış; kararlı prosedür; amorti edecek hacim; gizlilik; ölçekte gecikme/maliyet önemli.
**Zayıf uyum:** ucu açık iş; geniş dünya bilgisi gerektiren başarı (%87 en zayıf alan); mutlak en yüksek kalite şartı; sürekli değişen prosedür; GPU/beceri yokluğu.

---

## BÖLÜM 10 — CLAUDE PROJECTS: SOHBET TARAFI (25 TEKNİK)

**Kurulum (01–07):** 01 Project Instructions = kalıcı sistem prompt'u · 02 Yapılandırılmış talimat şablonu (ROLE / CONTEXT / RULES / OUTPUT DEFAULTS) · 03 Bilgi tabanı yüklemesi · 04 Stratejik dosya adlandırma (doc1.pdf sinyal vermez) · 05 Yaşayan talimatlar deseni (haftalık rafine) · 06 Alan başına ayrı Project · 07 Başlangıç kalibrasyon konuşması (15 dk, haftalarca vasat çıktıyı önler).

**Günlük iş akışları (08–14):** 08 Bağlam-zengin çıplak soru (%90 daha az kelime) · 09 Konuşma zinciri · 10 Araştırma biriktirici · 11 Şablon üretici · 12 Karar çerçevesi (üç perspektif — M12–M13'ün sohbet karşılığı) · 13 Toplantı hazırlık sistemi · 14 Kalite denetimi / meta-optimizasyon (çelişen talimat, bayat dosya, boşluk tespiti).

**İleri teknikler (15–21):** 15 Ses kalibrasyon dosyası (örnekler soyut sıfatlardan iyidir) · 16 Rekabet istihbaratı merkezi · 17 Müşteriye özel Project'ler · 18 SOP kurucu · 19 Geri bildirim döngüsü kaydedici (M2/M6'nın sohbet döngüsü) · 20 Project'ler arası sentezleyici · 21 Mevsimsel tazeleme (bağlam kaymasını önler).

**Güç kullanıcı sırları (22–25):** 22 Talimat öncelik sistemi (CRITICAL / STANDARD / PREFERENCES — önceliksiz Claude küçük bir tercihi tatmin için kritik kuralı çiğneyebilir) · 23 Persona değiştirme · 24 Kıyas (benchmark) konuşması · 25 Bileşik bilgi stratejisi.

---

## BÖLÜM 11 — GÜVENLİK, DENETİM VE SINIRLAR

### 11.1 Karantina
Güvenilmeyen içerik okuyan ajan ≠ eylem alan ajan. Tam kural seti §4.8; denetim altyapısı §3.6.

### 11.2 Güvenlik sınırı — modelin yapmayacakları ve etrafından tasarım
Üst kademe model belirli yüksek riskli alanlarda (siber güvenlik zafiyet araştırması, biyoloji, kimya, model damıtma) yanıt vermeyi reddeder ve bir alt kademeye geri düşer. **Bu dokümantedir; bug değildir.**

- Sistemin güvenlik araçlarına dokunuyorsa sınıflandırıcı blokları bekle; geri düşüş için mimari kur.
- Sınıflandırıcı geniştir: bilimsel hesaplama akışı veya kripto ilkellerinin kod incelemesi tetikleyebilir.
- **Skill'lerini geri düşüşü zarifçe yüzeye çıkaracak şekilde tasarla.** Sınıflandırıcı bloğunda sessizce düşen döngü, gerçek hatada düşen döngüyle birebir aynı görünür.
- Sistem kartını denetle; üretime almadan önce oku.

**Genel ilke:** Güvenlik sınırını başarısızlık modu olarak değil, **bilinen bir geri düşüş** olarak ele al.

### 11.3 Maliyet ve veri sınırları
- **Sınırsız döngü riski:** durma koşulu/adım limiti/token bütçesi olmayan döngü = gece 3'te 400$ faturası.
- **Saklama politikası:** Hassas veriyi saklama şartlarını kontrol etmeden bir rutinden geçirmek sessizce uyum sorunu yaratır.
- **İnsan üçlüsü:** Doğrulama sende kalır; kavrayış borcunu ödemek için üretileni oku; bilişsel teslimiyete karşı fikir sahibi kal.

---

## BÖLÜM 12 — UYGULAMALI İŞ AKIŞI KÜTÜPHANESİ (20 AKIŞ)

Kullanım çerçevesi: tamamlanma durumu dili + otonom operatör modeli (hedef koy, uzaklaş, bitmiş işe dön; bebek bakıcılığı yok). Basit görevleri ucuz modellere yönlendir.

**İş geliştirme (1–5):** Google Maps lead'leri · isabetli soğuk e-posta · rakip istihbaratı · ölçekte affiliate içerik · fiyat sayfası düzeltmesi.
**Pazarlama (6–10):** viral hook veritabanı · reklam hesabı otopsisi · 5k yorum → ürün yol haritası · onboarding kaçış analizi · rakip mesaj boşlukları.
**İçerik (11–15):** farkındalık aşamasına göre UGC · landing page araştırması · 30 günlük içerik takvimi · 10 YouTube senaryosu · haftalık bülten.
**Araştırma ve strateji (16–20):** pazar araştırma raporu · şirket due diligence · fiyatlandırma stratejisi · SEO fırsatları · fikir doğrulama.

**Başlarken:** Haftanın saatlerini yiyen tek bir akışı seç ve tamamlanma durumu olarak yeniden yaz.

---

## BÖLÜM 13 — BİRLEŞİK HATA KATALOĞU (H1–H26)

### 13.1 Mimari ve model seçimi
- **H1** · "Kendini geliştiren"i "kendi kendine öğrenen" sanmak → iyileşme etraftaki sistemdedir, modelde değil.
- **H2** · Her adımı en üst kademede koşturmak → model kademelendirme matrisi.
- **H3** · Güvenlik sınırını hesaba katmamak → sessizce düşen döngü; açık fallback kur, sistem kartını oku.

### 13.2 Bellek ve bileşme
- **H4** · Uzaklaşmadan önce yazmamak → sıradaki oturum sıfırdan başlar.
- **H5** · Oturum başında okumamak → güçlü modelde bile zayıf-model bellek davranışı.
- **H6** · Dersi sohbete yazıp skill'e yazmamak → proje ölünce ders ölür.
- **H7** · Aşamada takılıp kalmak (Investigate/Verify atlamak) → doğrulanmamış tahminler listesi, bileşmez.

### 13.3 Doğrulama ve kalite
- **H8** · Yapanın kendini doğrulaması → ayrı doğrulayıcı; yalnız rubrik + eser görür. ~6x daha fazla iyileşme.
- **H9** · Doğrulayıcının doğrulamadan zafer ilan etmesi → sahte pozitif; somut onay kriteri şart.
- **H10** · Meta-doğrulayıcı yokluğu → denetleyeni denetleyen yok (M5 ihlali).

### 13.4 Bağlam ve oturum
- **H11** · Hedef kayması, özellikle compact sonrası → proaktif yönlendirilmiş compact veya clear + brief.
- **H12** · Kötü autocompact → `/compact focus on X, drop Y`; ya da rewind + "summarize from here".
- **H13** · Düzeltmeyi rewind yerine ileri promptlama → başarısız denemenin gürültüsü bağlamı kirletir.
- **H14** · Bağlam çürümesini yok saymak → yeni görevde yeni oturum; alt-ajanla ara çıktıyı izole et.

### 13.5 Çok-ajan ve koordinasyon
- **H15** · Gereksiz yere çok-ajana uzanmak → tek ajanla başla, kırıldığı yeri bul.
- **H16** · Role göre bölme (kulaktan kulağa oyunu) → bağlam-merkezli ayrıştırma.
- **H17** · Belirsiz görev tanımları → ajanlar birbirinin işini kopyalar (M10 ihlali).
- **H18** · Paralel kod yazan ajanlar → uyumsuz varsayımlar, zor ayıklanan çatışmalar.
- **H19** · `parallel()` ve `pipeline()` karıştırmak → gereksiz bekleme veya eksik veri.

### 13.6 Maliyet ve otomasyon
- **H20** · Sınırsız döngü → /goal ile sert bitiş, token tavanı, kaçamayacak bütçe kontrolü.
- **H21** · İş akışını gereksiz kullanmak → 5 dakikalık iş için 5-panelli inceleme; token 5–10x şişer.
- **H22** · Derlemede LoRA kullanmak → çok adımlı prosedürü öğrenemez.
- **H23** · Rastgele yürüyüşle veri üretmek → bitiş dağılımı bozulur.

### 13.7 Güvenlik ve girdi
- **H24** · Güvenilmeyen içeriği yetkili ajana okutmak → karantina; okuyucu salt-okur, eylemi ayrı ajan yapar.
- **H25** · Gözcünün kendi başına terminate etmesi → önce raporla; sonlandırma insan/Beyin kararına bağlı.
- **H26** · Saklama/uyum sınırını atlamak → devreye almadan önce saklama politikasını incele.

---

## BÖLÜM 14 — AŞAMALI UYGULAMA YOL HARİTASI (FAZ 0–7)

Altın kural her fazda geçerli: **tek ajanla başla, kırıldığı yeri bul, o kırılma noktasının söylediği tek parçayı ekle.** Fazları sırayla yürü; bir sonrakine ancak mevcut fazın bitiş koşulu sağlandığında geç.

- **Faz 0 — Kırılma noktasını bul.** Gerçek bir işi tek oturumda koştur; nerede kırıldığını not et (kayma / tembellik / kendini kayırma). *Bitiş:* somut kırılma noktası belgelenmiş.
- **Faz 1 — Bellek omurgası.** STATE.md (5 bölüm); iki operasyonel kuralı alışkanlığa çevir; ilk skill; ilk Project. *Bitiş:* iki ardışık oturum, ikincisi STATE.md okuyarak devam etmiş. **Yarın eklenecek tek parça: STATE.md.**
- **Faz 2 — Yapan/denetleyen ayrımı.** İlk /goal koşusu; ilk ayrı doğrulayıcı alt-ajan; worktree izolasyonu. *Bitiş:* en az bir iş yazan + ayrı doğrulayıcıyla tamamlanmış. **Yarın eklenecek tek parça: Verifier — ~6x farkı yaratan tek yapısal hamle.**
- **Faz 3 — Desen kütüphanesi.** İlk dinamik iş akışı; ilk üç deseni gerçek işe uygula; parallel/pipeline ayrımı; worktree standardı; akışı kaydet. *Bitiş:* en az iki desen gerçek işte kullanılmış.
- **Faz 4 — Otomasyon katmanı.** Zamanlamayla tetiklenen triyaj; /loop + /goal; MCP bağlayıcıları; Routines; uçtan uca döngü anatomisi. *Bitiş:* en az bir otomasyon insan tetiği olmadan bulgu üretiyor. **Yarın eklenecek tek parça: görüyle öz-doğrulama.**
- **Faz 5 — Kendini geliştirme disiplini.** 5 aşamalı belleği tam işlet; bileşen skill disiplini; görüyle öz-doğrulama; eval paketi; doğrulayıcı > öz-eleştiri. *Bitiş:* skill gözle görülür büyümüş, eval düzenli koşuyor, bileşme belgelenebiliyor.
- **Faz 6 — Yönetişim.** Gözcü/Shadow; kurullar; Boşluk-Planlayıcı; Beyin müdahale hakkı; meta-doğrulayıcı; karantina zorunlu; güvenlik sınırı belgeli. *Bitiş:* Gözcü en az bir anomali raporladı; bir kurul bir sorunu çözdü.
- **Faz 7 — Ölçek.** Model yönlendirmesini otomatikleştir; token bütçelerini standartlaştır; kararlı yüksek-hacimli akışları derle; başabaş hesabı; kör puanlayıcıyla kalite/maliyet ölçümü. *Bitiş:* en az bir akış derlenmiş ve %87+ kalite eşiğini geçiyor.

### 14.2 Bir cümlelik özet

Tek ajanla başla; kırıldığı yeri bul; STATE.md ekle; yapanı denetleyenden ayır; başarısızlık moduna göre desen seç; döngüyü otomatikleştir; dersi skill'e yazarak bileşimi kapat; Gözcü ve kurullarla yönetişimi kur; ölçekte modeli yönlendir ve kararlı prosedürleri derle — **her adımda doğrulama, kavrayış ve muhakeme sende kalsın.**

---

## EK — HIZLI SÖZLÜK

- **Döngü mühendisliği:** Ajanı promptlayan kişi olarak kendini, ajanları senin yerine dürten bir sistemle değiştirmek.
- **Tamamlanma durumu:** Görev listesi yerine, doğru olması gereken bitiş koşulu.
- **Bileşik yığın:** İlkeller → Orkestrasyon → Bellek → Kendini geliştirme; her çıktı puanlanıp damıtılıp belleğe geri yazılır.
- **Self-improving ≠ self-learning:** Etraftaki sistem birikir, model sabit / model kendi ağırlıklarını günceller (üretimde yok).
- **Alt-ajan:** İzole bağlam + sınırlı araç + tek işli, at-ve-unut. **Amaç paralellik değil sıkıştırma.** Başka alt-ajan doğuramaz, birbiriyle konuşamaz.
- **Ajan takımı:** Kalıcı, eşler arası haberleşen, paylaşılan görev listesi (blockedBy) üzerinden koordine.
- **Bağlam-merkezli ayrıştırma:** Rolü değil, "bu alt görev hangi bağlama ihtiyaç duyuyor?"u temel alan bölme.
- **Dinamik iş akışı:** Claude'un göreve özel, anında yazdığı harness; ajan başına izolasyon + model + izolasyon seviyesi.
- **parallel() / pipeline():** bariyer (hepsini bekle) / akış (her öğe bağımsız aksın).
- **Çekişmeli doğrulama:** Yapanın çıktısını, yalnız rubrik+eser gören ayrı doğrulayıcının denetlemesi.
- **Bağlam çürümesi:** Bağlam büyüdükçe (~300–400k token civarı) performansın düşmesi.
- **Rewind:** Önceki bir mesaja dönüp oradan yeniden promptlamak; başarısız denemenin gürültüsünü silmenin en iyi alışkanlığı.
- **Compact vs /clear:** Model özetler (kayıplı, emeksiz) / sen önemli olanı yazıp temiz başlarsın (emekli, isabetli).
- **STATE.md:** Belleğin diskte yaşadığı yer. "Ajan unutur; repo unutmaz."
- **Bileşen skill:** Prosedürel bellek; her başarısızlıktan sonra ders skill'e yazılır. Projeyle ölmez.
- **/goal vs /loop vs Outcomes:** Koşul doğru olana dek devam (ayrı model puanlar) / tempoda yeniden çalıştır / bulut, dosya-rubrik + puanlayıcı + max_iterations.
- **Görüyle öz-doğrulama:** Yapan render eder, doğrulayıcı görüntüyü hedefe karşı okur.
- **Karantina:** Güvenilmeyen içerik okuyan ajanın hiçbir yüksek-yetkili eylem alamaması.
- **Gözcü / Shadow Agent:** Filoyu izleyen watchdog; heartbeat + anomali + alarm + hoop müdahale. Asla kendi kendine terminate etmez.
- **Derlenmiş iş akışı:** Kararlı prosedürü küçük modele öğretip self-host etmek. 128–462x ucuz, kalite %87–98.
- **Güvenlik sınırı:** Üst modelin riskli alanlarda alt kademeye düşmesi. Bug değil; fallback için mimari kur.
- **Routines:** Kaydedilmiş konfigürasyonun bulutta zamanlama/API/GitHub tetikleyicisiyle koşması.
- **Comprehension debt / cognitive surrender:** Okumadığın kod arttıkça biriken kavrayış borcu; ve fikir sahibi olmayı bırakma cazibesi.

---

*Belge sonu — v1.0.*

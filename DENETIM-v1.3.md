# DENETİM RAPORU — AJAN İŞLETİM TALİMATI v1.3

Yöntem: belgenin kendi S3 protokolü. Altı denetçi ayrı bağlamlarda, birbirini görmeden,
her biri yalnız kendi rubriğiyle koştu; ardından bir meta-doğrulayıcı (M5) denetçileri denetledi.
88 ham bulgu → 4 iptal/indirim → 12 kök neden + 1 yeni bulgu.

---

## İPTAL VE İNDİRİMLER (meta-doğrulama)

| Bulgu | Hüküm | Gerekçe |
|---|---|---|
| **O1** "S1 erişilemez" | **İPTAL → ORTA** | §9.5 yaması yalnız K2/K4'ü eliyor, "karar yalnız K1/K3 üzerinden verilir" diyor. §14.1 kontrol listesi "tamamlanma durumu"nu (satır 1277) "kademe seçildi"den (1284) ÖNCE koyuyor. S1 erişilebilir ama DAR: tek çalışan kriter (K1), K3 ölü. **Beyin bunu önce yanlış doğruladı — K3'ü sınayıp K1'e genelledi.** Buna dayanan O2'nin "her iş S2'ye düşer" kısmı, O19 ve "terk sebebi #1" hükmü de düşer. |
| **G14** hiyerarşi çelişkisi | **İPTAL** | Blok kendi çözücüsünü taşıyor: "(çelişki çıkarsa yukarıdaki kazanır)" ve §11 sıra 1. 2b yalnız ilkeyi ismen ezmeye izin veriyor, §11 bir M-ilkesi değil. Geriye kalan risk zaten G4. |
| **G1** skill karantinada yok | **KRİTİK → ORTA** | §11.1'in beşinci maddesi hedeften bağımsız SÜREÇ kapısı: "karantinalı girdiden çıkan ders §12'nin DAMITMA adımında otomatik durur". DAMITMA = skill'in yazıldığı adım. Kemer eksik, askı takılı. |
| **Z2** T_tahsis tanımsız | **İNDİR** | §5.2/§5.4 sütun adı `Tahsis`, bağ açık. Ayakta kalan: rezerv aktarımından sonra paydanın güncellenip güncellenmediği yazılı değil. |
| **H3** §8.2 faili yok | **YÜKSEK → ORTA** | 5 satırın 2'si uygulanabilir. Kusur "fail yok" değil, "muhatap yazılmamış". |

Kalan 82 bulgunun örneklem kontrolünde yanlış okuma bulunmadı. Doğrulananlar: Z3 (T_dalga
totolojisi), Z4 (%40 tavanı), Z6 (KO=1.0 iki bantta), H1 (.claude/agents ve permissions yok),
O8 (doldurulmuş rubrik yok), O16 (bölüm sırası + başlık sayısı), K-serisinin bütün negatif grep'leri.

---

## 12 KÖK NEDEN

| # | Kök neden | Alt bulgular | ETKİ | MALİYET |
|---|---|---|---|---|
| **R2** | **Yetki ve yasak yalnız düzyazı; uygulayıcısı yok.** 13 rolün hepsi tam araç setiyle doğuyor. "Salt-okur", "yüksek yetkili eylem alamaz", "sıraya girer" — hepsi nazik rica. | H1,H5,G5,G7,G13,O6 | 5 | 2 |
| **R1** | **Harness modeli yanlış.** Alt-ajan canlı iş arkadaşı sanılmış; gerçekte tek metin döndürüp yok olan fonksiyon çağrısı. Belge bunu §8.4'te doğru yazıp §3/§4/§5'i o cümle yokmuş gibi kurmuş. | H2,H6,H11,H13,H14,O14,K1 | 5 | 4 |
| **R5** | **Kalıcı bellek tek yönlü mandal: girişi kapısız, çıkışı yok.** Bir koşuluk teslimat 6 onaydan geçiyor; tüm gelecek projeleri bağlayan kural 0'dan. Emeklilik ölçütü tanım gereği boş kümeye uygulanıyor. | G4,G8,G10,Z16,Z17,Z18,O13,G1 | 5 | 2 |
| **R3** | **Ölçen ile ölçülen aynı kişi.** Tek veri kaynağı sanığın beyanı. Şişirme baskın strateji; yakalayacak tek ölçü (VT) ölü. | Z1,Z11,Z12,Z15,O4,H6,H7 | 5 | 3 |
| **R10** | **Risk ile büyüklük karıştırılmış.** Hiçbir kapı patlama yarıçapını ölçmüyor. §11.3 iki cümle, onayı kimin vereceği yazılmamış. | G3,G11,O5,K4 | 5 | 2 |
| **R8** | **Kademe kapısı: seçen denetlenen.** Tek satırla altı mekanizma kalkıyor, kayıt bırakmadan. Tablo "hiçbiri atlanmaz" derken M5'e "—" yazıyor. | Y1,Y2,Y9,O3,O5,O12,O1↓ | 4 | 2 |
| **R6** | **Provenance tek kanala kurulmuş; kanal kimliği doğrulanmıyor.** §3/§7 karantina dışı; "kullanıcı düzeltmesi" kanalı sınanmıyor. | G2,G4,G6,G11,G12,G15 | 4 | 2 |
| **R7** | **Şema ölçtüğünü taşımıyor; başarı tanımı yok.** 7 alanlık çıktı 4 alanlık şemaya yazılıyor, düşen alan kalite biti. §14.3'ün 12 kutusu da işaretliyken kötü eser teslim edilebilir. | Z14,Z19,Z20,O7 | 4 | 2 |
| **M5-Y1** | **YENİ — üç normatif yüzey, tek sürüm damgası, sıfır senkron kuralı.** `grep v1.3`: belgede 3, CLAUDE.md'de 0, SKILL.md'de 0. §15 yalnız belgeyi kapsıyor. **Sapma zaten olmuş:** CLAUDE.md S1'i "tek adımlık, tek cümlede savunulabilen iş" diye tanımlıyor, §0.1 ise K1–K4 kriter setiyle. Skill 12 satırlık tablosuyla sabit bölüm numaralarına çapalı; §15.2 numara kaymasını serbest bırakıyor. | — | 3 | 1 |
| **R9** | **Sonlandırıcısı olmayan döngüler.** §4.4 ile M20 birbirini kilitliyor; kök-neden özyinelemesi sınırsız; "hiçbiri ayakta kalmadı"nın ikinci kez tek çıkışı yasak olan çıkış. | Y3,Y5,Y11,Y12 | 3 | 1 |
| **R12** | **Belge kendi kapılarından geçmemiş.** 39k token, doldurulmuş tek rubrik örneği yok, 10.6→10.7→10.5, başlık "10 adım" içerik "11 adım", §5.1 ile §5.2 birbirini iptal ediyor. | O2,O8,O9,O11,O15,O16,O18,O20 | 3 | 3 |
| **R11** | **Yaşam döngüsü boşlukları.** Yarıda kalma, geri sarma, kapsam değişimi, keşif işi, tekrarlayan iş, ara rapor — negatif grep'lerle kanıtlı. | K1–K6 | 3 | 3 |
| **R4** | **Zaman aritmetiği tanımsız/döngüsel/kendi anomalisini imal ediyor.** T_dalga totolojik; %40 tavanı bütçenin yarısını sahipsiz bırakıyor; kalibrasyon tek yönlü mandal (60→72→86.4, geri dönüş imkânsız); Zaman Denetçisi dayandığı hükümden önce koşuyor. | Z3–Z10,Z13,O10,Y4,Y8 | 2 | **5 → TAMİR ETME, SİL** |

---

## ÇELİŞEN TAVSİYELER — hakem kararları

| Çatışma | Hüküm |
|---|---|
| Yeni bölüm ekle (K1–K6, G3, Z20) ↔ belge zaten 39k token (O15) | **Yer kısıtı olarak O15 kazanır.** Eklenen her bölüm için R4'ten eşdeğer hacim silinir. |
| Kalıcı kurala doğrulama kurulu (G10/Z16) ↔ sistem öğrendikçe hızlansın (K5) | **Çelişmiyorlar, sırayla:** girişi onaylı olsun, onaylandıktan SONRA kademe düşürme yetkisi kazansın. K5'in "2 kez sorunsuz" ölçütü zaten G10'un istediği kanıt. |
| §11.3 çok sürtünmeli, gevşet (O6) ↔ §11.3 çok dar, 12 sınıf ekle (G3) | **Kapsamda G3, tanede O6.** Kural gevşemez; ONAY BİRİMİ değişir: eylem başına değil, *eylem sınıfı + hedef kümesi* başına oturumluk onay. |
| Ajanı kimliğiyle sürdür (H11) ↔ alt-ajan dönüşü provenance taşımıyor (G5) | **G5 kazanır.** Sürdürülen ajan karantinalı bağlamı da taşır. `fork` yalnız güvenilir kaynaklı dalgalarda. |
| Ölçümü esere taşı (H2/H6) ↔ §5.4 tablosunu tamir et (Z serisi) | **H2 kazanır kesin olarak.** Veri kaynağı sanığın beyanı olduğu sürece formül düzeltmek, ölçülemeyen bir büyüklüğü doğru hesaplamaktır. |

## YAN ETKİLER

- **R2'yi düzeltmek en büyük kazanç ama en büyük yeni sürtünmeyi de üretir.** Araç setleri daraldığı anda "salt-okur" Doğrulayıcı testi çalıştıramaz hale gelebilir (§3.1 ona o yetkiyi veriyor). Kademeli uygula: önce Doğrulayıcı/Meta/Karantina Okuyucu, sonra işçiler.
- **G3+O6'nın onay genişletmesi terk riskini doğrudan artırır.** O6'nın "aynı cümlede olduğu için gerçek güvenlik onunla gider" tespiti bu denetimin en isabetli sürtünme gözlemi.
- **K5'in hızlı yolu R8'i besler.** Kademe düşürme yetkisi denetlenen ajanın seçtiği kapıya bağlanırsa Y1 kötüleşir. K5 ancak R8 düzeldikten SONRA güvenli.
- **Z20'nin DBO'su teşvik yaratır:** "1. turda 3/3 ONAY" hedefi kurulu yumuşamaya iter (Y9'un baskısını kurumsallaştırır). Payı RET yokluğu değil, KULLANICI DÜZELTMESİ yokluğu olmalı.
- **K1'in uçuş kaydı STATE.md'ye yeni yazma yolu açar** → H5 yarışını ve G2 kapsam boşluğunu büyütür. Ayrı append-only dosyaya yazılmalı.
- **"Ölçümü esere taşı" M17'yi kurtarmıyor, öldürüyor** — ve bu doğru sonuç.

---

## HÜKÜM: YAMA MI, MİMARİ Mİ?

**İkisi de. Doktrin sağlam, uygulama katmanı yanlış modele yazılmış.**

**Yama yeterli:** §1'in 21 ilkesi · §7 ayrıştırma · §9 desen seçimi · §10.1–10.3 doğrulama zinciri ·
§11.1 doktrini · §12 çerçevesi · §15.

**Yeniden yazılmalı:** §3.2 Gözcü · §4.1 kaynak hesabı · **§5'in tamamı** · §10.5.
Ortak öncülleri tek bir yanlış: alt-ajanın koşarken gözlemlenebilir, sorgulanabilir, süresi
okunabilir bir varlık olduğu. Z serisinin 20 bulgusunun 13'ü bu tek öncülün türevi ve
**hiçbiri formül düzeltmesiyle kapanmaz.**

**Tek en yüksek getirili hamle:** §5'i onarma, **§5.5'e indir.** Zaman tahsisi yerine kapsam sınırı
varsayılan olsun; KO/VT/kalibrasyon tablosu silinsin; M17 "asgari süre denetimi"nden
"kapsam uyumu denetimi"ne dönüşsün. Bu tek karar R4'ün 13, R3'ün 4, R1'in 2 bulgusunu kapatır ve
belgeyi ~200 satır kısaltarak R12'ye ihtiyaç duyduğu yeri açar.

**En sert hüküm:** §15.3 "47 doğrulanmış bulgunun tamamı uygulandı, üç bağımsız denetçi +
meta-doğrulayıcıdan geçti" diye meşruiyet ilan ediyor. O denetimden geçmiş bir metinde §2
başlığının içeriğiyle çelişmesi, 10.6→10.7→10.5 sırası ve `T_dalga = T_dalga` totolojisi AYAKTA.
Belgenin kendi Yapı Denetçisi ölçütü iki dakikada RET verirdi. **§15.3'ün o satırı düzeltilmeli
veya kaldırılmalı** — M4'ün en görünür ihlali orada ve okuyucudan istenen güvenin tamamı ona dayanıyor.

---

## UYGULAMA SIRASI

1. **R2** — güvenlik mimarisini kâğıttan çıkar (`.claude/agents/*.md` + `permissions`)
2. **R5 + R10** — kalıcı zararın iki yolunu kapat; ikisi de ucuz
3. **R8 + M5-Y1 + R9** — düşük maliyetli kapı ve tutarlılık düzeltmeleri
4. **R1 + R3** birlikte — mimari onarım (§5'in indirilmesi burada)
5. **R7 + R6**
6. **R12 + R11** — R4'ün silinmesinden açılan yere

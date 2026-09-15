# DENETİM RAPORU — AJAN İŞLETİM TALİMATI v1.6.1

Belgenin kendi kapanışı "v1.6'nın kendisi henüz denetlenmedi" diyordu. Bu denetim o turdur.

**Yöntem.** §4.4'ün üç ölçütü (İçerik · Yapı · Uygulanabilirlik) ve §10.2'nin belge işi
rubriği uygulandı. Her bulgu satır numarasıyla; çelişki iddiaları için iki alıntı birden.
Ölçülebilir olan her şey `kontrol/` altındaki kapılara çevrildi — düzyazı bulgu, düzeltilse
bile tekrar eder.

**Kapsam kaydı (dürüstlük notu).** Bu denetim tek bağlamda koştu: ayrı bağlamlarda kör ve
eşzamanlı bir Final Kurulu toplanmadı. §0.1'in teslim beyanı gereği: **S2 düzeyi denetimdir,
S3 değil.** Bulguların kendisi eserden okunabilir olduğu için kanıtları bağımsız olarak
doğrulanabilir; kaçırılmış olabilecekler için bu kayıt konuyor.

---

## 8 BULGU

| # | Bulgu | ETKİ | MALİYET |
|---|---|---|---|
| **B1** | **R2 üç rolde açık kaldı — kapandı ilan edilmişti.** §3.1 on üç çekirdek rol sayıyor; `kurulum/claude/agents/` altında on dosya var. **Gözcü**, **Kapsam Belirleyici** ve **Kapsam Uyumu Denetçisi**'nin tanım dosyası yok. §3'ün kendi kuralı: *"O dosya yoksa rol tam araç setiyle doğar — `Write`, `Edit` ve `Bash` dahil."* Yani bu üçünün YASAK sütunu uygulanmıyor. | 5 | 3 |
| **B2** | **§13.4 şablonu, v1.4 ve v1.5'te silinen üç mekanizmayı geri getiriyor.** §13 "kopyala-yapıştır" bölümüdür: ajana birebir giden metin budur. | 5 | 1 |
| **B3** | **§0 okuma protokolü yanlış bölüme gönderiyor.** Adım 4b uçuş kaydı için `§2.2`'yi gösteriyor; uçuş kaydı `§2.0`'da tanımlı, §2.2 kapsam değişikliği. | 4 | 1 |
| **B6** | **İki doğurulabilir rol kataloğa hiç girmemiş.** **Kademe Kontrolörü** (§0.1, v1.6/R8) ve **Çelişki-Tarayıcı** (§10.5). İkisi de §3.1'de yok, tanım dosyası yok. | 4 | 2 |
| **B4** | **Künye "Kurul 5" diyor; dört kurul var.** §4.5 Boşluk Taraması belgede hiçbir yerde kurul diye anılmıyor — tek rolün (Boşluk-Planlayıcı) taramasıdır. | 3 | 1 |
| **B5** | **Sözlük "beş anomali" diyor; §4.2 yedi madde listeliyor.** | 2 | 1 |
| **B7** | **§14.3, §6.2'ye gönderiyor; operatif kural §6.3'te.** §6.2 boş şablondur; "kim hangi bölüme ne zaman yazar" §6.3 tablosudur. | 2 | 1 |
| **B8** | **v1.6.1 kendi kapısından tam geçmedi (öz-bulgu).** §15.2 adım 3 "§10.1 zincirinden geçer" diyor; format kapısı (§10.7) koşturuldu, bağımsız Doğrulayıcı koşturulmadı. Künyedeki "Final Kurulu 3/3 onay" satırı v1.6.1 için doğrulanmış değildir. | 3 | 2 |

---

## KANITLAR

### B1 — R2 üç rolde açık

`§3.1` on üç rol sayar. `kurulum/claude/agents/` on dosya içerir. Beyin orkestratördür,
alt-ajan değildir; dosya gerekmez. Geriye **on iki** rol kalır, **dokuzunun** dosyası vardır.

| Dosyası olmayan rol | Belgedeki YASAK'ı (§3.1) | Uygulanıyor mu |
|---|---|---|
| **Gözcü (Shadow)** | "Asla kendi başına ajan sonlandırmaz — önce raporlar" | hayır |
| **Kapsam Belirleyici** | "İçerik üretmez; listeyi işi yapan ajan yazamaz" | hayır |
| **Kapsam Uyumu Denetçisi** | "Sınırı genişletemez/daraltamaz (Beyin karar verir)" | hayır |

En ağırı üçüncüsüdür. v1.5'in **§5'in tamamını** yeniden yazma gerekçesi R3'tü: *ölçen ile
ölçülen aynı kişiydi.* Yeni düzenin tek dayanağı, ölçümü **esere yazamayan** ayrı bir rolün
yapmasıdır (§5.4: "Ölçü ESERDEN okunur, ajanın beyanından değil"; §6.3: "yalnız Kapsam Uyumu
Denetçisi yazar"). Tanım dosyası olmayınca o rol `Write`/`Edit`/`Bash` ile doğar — yani
ölçtüğü esere yazabilir. v1.5'in kök-neden düzeltmesi, uygulayıcısı kurulmadığı için
kâğıtta duruyor.

v1.4 günlüğü R2'yi "rollerin yetki sınırları düzyazıdan gerçek ajan tanım dosyalarına
taşındı" diye kapatmıştı. Doğrusu: **dokuz rol için taşındı, üç rol için taşınmadı.**

### B2 — §13.4 silinmiş mekanizmaları geri getiriyor

Şablon (satır 1592–1595):

```
Toplam süre: <T>. Alt görevler ve karmaşıklık/kritiklik puanları: <…>.
… Doğrulama payını %15'in altına indirme.
```

Belgenin aynı konudaki hükümleri:

- §5.2 (satır 670): *"v1.4'e kadar kullanılan `ağırlık = karmaşıklık × kritiklik` çarpımı
  ölçütsüz iki sezgiyi sahte-kesin bir sayıya çeviriyordu"* → kaldırıldı.
- §5.2 (satır 674): *"**Doğrulama bir yüzde değil, KAPIDIR.** v1.4'e kadar doğrulamaya
  bütçenin %15–20'si ayrılıyordu"* → yüzde kapıya çevrildi.
- §5.1 / §15.3 v1.5 satırı: süre tahsisi tümüyle silindi; `T` diye bir girdi yok.

Üçü de §13.4'te ayakta. §13.5 (Kapsam Uyumu Denetçisi çağrısı) v1.5 diline **düzgün**
güncellenmiş — yani sweep yapıldı ve 13.4 atlandı. v1.5 commit'i "29 tüketici yeniden
bağlandı" diyor; bu onlardan biri değildi.

Bu §10.2'nin otomatik RET koşuludur: *"aynı kural iki yerde farklı yazılmış."* Ağırlaştırıcı
sebep: iki kopyadan **operatif olanı** yanlış olandır. §5.2'yi okumayan, §13.4'ü yapıştıran
ajan silinmiş üç mekanizmayı uygular.

### B3 — okuma protokolü yanlış bölüme gönderiyor

Satır 22: `4b. **Uçuş kaydını kontrol et** (`.ajan-ucus.log`, §2.2).`
Satır 214 (§2.0 içinde): `.ajan-ucus.log` tanımının geçtiği tek yer.
§2.2'nin başlığı: *"Kapsam değişikliği — akış ortasında hedef değişirse."*

§0, belgenin en yüksek trafikli yoludur: her ajan her oturumda oradan geçer. §2.2'ye gidip
uçuş kaydı bulamayan ajan kurtarma akışını atlar — v1.6'nın R11 için eklediği kesinti
düzeltmesi tam olarak orada devreye girecekti.

Atıf **çözülüyor** (§2.2 var), o yüzden `kontrol/yuzey-senkronu.py` kapı 5 bunu yakalamadı.
Kapı kırık atfı arıyor; bu yanlış hedefli atıf.

### B4 — künye "Kurul 5"

§4.1 PARALELLİK KURULU · §4.2 KÖK-NEDEN KURULU · §4.3 KARAR KURULU · §4.4 FİNAL KURULU =
**dört**. §4.5 BOŞLUK TARAMASI'dır; belgede hiçbir yerde "Boşluk Kurulu" geçmez ve sözlüğün
kurul tanımı *"toplanan geçici ajan **grubu**"* der — boşluk taramasını tek rol yapar.

v1.6 künyeyi sabit değerden **türetilmiş** değere çevirdi ("kurul sayısı §4.x başlıklarından").
Türetme alt bölüm sayar, kurul saymaz. Sabit yanlış değeri türetilmiş yanlış değerle
değiştirmek sayıyı doğrulamadı — yalnız yanlışı otomatikleştirdi ve denetlenmesi
gereken bir yer gibi görünmekten çıkardı.

### B5 — sözlük beş, gövde yedi

Sözlük: *"**Anomali** | Gözcü'nün kök-neden kurulunu tetikleyen **beş** durumdan biri (§4.2)."*
§4.2 listesi yedi maddedir. İkisi v1.5/v1.6'da eklendi (kapsam dışına çıkma ve gerekçesiz
eksik bırakma — ikisi de "ilk seferde tetikler"). Sözlük güncellenmedi.

### B6 — kataloğa girmemiş iki rol

**Kademe Kontrolörü** (§0.1, satır 77): *"ucuz kademede tek soruluk bir 'Kademe Kontrolörü'
alt-ajanı"*, girdi kısıtıyla birlikte: *"Kontrolöre YALNIZ görev metni + §0.1'in dört S1
ölçütü verilir — eserin kendisi, gerekçe veya kimin istediği verilmez."*

Bu rol v1.6'nın R8 düzeltmesinin **tek uygulayıcısıdır**: S1 kapısını onaylayan aktör odur.
§3.1'de yok, `agents/` altında dosyası yok. `kurul-uyesi.md` yalnız Final Kurulu üyesini
kapsar. §3'ün kuralı: *"Eksik alanla ajan doğurmak yasaktır (M10)."*

**Çelişki-Tarayıcı** (§10.5): N≥4 dalgada halkanın yerine geçer, tüm çıktıları birlikte okur.
Aynı durumda.

### B7 — §14.3 yanlış alt bölüme gönderiyor

Satır 1683: `STATE.md'nin **değişen** bölümleri güncellendi (§6.2)`. §6.2 boş şablondur;
"Kim yazar / Hangi bölüme / Ne zaman" tablosu §6.3'tedir.

### B8 — v1.6.1'in kendi kapısı (öz-bulgu)

§15.2 adım 3: *"Değişiklik §10.1 zincirinden geçer."* v1.6.1'de format kapısı (§10.7)
koşturuldu ve yedi kapının tamamı mutasyon testiyle doğrulandı; **bağımsız bir Doğrulayıcı
koşturulmadı.** Künyedeki "Final Kurulu 3/3 onay" satırı v1.1'den beri duruyor ve hiçbir
sürümde yeniden kazanılmadı. Bu rapor onu kaldırmayı önerir: kazanılmamış meşruiyet
iddiası, denetimin v1.3'te verdiği **en sert hükmün** konusuydu ve künyede hâlâ duruyor.

---

## TEK KÖK NEDEN

Sekiz bulgunun yedisi (B8 hariç) **aynı şeydir**: bir değişiklik bir yüzeye iner, tüketicileri
taranmaz.

| Sürüm | Neyi değiştirdi | Neyi taramadı |
|---|---|---|
| v1.4 | R2 — rol sınırlarını dosyaya taşıdı | üç rolü (B1) |
| v1.5 | §5'i yeniden yazdı, 29 tüketici bağladı | §13.4 şablonunu (B2) |
| v1.6 | R8/R11 — yeni rol ve yeni anomali maddeleri ekledi | §3 kataloğunu, sözlüğü (B5, B6) |
| v1.6 | künyeyi türetilmiş hale getirdi | türetmenin doğru şeyi saydığını (B4) |
| v1.6.1 | senkron kapısını kurdu | **mekanik olmayan senkron sınıfını** |

Son satır bu denetimin asıl hükmüdür. `kontrol/yuzey-senkronu.py` **ucuz olan** sınıfı
kapatıyor: sürüm damgası, birebir kopya, kırık atıf, ölü terim. Bu belgeyi üç sürüm üst üste
ısıran sınıf ise **anlamsal**: çözülen ama yanlış hedefli atıf (B3, B7), bölümüyle çelişen
şablon (B2), gövdesiyle uyuşmayan sayı iddiası (B4, B5), kataloğa girmemiş rol (B1, B6).

Bunların hepsi ölçülebilir — yalnız farklı bir ölçüyle. Kapı genişletildi.

---

## UYGULAMA SIRASI

1. **B2** — §13.4'ü v1.5 diline getir. Tek şablon, en yüksek getiri: operatif metin bu.
2. **B3 + B7** — iki atıf düzeltmesi.
3. **B4 + B5** — iki sayı düzeltmesi; künye türetmesini kurul saymaya çevir.
4. **B1 + B6** — beş ajan tanım dosyası (Gözcü · Kapsam Belirleyici · Kapsam Uyumu Denetçisi ·
   Kademe Kontrolörü · Çelişki-Tarayıcı) + §3.1/§3.3 kataloğuna iki satır.
   **Tasarım işi içerir:** Kapsam Uyumu Denetçisi'nin `Bash`'e ihtiyacı var (§13.5: "komutu
   KENDİN yeniden çalıştır") ama `Write`/`Edit` alamaz — ölçtüğü esere yazamamalı.
5. **B8** — künyeden "Final Kurulu 3/3 onay" satırını kaldır veya kurulu gerçekten topla.

---

**Rapor sonu — v1.6.1 denetimi, S2 düzeyi.**
Bağımsız doğrulayıcı koşturulmadı; bulguların kanıtları eserden okunabilir olduğu için
her biri ayrı ayrı sınanabilir. Bu raporun kendisi de bir eserdir ve aynı kapıya tabidir.

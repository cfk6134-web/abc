# Kalıcı kurallar

Projeler arası geçerli, hatalardan damıtılmış kurallar. Her oturumda okunur (§0 adım 3).

**Yazma kuralı:** Buraya yalnız *doğrulanmış* ve *genellenebilir* dersler girer. Tek seferlik
sürçmeler ve projeye özgü gerçekler `STATE.md`'ye gider, buraya değil.

**Onay kuralı:** Bu dosya her oturumda okunur, yani protokolle eşdeğer bağlayıcılıktadır.
Buraya yazmak **kullanıcının açık onayını** gerektirir ve her kural en az bir bağımsız
Doğrulayıcı'dan geçer (§12).

**Zorunlu biçim.** Şu alanları taşımayan satır kural sayılmaz ve okunmaz:

```
- <kural>. (dayanak: <hangi hata>, tarih: <…>, hedef hata sınıfı: <id>,
            kaynak: güvenilir | KARANTİNALI, son doğrulama: <…>)
```

`hedef hata sınıfı` olmadan kuralın işe yarayıp yaramadığı ölçülemez ve kural hiç emekli olamaz.

**Boyut kuralı:** Bu dosya bir ekrana (≈40 satır) sığmalı. Üç çıkış yolu vardır (§12):
**ARŞİVLE** (koşul kalktı · 20 koşudur tetiklenmedi · yeni kural kapsıyor),
**YENİDEN YAZ** (hedef hata kural yazıldıktan sonra tekrar etti → kural etkisiz),
**İPTAL** (kuralın dayanağı yanlışlandı → derhal okumadan çıkar).
Bir kuralı yalnız "uzun süredir uyuluyor" diye emekli etme; ama "uzun süredir hiç tetiklenmedi"
ölçülebilir bir gerekçedir.

---

## Aktif kurallar

<!-- Örnek biçim — ilk gerçek ders geldiğinde bunu sil:
- <kural>. (dayanak: <hangi hata>, tarih: <…>, kaynak: güvenilir | KARANTİNALI)
-->

_(henüz kural yok — ilk ders geldiğinde §12 döngüsünden buraya yazılır)_

## Arşiv

<!-- Koruduğu koşul ortadan kalkmış veya 20 koşudur tetiklenmemiş kurallar.
     Varsayılan okumaya girmez; bir hata olduğunda buraya da bakılır. -->

## İptal

<!-- Dayanağı YANLIŞLANMIŞ kurallar. Arşivden farkıdır: bunlar "artık gerekmiyor" değil,
     "baştan yanlıştı". Biçim:
     - <kural> — İPTAL: <tarih>, gerekçe: <dayanak nasıl yanlışlandı>
     Kaynağı KARANTİNALI olan kurallar 10 koşuda bir yeniden doğrulanır;
     doğrulanmazsa buraya iner. -->

# Kalibrasyon Testi

`belge-tutarlilik-denetimi` skill'inin yakalama ve isabet oranını ölçen sabit test seti.

## Dosyalar

| Dosya | Ne |
|---|---|
| `kalibrasyon/sozlesme-tohumlu.md` | 11 bilinen hata + 1 tuzak içeren gerçekçi bir hizmet sözleşmesi |
| `kalibrasyon/cevap-anahtari.md` | Tohumların konumu ve hedef maddeleri — **denetimi yapan tarafa verilmez** |
| `kalibrasyon/puanla.py` | Raporu okuyup yakalama oranını ve tuzağın nasıl ele alındığını ölçer |

## Nasıl çalıştırılır

Test için alt-ajan gerekmiyor; temiz bir oturum yeterli. Önemli olan, denetimi yapanın cevap anahtarını görmemesi.

**1. Temiz bir oturumda denetimi çalıştır.** Skill kurulu olduğu için şu yeterli:

```
evals/kalibrasyon/sozlesme-tohumlu.md dosyasını TAM modda denetle,
raporu /tmp/rapor.md dosyasına yaz.
cevap-anahtari.md ve puanla.py dosyalarını okuma.
```

**2. Puanla:**

```bash
python3 evals/kalibrasyon/puanla.py /tmp/rapor.md
```

Betik şunları verir: kaç tohum bulundu, hangileri kaçtı, ve tuzağın (P1) gerekçeyle düşürülüp düşürülmediği.

**3. İsabeti elle değerlendir.** Yakalama otomatik ölçülür; isabet için raporu okumak gerekir: raporlanan bulguların kaçı gerçek, kaçı uydurma? Alıntısı metinde bulunmayan her bulgu uydurmadır.

İki koşu yapıp karşılaştırmak (KG-6) bulguların `KESİN` mi `OLASI` mı olduğunu gösterir.

## Testin can alıcı noktası: T11 ile P1

İkisi de "saklı kalmak kaydıyla" içerir; ayıran şey **yön**:

- **P1 (bulgu değil):** Madde 4.1, Madde 5'i saklı tutuyor — genel kural özel kurala boyun eğiyor, kurgu sağlam. Çelişki olarak raporlanırsa isabet düşer.
- **T11 (bulgu):** Madde 6.4, Madde 6.2'yi saklı tutuyor — erteleme yetkisi kendi kendini iptal ediyor, ölü hüküm. Kaçırılırsa yakalama düşer.

İfadeyi görüp bulguyu düşüren mekanik bir süzgeç P1'i doğru geçer ama T11'i kaçırır. Yönü okuyan bir süzgeç ikisini de doğru sınıflandırır. Bu çift, KG-2'nin mekanik mi anlamlı mı çalıştığını ölçer.

## Ölçüm geçmişi

### 1. tur — eski fixture (P1 yönü ters kuruluydu), 10 tohum

| | Skill'li | Taban (skill'siz) |
|---|---|---|
| Yakalama | 10/10 | 10/10 |
| Raporlanan | 13 ana bulgu + 29 etkilenen konum | 37 kalem, gruplama yok |
| Gerekçeli ret | 5 | 0 |
| Alıntı doğrulaması | 23/23 | beyan yok |
| Kapsam sınırı beyanı | var | yok |

**Bu turun asıl çıktısı bir kusur tespiti oldu.** Skill, "saklı kalmak kaydıyla" ifadesini görüp aday bulguyu mekanik olarak düşürdü. Taban koşusu ise ifadenin yönünü okudu ve haklı çıktı: özel hüküm genel hükmü saklı tutuyorsa kendini iptal eder. KG-2 bu hâliyle yanlış negatif üretiyordu.

Düzeltme: KG-2 artık istisna kaydının varlığını değil **yönünü** kontrol ediyor (bkz. `.claude/skills/belge-tutarlilik-denetimi/references/kalite-guvencesi.md`). Fixture'daki P1 tuzağı doğru yönle yeniden kuruldu ve ters yönü ölçen T11 tohumu eklendi.

### 2. tur — düzeltilmiş KG-2 (odaklı test)

Tam denetim koşuları üç kez oturum limitine takıldı. Bunun üzerine test, asıl bilinmeyene daraltıldı: her iki istisna kaydını da içeren Madde 4–6 aralığı denetletildi.

**Bu test yakalama değil, sınıflandırma ölçer** — ajana hangi aralığa bakacağı söylendiği için "bulabildi mi" sorusunu yanıtlamaz. Yanıtladığı soru: kaydı gördüğünde yönüne göre doğru ayırabiliyor mu?

| Kayıt | Yön | Beklenen | Sonuç |
|---|---|---|---|
| Madde 6.4 → 6.2'yi saklı tutuyor | Özel hüküm genel hükmü saklı tutuyor | `ÇELİŞKİLİ` | ✓ raporlandı |
| Madde 4.1 → 5'i saklı tutuyor | Genel kural özel kurala boyun eğiyor | Düşürülmeli | ✓ düşürüldü |

Ajanın yön okuması her iki hâlde de doğru gerekçeye dayandı: 6.4 için "boyun eğen hüküm uygulanabilir kalmıyor, tek işlevi 30 günden sapmaktı" → ölü hüküm; 4.1 için "boyun eğme daraltır ama boşaltmaz, iki alanda uygulanmaya devam eder" → kurgu sağlam.

Aynı koşuda kendiliğinden uygulanan diğer kurallar: teminat boşluğu çelişki değil eksiklik sayılıp tek sahip kuralıyla madde 16'ya yönlendirildi; Ek-B toplam hatası kök nedene göre Ek-B'ye ait ana bulgu olarak işaretlendi (İP-6); kapsam sınırı beyan edildi (KG-5); kullanılan araçlar listelendi (KG-7); tek koşu olduğu için kesinlik iddia edilmedi (KG-6); alıntılar `grep -F` ile doğrulandı (KG-1).

**Hâlâ ölçülmemiş olanlar:** tam denetimde 11 tohumun yakalama oranı, isabet oranı ve iki koşu arasındaki tekrarlanabilirlik. 1. tur sayıları 2. tur ile doğrudan karşılaştırılamaz — o koşular eski fixture'a karşı çalıştı ve 11. tohumu görmedi.

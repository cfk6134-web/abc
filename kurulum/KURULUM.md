# Genel kurulum — her projede geçerli

Bu paket, işletim talimatını bilgisayarındaki **tüm** Claude Code projelerinde devreye alır.
Tek proje için kurmak istersen `~/.claude/` yerine o projenin `.claude/` klasörünü kullan.

## Tasarım kararı: neden tam belge her oturuma yüklenmiyor

Talimat 1400 satır. Bunu global `CLAUDE.md`'ye koymak, en önemsiz iş için bile her oturumda
bağlamın önemli bir kısmını yakardı — belgenin kendi bağlam hijyeni kuralını (§8) ve "ağır
makineyi hak etmeyen işe kurma" ilkesini (§9.5) ihlal ederdi.

Bunun yerine üç katmanlı ifşa:

```
CLAUDE.md (42 satır)     → her oturumda. Kademe seçimi + kademeden bağımsız kurallar.
ajan-isletim skill'i     → iş büyüdüğünde açılır, hangi bölümü okuyacağını söyler.
AJAN-ISLETIM-TALIMATI.md → yalnız ilgili bölümü, grep'le. Tamamı asla bağlama alınmaz.
```

## Kurulum

### 1. Dosyaları yerine koy

```bash
mkdir -p ~/.claude/skills

cp kurulum/claude/CLAUDE.md                      ~/.claude/CLAUDE.md
cp kurulum/claude/AJAN-ISLETIM-TALIMATI.md       ~/.claude/
cp kurulum/claude/KURALLAR.md                    ~/.claude/
cp -r kurulum/claude/skills/ajan-isletim         ~/.claude/skills/
```

> `~/.claude/CLAUDE.md` zaten varsa **üzerine yazma** — dosyayı aç ve içeriği kendi notlarının
> yanına ekle.

### 2. Hook'ları ekle

`kurulum/claude/settings.json` içindeki `hooks` bloğunu `~/.claude/settings.json` dosyanla
**birleştir**. Dosya zaten varsa üzerine yazma; `hooks` anahtarını mevcut ayarlarının yanına ekle.

Doğrula:

```bash
python3 -m json.tool ~/.claude/settings.json > /dev/null && echo "JSON geçerli"
```

Hook'lar Claude Code'un yeniden okuması gerekir: bir kez `/hooks` menüsünü aç, ya da Claude
Code'u yeniden başlat.

### 3. Her yeni projede

```bash
cp kurulum/proje/STATE.md <proje-kökü>/STATE.md
```

Adını doldur. Bu dosya projeye özgüdür ve projeyle kalır; `KURALLAR.md` ise seninle taşınır.

## Hook'lar ne yapıyor

| Hook | Ne zaman | Ne yapar | Maliyet |
|---|---|---|---|
| `SessionStart` | Oturum açılışı | Zaman damgası basar (§5.1'in ihtiyaç duyduğu ölçüm çıpası) ve kademe seçimini hatırlatır | 0 token |
| `SubagentStop` | Her alt-ajan bitişi | `~/.claude/ajan-telemetri.log`'a satır ekler | 0 token, arka planda |
| `Stop` | Oturum sonu | `STATE.md` 30+ dakikadır güncellenmediyse uyarır | 0 token |

Üçü de deterministik kabuk komutu — model çalıştırmaz, hiçbir şey silmez, yalnız okur ve
log'a satır ekler. Bu, Gözcü'nün (§3.2) "ucuz filtre" katmanının pratik karşılığıdır:
sürekli bir LLM koşturmak yerine sayılabilir sinyalleri bedava yakalar.

`SubagentStop` telemetrisi zamanla birikir; Zaman Denetçisi'nin (§5.4) kalibrasyon verisi
oradan gelir:

```bash
wc -l ~/.claude/ajan-telemetri.log     # toplam alt-ajan koşusu
```

## Çalıştığını doğrula

1. Yeni bir Claude Code oturumu aç. Açılışta telemetri satırı bağlama girmeli.
2. Çok adımlı bir iş iste ("şu modülü refactor et ve testlerini yaz"). Ajan kademe seçmeli
   (muhtemelen S2) ve bunu söylemeli.
3. `/skills` listesinde `ajan-isletim` görünmeli.
4. Küçük bir iş iste ("şu yazım hatasını düzelt"). Ajan S1'de kalmalı, kurul kurmamalı.
   Kurul kuruyorsa çekirdek yanlış okunuyor demektir.

## Kaldırma

```bash
rm ~/.claude/CLAUDE.md ~/.claude/AJAN-ISLETIM-TALIMATI.md
rm -rf ~/.claude/skills/ajan-isletim
```
`~/.claude/settings.json` içindeki `hooks` bloğunu elle çıkar. `KURALLAR.md`'yi silme —
birikmiş dersler orada.

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
cp -r kurulum/claude/agents                      ~/.claude/
```

`agents/` klasörü **rollerin yetki sınırlarını gerçekten uygular.** Bu dosyalar olmadan
belgedeki her `YETKİ` ve `YASAK` satırı yalnız bir ricadır: alt-ajan varsayılan olarak
`Write`, `Edit` ve `Bash` dahil tam araç setiyle doğar. Yani "salt-okur Doğrulayıcı" ve
"yüksek yetkili eylem alamaz Karantina Okuyucu", eli klavyede duran bir ajana yazılmış
nazik cümleler olur. Bu klasör o cümleleri kurala çevirir.

> `~/.claude/CLAUDE.md` zaten varsa **üzerine yazma** — dosyayı aç ve içeriği kendi notlarının
> yanına ekle.

### 2. Hook'ları ekle

`kurulum/claude/settings.json` içindeki `hooks` **ve** `permissions` bloklarını
`~/.claude/settings.json` dosyanla **birleştir**. Dosya zaten varsa üzerine yazma;
iki anahtarı mevcut ayarlarının yanına ekle.

`permissions.deny` sır dosyalarının okunmasını engeller (`.env`, `~/.ssh`, anahtarlar);
`permissions.ask` ise geri dönüşü zor eylemleri (force push, `reset --hard`, dal silme,
kalıcı kural dosyasına yazma) onaya bağlar. Deny kuralları allow'dan **önce** değerlendirilir
ve katmanlar arasında birleşir — proje ayarların bunları gevşetemez.

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
| `SubagentStop` | Her alt-ajan bitişi | `~/.claude/ajan-telemetri.log`'a JSON satır ekler: zaman + oturum kimliği + ajan rolü | 0 token |
| `Stop` | Oturum sonu | `STATE.md` varsa ve 30+ dakikadır güncellenmediyse turu **engeller** (modele gider, ekrana değil) | 0 token |

Üçü de deterministik kabuk komutu — model çalıştırmaz, hiçbir şey silmez, yalnız okur ve
log'a satır ekler. Bu, Gözcü'nün (§3.2) "ucuz filtre" katmanının pratik karşılığıdır:
sürekli bir LLM koşturmak yerine sayılabilir sinyalleri bedava yakalar.

`SubagentStop` telemetrisi zamanla birikir:

```bash
wc -l ~/.claude/ajan-telemetri.log                    # toplam alt-ajan koşusu
python3 -c "import json,sys,collections;print(collections.Counter(json.loads(l)['a'] for l in open('$HOME/.claude/ajan-telemetri.log')))"
```

> **Bu log ne VERMEZ:** başlangıç damgası yok, tur sayısı yok, token yok. Yani buradan
> **süre hesaplanamaz.** Log yalnız "hangi rol kaç kez koştu" sorusunu yanıtlar.
> Bir alt-ajanın ne kadar sürdüğü bu ortamda hiçbir yere akmaz; bunu süre ölçüyormuş gibi
> kullanan her kural, ölçtüğünü sandığı şeyi ölçmez.

## Çalıştığını doğrula

1. Yeni bir Claude Code oturumu aç. Açılışta telemetri satırı bağlama girmeli.
2. Çok adımlı bir iş iste ("şu modülü refactor et ve testlerini yaz"). Ajan kademe seçmeli
   (muhtemelen S2) ve bunu söylemeli.
3. `/skills` listesinde `ajan-isletim` görünmeli; `/agents` listesinde 10 rol görünmeli.
   Görünmüyorlarsa frontmatter bozuktur — geçersiz alan **sessizce düşürülür**, hata vermez.
4. Küçük bir iş iste ("şu yazım hatasını düzelt"). Ajan S1'de kalmalı, kurul kurmamalı.
   Kurul kuruyorsa çekirdek yanlış okunuyor demektir.

## Kaldırma

```bash
rm ~/.claude/CLAUDE.md ~/.claude/AJAN-ISLETIM-TALIMATI.md
rm -rf ~/.claude/skills/ajan-isletim ~/.claude/agents
```
`~/.claude/settings.json` içindeki `hooks` bloğunu elle çıkar. `KURALLAR.md`'yi silme —
birikmiş dersler orada.

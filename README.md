# Claude Startup Lab

Türkçe talimatlarla çalışan, ayrı ayrı kurulabilen 10 Claude Code iş akışı eklentisi.

**Durum:** v0.1.0. Paket yapısı yerel doğrulayıcıyla kontrol edilmiştir. Claude Code çalışma zamanı ve gerçek projelerde davranış testi henüz yapılmamıştır. Bunlar komut tabanlı eklentilerdir; JavaScript hooks module kullanan native mods değildir.

## Eklentiler

| İş akışı | Eklenti adı | Claude Code komutu | Amaç |
| --- | --- | --- | --- |
| CTO Mode | `cto` | `/cto:run` | Fikirden uygulanabilir mimari ve geliştirme planına. |
| Ruthless Reviewer | `reviewer` | `/reviewer:run` | Kanıta dayalı kod incelemesi ve yayın kararı. |
| App Factory | `app-factory` | `/app-factory:run` | Android MVP ve mağaza hazırlığı. |
| Autopsy | `autopsy` | `/autopsy:run` | Eski projeye onarım veya yeniden yazma kararı. |
| Time Machine | `time-machine` | `/time-machine:run` | Büyüme ve değişim risklerini değerlendirme. |
| Chaos Monkey | `chaos` | `/chaos:run` | Kontrollü yerel dayanıklılık testi. |
| Detective | `detective` | `/detective:run` | Bug kök nedeni ve dar kapsamlı düzeltme. |
| Solo Startup | `solo-startup` | `/solo-startup:run` | Rol bazlı ürün geliştirme koordinasyonu. |
| Clone & Improve | `clone-improve` | `/clone-improve:run` | Ürün mekaniklerinden özgün alternatif geliştirme. |
| Game Master | `game-master` | `/game-master:run` | Doğrulanmış geliştirme işlerini RPG görevlerine çevirme. |

## Hızlı başlangıç

Git, Python 3 ve güncel Claude Code kurulu olmalı. Claude Code hesabı/oturumu ayrıca gerekir.

Depoyu indirdikten sonra depo kökünde terminalde:

```sh
python scripts/validate.py
claude plugin validate .
claude plugin marketplace add .
claude plugin install cto@startup-lab
```

Ardından geliştireceğin projenin dizininde `claude` başlat ve oturum içine yaz:

```text
/cto:run Android için öğrenci odaklı PDF düzenleme uygulamasının MVP'sini planla ve ilk akışını geliştir.
```

Tam kurulum, tüm eklentiler, Windows ve GitHub adımları: [Kurulum rehberi](docs/INSTALL.md).

## Çalışma modeli

Komutları kullanıcı başlatır. Eklentiler araç iznini atlatmaz; sabit bir model zorlamaz. Claude Code'un mevcut araçlarıyla çalışır. Solo Startup, alt ajan araçları mevcutsa delegasyon yapar; aksi halde rolleri sırayla uygular. APK üretimi için ayrıca Android/Flutter/React Native toolchain gerekir.

Önerilen sıra: CTO → App Factory → Detective → Chaos → Reviewer. Diğerlerini ihtiyaç olduğunda çağır. Raporlar hedef projeye yazılır.

## Geliştirme ve kontrol

```sh
python scripts/validate.py
claude plugin validate .
claude plugin validate ./plugins/cto
claude --plugin-dir ./plugins/cto
```

Son komut geçici yerel yükleme içindir. Kalıcı kurulumla birlikte aynı eklentinin iki kopyasını yükleme.

Lisans: [MIT](LICENSE). Resmi Anthropic ürünü değildir.

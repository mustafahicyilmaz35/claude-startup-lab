# Kurulum ve GitHub'a yükleme

## 1. Gereksinimler

- Git ve hesabıyla giriş yapılmış güncel Claude Code.
- Doğrulama için Python 3. Windows'ta `python` yerine `py -3` gerekebilir.
- Resmi kurulum: https://code.claude.com/docs/en/setup
- `claude --version` ve `git --version` ile kontrol et.

Bu paket Claude Code için hazırlanmıştır. Android telefondaki normal sohbet uygulamasına eklenti olarak kurulmaz.

## 2. GitHub'a göndermeden yerel kurulum

Arşivi aç. `claude-startup-lab` klasöründe terminal aç:

```sh
python scripts/validate.py
claude plugin validate .
claude plugin marketplace add .
claude plugin install cto@startup-lab
```

Bütün eklentileri ayrı ayrı kurmak için aşağıdaki komutlar PowerShell, Bash ve Zsh'ta kullanılabilir:

```sh
claude plugin install cto@startup-lab
claude plugin install reviewer@startup-lab
claude plugin install app-factory@startup-lab
claude plugin install autopsy@startup-lab
claude plugin install time-machine@startup-lab
claude plugin install chaos@startup-lab
claude plugin install detective@startup-lab
claude plugin install solo-startup@startup-lab
claude plugin install clone-improve@startup-lab
claude plugin install game-master@startup-lab
claude plugin list
```

Varsayılan kurulum kullanıcı kapsamındadır. Proje kapsamı gerekiyorsa örneğin `claude plugin install cto@startup-lab --scope project` kullan. Yerel marketplace klasörünü taşımadan/silmeden tut.

## 3. Kullanım

Kendi uygulama deponun dizininde `claude` başlat. Komutları terminal kabuğuna değil Claude Code sohbetine yaz:

```text
/cto:run Android gider takip uygulaması; tek geliştirici, çevrimdışı MVP.
/reviewer:run Son değişiklikleri incele; kodu değiştirme.
/app-factory:run CTO planındaki ilk kullanıcı akışını Android MVP olarak geliştir.
/autopsy:run Bu depoyu incele; onarma veya refactor kararı ver.
/time-machine:run Eşzamanlı isteklerin 10 kat artması senaryosunu değerlendir.
/chaos:run Yalnızca yerel test ortamında ödeme tekrar denemelerini sandbox ile sınayalım.
/detective:run Kullanıcı kaydet düğmesine iki kez basınca mükerrer kayıt oluşuyor.
/solo-startup:run Bu projeyi planla, uygula ve farklı rollerle doğrula.
/clone-improve:run Todoist temel iş akışından ADHD kullanıcılarına özgün bir görev uygulaması tasarla.
/game-master:run Mevcut MVP görevlerini doğrulanabilir quest'lere çevir.
```

Komut görünmezse `claude plugin list` ile etkinliği kontrol et ve yeni bir Claude Code oturumu aç. Yönetilen kurumsal politika eklentiyi engelleyebilir. APK build araçları veya dış servis erişimi eksikse ilgili mod bu engeli raporlar.

## 4. GitHub deposu oluşturma

GitHub'da kendi hesabında boş bir `claude-startup-lab` deposu oluştur. Yerel paket zaten Git başlangıç commit'i içeriyorsa yeniden `git init` gerekmez. Web arayüzünden yükleyeceksen `.claude-plugin` dahil bütün kaynak dosyalarını koru.

Klasör içinde aşağıdaki adımları uygula. `GITHUB_KULLANICIN` yer tutucusunu kendi kullanıcı adınla değiştir. Depoyu GitHub'da README eklemeden boş oluştur; mevcut dolu bir depoyu bu adımlarla ezme.

```sh
git status
git branch -M main
git remote add origin https://github.com/GITHUB_KULLANICIN/claude-startup-lab.git
git push -u origin main
```

Git geçmişi içermeyen bir kaynak kopyası kullanıyorsan önce:

```sh
git init -b main
git add .
git commit -m "Initial release: ten Claude Code workflow plugins"
```

Commit kimliği eksikse kendi Git ad/e-posta ayarını yap. GitHub'a gönderim için Git Credential Manager veya SSH gibi normal kimlik doğrulama yöntemini kullan; token'ı dosyalara yazma.

## 5. GitHub üzerinden kurulum

Depo gönderildikten sonra başkaları şu komutları kullanabilir. Kullanıcı adını değiştirmeyi unutma:

```sh
claude plugin marketplace add GITHUB_KULLANICIN/claude-startup-lab
claude plugin install cto@startup-lab
```

Diğer dokuz eklenti için bölüm 2'deki install komutları aynıdır. Yerel marketplace ile GitHub kaynağının adı aynıdır; geçişte önce yerel kaydı kaldır:

```sh
claude plugin marketplace remove startup-lab
claude plugin marketplace add GITHUB_KULLANICIN/claude-startup-lab
```

Gerekirse eklentileri yeniden kur ve `claude plugin list` ile kontrol et.

## 6. Güncelleme ve kaldırma

```sh
claude plugin marketplace update startup-lab
claude plugin update cto@startup-lab
claude plugin disable cto@startup-lab
claude plugin uninstall cto@startup-lab
```

Diğer eklentilerde adı değiştir. Kaynakta değişiklik yayınlarken ilgili plugin.json sürümünü artır; marketplace ve eklentileri doğrula, commit/push yap. Güncel seçenekler için `claude plugin --help` kullan.

## 7. Yayın öncesi kabul kontrolü

1. `python scripts/validate.py` başarılı olmalı.
2. Claude kurulu makinede marketplace ve her eklenti için `claude plugin validate` çalıştır.
3. Geçici test projesinde her komutun listelendiğini ve argümanı aldığını kontrol et.
4. Reviewer ve Autopsy'nin analiz isteğinde kaynak kodu değiştirmediğini dene.
5. Detective'i bilinen küçük bir bug üzerinde; Chaos'u izole mock servis üzerinde dene.
6. Game Master'ı aynı tamamlanmış görevle iki kez çağır; çift XP vermediğini kontrol et.
7. Solo Startup'ın mevcut araçlara göre delegasyon veya sıralı çalışma bildirdiğini kontrol et.

Bu kontrollerin çalışma zamanı kısmı paket hazırlanırken yürütülmedi.

## Kaynaklar

2026-10-07 tarihinde kontrol edilen resmi belgeler:
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/plugin-marketplaces
- https://code.claude.com/docs/en/skills

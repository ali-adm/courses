

## Для настройки Git на сервере Ubuntu, нужно:

1. Создать или скопировать SSH-ключи на сервер, если ты хочешь использовать SSH для подключения к GitHub.
2. Добавить SSH-ключ в аккаунт на GitHub.

Шаги:

1. **Проверь, есть ли SSH-ключи на сервере**:
   ```bash
   ls ~/.ssh
   ```
   Если там нет ключей, создай их:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. **Добавь SSH-ключ в агент**:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

3. **Скопируй публичный ключ**:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
   И добавь его в GitHub в разделе Settings → SSH and GPG keys.

4. Если репозиторий уже инициализирован, выполни команду для смены удалённого URL на SSH:
    ```bash
    git remote set-url origin git@github.com:ali-adm/chatbot-ui.git
    ```

5. Если Git-репозиторий не был инициализирован, можно это сделать с помощью:
    ```bash
    git init
    git remote add origin git@github.com:ali-adm/chatbot-ui.git
    ```

6. **Проверь соединение с GitHub**:
   ```bash
   ssh -T git@github.com
   ```

7. **Убедись, что remote настроен на SSH, а не HTTPS**:
   ```bash
   git remote set-url origin git@github.com:ali-adm/chatbot-ui.git
   ```
8. Текущая ветка main не имеет вышестоящей ветки. Чтобы отправить текущую ветку и установить внешнюю ветку как вышестоящую для этой ветки, используй
   ```bash
   git push --set-upstream origin main
   ```
   Либо просто
   ```bash
   git push -u origin main
   ```
9. Если появится сообщение о том, что нужно слить внешние изменения, и `git pull` - yне работает используй сначала
   ```bash
   git pull --set-upstream origin main
   ```
   Затем используй команды из предыдущего пункта.

Теперь ты сможешь пушить изменения на GitHub через SSH.


## Подключить каталог к репозиторию

Чтобы сменить удалённый репозиторий на свой, сделай следующее:

1. **Посмотреть текущие удалённые репозитории**:
   ```bash
   git remote -v
   ```

2. **Удалить старый удалённый репозиторий**:
   ```bash
   git remote remove origin
   ```

3. **Добавить свой репозиторий**:
   ```bash
   git remote add origin https://github.com/yourusername/your-repo.git
   ```

4. **Либо переключи remote на SSH, а не HTTPS**:
   ```bash
   git remote set-url origin git@github.com:yourusername/your-repo.git
   ```

5. **Теперь пушь изменения в свой репозиторий**:
   ```bash
   git push -u origin main
   ```
   Замените `main` на нужную ветку.

6. Если появится сообщение о том, что нужно слить внешние изменения, и `git pull` - yне работает используй сначала
   ```bash
   git pull --set-upstream origin main
   ```
   Затем используй команды из предыдущего пункта.


## Добавить ветку в существующий репозиторий

Чтобы запушить изменения из ветки `legacy` на тот же репозиторий, где у тебя уже есть ветка `main` с новой версией, нужно сделать следующее:

1. Убедись, что ты работаешь в ветке `legacy`. Выполни команду:
   ```bash
   git checkout legacy
   ```

2. Добавь свой удаленный репозиторий (если ещё не добавил). Например:
   ```bash
   git remote add origin https://github.com/username/repository.git
   ```

3. Чтобы не перепутать с веткой `main`, можешь пушить ветку `legacy` под тем же именем:
   ```bash
   git push origin legacy
   ```

Если же ты хочешь обновить ветку `main` из текущей ветки `legacy`:
1. Переключись на ветку `main`:
   ```bash
   git checkout main
   ```

2. Смерджи изменения из ветки `legacy` в `main`:
   ```bash
   git merge legacy
   ```

3. После этого можешь запушить изменения в ветку `main`:
   ```bash
   git push origin main
   ```

Таким образом ты обновишь либо ветку `legacy`, либо сольешь её изменения в `main`.


## Удалить все содержимое из ветки legacy, и добавить туда новое

Чтобы удалить все содержимое ветки `legacy` в удалённом репозитории и заменить его новым содержимым из локальной ветки `legacy`, выполните следующие шаги:

### Шаги для удаления старого содержимого и замены новым:

1. **Переключитесь на локальную ветку `legacy`:**
   Убедитесь, что находитесь на ветке `legacy` в локальном репозитории:

   ```bash
   git checkout legacy
   ```

2. **Удалите всё содержимое из ветки `legacy` (локально):**
   Удалите все файлы и каталоги из рабочей директории:

   ```bash
   git rm -r *
   ```

   Это удалит все файлы из индекса, но оставит ветку и её историю.

3. **Добавьте новые файлы (если они есть):**
   Добавьте новые файлы или содержимое, которые нужно запушить в ветку:

   ```bash
   git add .
   ```

4. **Закоммитьте изменения:**
   Сделайте коммит, который будет содержать удаление старого и добавление нового содержимого:

   ```bash
   git commit -m "Удалено старое содержимое и добавлено новое"
   ```

5. **Запушьте изменения на удалённую ветку `legacy`:**

   Чтобы перезаписать удалённую ветку полностью, используйте опцию `--force`:

   ```bash
   git push origin legacy --force
   ```

   Важно: **Опция `--force` перезапишет историю удалённой ветки**. Убедитесь, что никто не работает с этой веткой в удалённом репозитории, чтобы избежать потери данных.

Теперь удалённая ветка `legacy` будет содержать только те данные, которые вы запушили из локальной ветки.

## Удаление комита из оригинального репозитория

Чтобы удалить коммит из оригинального репозитория, тебе нужно сделать следующее:

1. **Перейти в нужную ветку** (если ты не на ней):
   ```bash
   git checkout main
   ```
   (или замените `main` на имя своей ветки)

2. **Вернуться к предыдущему коммиту**:
   ```bash
   git reset --hard HEAD~1
   ```
   Это удалит последний коммит и все изменения в нем.

3. **Сделать force push**:
   ```bash
   git push origin main --force
   ```
   Это перезапишет историю коммитов в оригинальном репозитории.

**Внимание!** Force push может перезаписать изменения, сделанные другими пользователями, так что используйте его с осторожностью.
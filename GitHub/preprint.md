Для настройки Git на сервере Ubuntu, нужно:

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

Теперь ты сможешь пушить изменения на GitHub через SSH.
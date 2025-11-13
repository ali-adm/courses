## Оглавление 

- [Оглавление](#оглавление)
- [Включение стирания строки ctrl+u как в bash](#включение-стирания-строки-ctrlu-как-в-bash)
- [Удаленный доступ к серверу по WinRM → запуск WSL](#удаленный-доступ-к-серверу-по-winrm--запуск-wsl)
  - [ЭТАП 1: Проверка на сервере (один раз сделал — и забыл)](#этап-1-проверка-на-сервере-один-раз-сделал--и-забыл)
  - [ЭТАП 2: С ноутбука → подключаемся по WinRM](#этап-2-с-ноутбука--подключаемся-по-winrm)
  - [ЭТАП 3: внутри сессии — запуск WSL](#этап-3-внутри-сессии--запуск-wsl)
  - [ЭТАП 4: дальше — SSH В WSL](#этап-4-дальше--ssh-в-wsl)
  - [Готовые команды (скопипасть с ноутбука)](#готовые-команды-скопипасть-с-ноутбука)
  - [БОНУС: Одной строкой (без интерактива)](#бонус-одной-строкой-без-интерактива)
  - [АВТОМАТИЗАЦИЯ (сохрани как .ps1)](#автоматизация-сохрани-как-ps1)
  - [БЕЗОПАСНОСТЬ (если не дома)](#безопасность-если-не-дома)
- [Классическая ошибка — `CreateRemoteRunspaceFailed`.](#классическая-ошибка--createremoterunspacefailed)
  - [ШАГ 1: Проверь основное (с ноутбука)](#шаг-1-проверь-основное-с-ноутбука)
  - [ШАГ 2: На сервере (если можешь зайти физически или через RDP)](#шаг-2-на-сервере-если-можешь-зайти-физически-или-через-rdp)
  - [ШАГ 3: С ноутбука — тест подключения](#шаг-3-с-ноутбука--тест-подключения)
  - [ШАГ 4: Альтернативный способ — `winrm` из cmd (если PowerShell глючит)](#шаг-4-альтернативный-способ--winrm-из-cmd-если-powershell-глючит)
  - [ШАГ 5: Полный рабочий пример](#шаг-5-полный-рабочий-пример)
  - [Если все еще не работает — диагностика](#если-все-еще-не-работает--диагностика)
  - [ГОТОВЫЙ СКРИПТ "ВСЁ В ОДНОМ" (с автопроверкой)](#готовый-скрипт-всё-в-одном-с-автопроверкой)
- [Если лень — альтернатива: **RDP + Автозапуск WSL**](#если-лень--альтернатива-rdp--автозапуск-wsl)
- [Если ошибка авторизации:](#если-ошибка-авторизации)
  - [Решение: 2 варианта (выбирай)](#решение-2-варианта-выбирай)
  - [ВАРИАНТ 1: разрешить HTTP (незашифрованный) — быстро, для дома](#вариант-1-разрешить-http-незашифрованный--быстро-для-дома)
    - [НА СЕРВЕРЕ (один раз):](#на-сервере-один-раз)
    - [С НОУТБУКА — сразу работает:](#с-ноутбука--сразу-работает)
  - [ВАРИАНТ 2: перейти на HTTPS (5986) — БЕЗОПАСНО](#вариант-2-перейти-на-https-5986--безопасно)
    - [НА СЕРВЕРЕ:](#на-сервере)
    - [С НОУТБУКА:](#с-ноутбука)
  - [БЫСТРЫЙ ФИКС (95% кейсов — это вариант 1)](#быстрый-фикс-95-кейсов--это-вариант-1)
    - [С НОУТБУКА → одна команда (если можешь зайти на сервер хоть как-то):](#с-ноутбука--одна-команда-если-можешь-зайти-на-сервер-хоть-как-то)
  - [ПРОВЕРКА: Что включено?](#проверка-что-включено)
  - [ГОТОВО. Ты уже внутри!](#готово-ты-уже-внутри)
- [БОНУС: скрипт "ВСЁ АВТОМАТОМ" (сохрани как `fix-winrm.ps1`)](#бонус-скрипт-всё-автоматом-сохрани-как-fix-winrmps1)
- [Как разрешить выполнение скриптов в PowerShell](#как-разрешить-выполнение-скриптов-в-powershell)
  - [Альтернативные политики](#альтернативные-политики)



## Включение стирания строки ctrl+u как в bash
```ps
Set-PSReadLineKeyHandler -Key Ctrl+u -Function BackwardDeleteLine
```

## Удаленный доступ к серверу по WinRM → запуск WSL

> **WinRM = Windows Remote Management**  
> Это **"SSH для Windows"** — работает через порт **5985 (HTTP)** или **5986 (HTTPS)**.

Кейс создавался для запуска WSL на удаленнм хосте с Windows.

### ЭТАП 1: Проверка на сервере (один раз сделал — и забыл)

Ты уже **поднимал WinRM** — но на всякий случай (если не работает):

```powershell
# Запусти на сервере ОТ АДМИНА
# Включи WinRM
winrm quickconfig
# Должно сказать: "WinRM service is already running"
```

Дополнительно (если с ноутбука не из той же сети/домена):

```powershell
# Разреши Basic Auth (для локальной сети)
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "192.168.1.100" -Force  # IP ноутбука
# Или * для всех (небезопасно, но дома ок)
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "*" -Force

# Включи Basic Auth
Set-Item WSMan:\localhost\Service\Auth\Basic -Value $true

# Разреши небезопасные подключения (если не HTTPS)
Set-Item WSMan:\localhost\Service\AllowUnencrypted -Value $true
```

> Перезагрузи службу: `Restart-Service WinRM`


### ЭТАП 2: С ноутбука → подключаемся по WinRM

Ты на **Windows ноуте**? Используй **PowerShell**.

```powershell
# Замени IP на IP сервера
$ip = "192.168.1.50"
$cred = Get-Credential  # Введи логин\пароль админа сервера

# Тест связи
Test-WSMan -ComputerName $ip

# Вход в интерактивную сессию
Enter-PSSession -ComputerName $ip -Credential $cred
```


### ЭТАП 3: внутри сессии — запуск WSL

```powershell
# Ты уже "на сервере" в PowerShell
wsl --list --verbose
# Если WSL выключен:
wsl --shutdown  # на всякий
wsl --start   # или просто wsl, если дистрибутив по умолчанию
```

> WSL2 **автозапустится** при первом `wsl` или `wsl -d Ubuntu`


### ЭТАП 4: дальше — SSH В WSL

После запуска WSL — SSH как обычно:

```bash
# С ноутбука (в WSL или Git Bash)
ssh user@192.168.1.50 -p 22
```

> Убедись, что **OpenSSH Server** в WSL включён:
```bash
sudo service ssh status
sudo service ssh start
```

[Назад к оглавлению](#оглавление)

### Готовые команды (скопипасть с ноутбука)

```powershell
# 1. Тест
Test-WSMan -ComputerName 192.168.1.50

# 2. Подключение
Enter-PSSession -ComputerName 192.168.1.50 -Credential (Get-Credential)

# 3. Внутри сессии:
wsl --list
wsl -d Ubuntu-22.04
# или
wsl --start
```


### БОНУС: Одной строкой (без интерактива)

```powershell
Invoke-Command -ComputerName 192.168.1.50 -Credential (Get-Credential) -ScriptBlock { wsl -d Ubuntu-22.04 }
```

> Запустит WSL на хосте Windows и **сразу выйдет**.


### АВТОМАТИЗАЦИЯ (сохрани как .ps1)

```powershell
# start-wsl-remote.ps1
$server = "192.168.1.50"
$cred = Get-Credential

Write-Host "Запускаем WSL на $server..." -ForegroundColor Green
Invoke-Command -ComputerName $server -Credential $cred -ScriptBlock {
    wsl --list --verbose
    wsl -d Ubuntu-22.04
} -ErrorAction Stop

Write-Host "WSL запущен! Теперь SSH: ssh user@$server" -ForegroundColor Cyan
```

> Запускай: `.\start-wsl-remote.ps1`


### БЕЗОПАСНОСТЬ (если не дома)

> - Используй **HTTPS (5986)** + сертификат
> - Или **VPN**
> - Не открывай WinRM в интернет!

[Назад к оглавлению](#оглавление)


## Классическая ошибка — `CreateRemoteRunspaceFailed`.  

Иногда WinRM **плюётся** на подключение.  
Погнали **диагностику за 2 минуты** — и **починим**.


### ШАГ 1: Проверь основное (с ноутбука)

```powershell
# 1. Пинг?
ping 192.168.1.254

# 2. Порт открыт?
Test-NetConnection 192.168.1.254 -Port 5985
```

Если **Port 5985 = False** → **WinRM не слушает** или **фаервол блочит**.


### ШАГ 2: На сервере (если можешь зайти физически или через RDP)

Запусти от **админа**:

```powershell
# 1. Включи WinRM (если не включён)
winrm quickconfig
# Должно сказать: "WinRM service is already running"

# 2. Проверь, слушает ли
netstat -an | findstr 5985
# Должно быть: TCP    0.0.0.0:5985    0.0.0.0:0    LISTENING

# 3. Фаервол — открой порт
New-NetFirewallRule -Name "WinRM HTTP" -DisplayName "WinRM HTTP" -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 5985

# 4. Разреши Basic Auth и TrustedHosts
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "192.168.1.*" -Force  # или конкретный IP ноутбука
Set-Item WSMan:\localhost\Service\Auth\Basic -Value $true
Set-Item WSMan:\localhost\Service\AllowUnencrypted -Value $true
```

> Перезапусти: `Restart-Service WinRM`

---

### ШАГ 3: С ноутбука — тест подключения

```powershell
# Замени IP
$ip = "192.168.1.254"

# Тест WinRM
Test-WSMan -ComputerName $ip -ErrorAction SilentlyContinue
```

**Ожидаемый вывод:**
```xml
wsmid: http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd
ProtocolVersion: http://schemas.dmtf.org/wbem/wsman/1/wsman/version
ProductVendor: Microsoft Corporation
ProductVersion: OS: 10.0.22621 SP: 0.0 Stack: 3.0
```

Если **ничего нет** → WinRM **не отвечает**.


### ШАГ 4: Альтернативный способ — `winrm` из cmd (если PowerShell глючит)

```cmd
winrm identify -r:http://192.168.1.254:5985 -auth:basic -u:твой_логин -p:твой_пароль
```

---

### ШАГ 5: Полный рабочий пример 

```powershell
$ip = "192.168.1.254"
$cred = Get-Credential  # Введи: .\твой_пользователь (локальный админ)

# Тест
Test-WSMan -ComputerName $ip

# Если ОК — подключаемся
Enter-PSSession -ComputerName $ip -Credential $cred -Authentication Basic
```

> **Ключевая фишка**: добавь `-Authentication Basic`, если не в домене.

---

### Если все еще не работает — диагностика

| Проблема | Как проверить | Решение |
|--------|---------------|--------|
| **WinRM не запущен** | `Get-Service WinRM` | `Start-Service WinRM -PassThru` |
| **Фаервол блочит** | `Test-NetConnection ... -Port 5985` | Открой порт (см. выше) |
| **TrustedHosts пустой** | `Get-Item WSMan:\localhost\Client\TrustedHosts` | `Set-Item ... -Value "192.168.1.100"` |
| **Basic Auth выключен** | `Get-Item WSMan:\localhost\Service\Auth\Basic` | `Set-Item ... $true` |
| **HTTPS только** | `winrm get winrm/config/service` | Включи HTTP или настрой HTTPS |

[Назад к оглавлению](#оглавление)


### ГОТОВЫЙ СКРИПТ "ВСЁ В ОДНОМ" (с автопроверкой)

```powershell
$ip = "192.168.1.254"
$cred = Get-Credential

Write-Host "Тестируем WinRM..." -ForegroundColor Yellow
if (Test-WSMan -ComputerName $ip -ErrorAction SilentlyContinue) {
    Write-Host "WinRM ОТВЕЧАЕТ! Подключаемся..." -ForegroundColor Green
    Enter-PSSession -ComputerName $ip -Credential $cred -Authentication Basic
} else {
    Write-Host "WinRM НЕ ОТВЕЧАЕТ. Проверь:" -ForegroundColor Red
    Write-Host "  1. winrm quickconfig на сервере"
    Write-Host "  2. Фаервол: порт 5985"
    Write-Host "  3. TrustedHosts"
}
```


## Если лень — альтернатива: **RDP + Автозапуск WSL**

1. Включи **RDP** на сервере
2. Подключись: `mstsc /v:192.168.1.254`
3. Включи автозапуск WSL при старте Windows:

```powershell
# В планировщике задач (Task Scheduler)
# Действие: wsl -d Ubuntu-22.04
# Триггер: При входе в систему
```


**Сейчас ты должен увидеть `Test-WSMan` с XML.**  

```powershell
Test-WSMan -ComputerName 192.168.1.254 -ErrorAction Stop
```

[Назад к оглавлению](#оглавление)


## Если ошибка авторизации:

```ps
PS C:\Users\aliadm> Enter-PSSession -ComputerName $ip -Credential $cred -Authentication Basic
Enter-PSSession : Сбой подключения к удаленному серверу 192.168.1.254. Соо
бщение об ошибке: Клиенту WinRM не удается обработать запрос. В настоящее
время в конфигурации клиента отключена передача незашифрованных данных. Из
мените конфигурацию клиента и повторите запрос. Подробности см. в разделе
справки "about_Remote_Troubleshooting".
строка:1 знак:1

Enter-PSSession -ComputerName $ip -Credential $cred -Authentication B ..
```

Как сообщается в ошибке - "передача незашифрованных данных отключена"  → WinRM на **сервере** **запрещает HTTP (незашифрованный трафик)**. Ты используешь **порт 5985 (HTTP)**, а сервер требует **HTTPS (5986)** или **разрешение незашифрованного**.


### Решение: 2 варианта (выбирай)


### ВАРИАНТ 1: разрешить HTTP (незашифрованный) — быстро, для дома

> **Только если в домашней сети!**

#### НА СЕРВЕРЕ (один раз):

```powershell
# Запусти ОТ АДМИНА на сервере
Set-Item WSMan:\localhost\Service\AllowUnencrypted -Value $true
Restart-Service WinRM
```

#### С НОУТБУКА — сразу работает:

```powershell
Enter-PSSession -ComputerName 192.168.1.254 -Credential $cred -Authentication Basic
```


### ВАРИАНТ 2: перейти на HTTPS (5986) — БЕЗОПАСНО

#### НА СЕРВЕРЕ:

```powershell
# 1. Создай самоподписанный сертификат
New-SelfSignedCertificate -DnsName "server.local" -CertStoreLocation Cert:\LocalMachine\My

# 2. Найди thumbprint
Get-ChildItem -Path Cert:\LocalMachine\My

# 3. Привяжи к WinRM
winrm create winrm/config/Listener?Address=*+Transport=HTTPS @{Hostname="server.local";CertificateThumbprint="ТВОЙ_THUMBPRINT"}
```

#### С НОУТБУКА:

```powershell
Enter-PSSession -ComputerName 192.168.1.254 -Credential $cred -Authentication Basic -UseSSL
```

[Назад к оглавлению](#оглавление)


### БЫСТРЫЙ ФИКС (95% кейсов — это вариант 1)

#### С НОУТБУКА → одна команда (если можешь зайти на сервер хоть как-то):

```powershell
Invoke-Command -ComputerName 192.168.1.254 -Credential (Get-Credential) -ScriptBlock {
    Set-Item WSMan:\localhost\Service\AllowUnencrypted -Value $true
    Restart-Service WinRM
    Write-Host "HTTP разрешён! Пробуй Enter-PSSession" -ForegroundColor Green
}
```

> После этого — **сразу**:
```powershell
Enter-PSSession -ComputerName 192.168.1.254 -Credential $cred -Authentication Basic
```


### ПРОВЕРКА: Что включено?

```powershell
# На сервере
winrm get winrm/config/service
```

Ищи:
```
AllowUnencrypted = true
```

---

### ГОТОВО. Ты уже внутри!

После подключения:

```powershell
wsl --list --verbose
wsl -d Ubuntu-22.04
```

И дальше — **SSH в WSL как обычно**.

[Назад к оглавлению](#оглавление)


## БОНУС: скрипт "ВСЁ АВТОМАТОМ" (сохрани как `fix-winrm.ps1`)

```powershell
$ip = "192.168.1.254"
$cred = Get-Credential

Write-Host "Фиксим WinRM на $ip..." -ForegroundColor Yellow

Invoke-Command -ComputerName $ip -Credential $cred -ScriptBlock {
    Set-Item WSMan:\localhost\Service\AllowUnencrypted -Value $true
    Set-Item WSMan:\localhost\Service\Auth\Basic -Value $true
    Restart-Service WinRM
    Write-Host "WinRM готов к HTTP + Basic!" -ForegroundColor Green
}

Start-Sleep -Seconds 3

Write-Host "Подключаемся..." -ForegroundColor Cyan
Enter-PSSession -ComputerName $ip -Credential $cred -Authentication Basic
```

> Запусти — и ты **внутри сервера**.

[Назад к оглавлению](#оглавление)


##  Как разрешить выполнение скриптов в PowerShell

```bash
PS C:\Users\aliadm> npm -v
npm : Невозможно загрузить файл C:\Program Files\nodejs\npm.ps1, так как выполнение сценариев отключено в этой системе.
```

Классическая проблема с политикой выполнения в PowerShell. Ошибка говорит о том, что в системе заблокировано выполнение скриптов, к которым относится и `npm.ps1`. Лечится это изменением политики выполнения.

Вот пошаговая инструкция, как это сделать: 

1.  **Запусти PowerShell от имени администратора**: Это обязательно, без прав администратора политику не изменить. Нажми `Win + X` и выбери «Windows PowerShell (администратор)».

2.  **Проверь текущую политику**: Выполни команду:

    ```powershell
    Get-ExecutionPolicy
    ```

    Скорее всего, она вернет `Restricted` (что означает «запрещено»).

3.  **Установи разрешающую политику**: Самым безопасным вариантом считается `RemoteSigned`. Она позволяет запускать локальные скрипты без подписи, но требует цифровой подписи для скриптов, скачанных из интернета (например, через почту или браузер).
    ```powershell
    Set-ExecutionPolicy RemoteSigned
    ```
    После ввода команды появится запрос на подтверждение — введи `Y` и нажми Enter.

4.  **Проверь новую политику**:
    ```powershell
    Get-ExecutionPolicy
    ```
    Теперь команда должна вернуть `RemoteSigned`.

Готово! После этих действий закрой все открытые окна PowerShell (включая те, что не запущены от администратора) и открой заново. Ошибка при вызове `npm -v` должна исчезнуть.

### Альтернативные политики

Если по какой-то причине `RemoteSigned` не подходит, можно рассмотреть другие варианты:

*   `Bypass`: Обходит все политики безопасности. **Не рекомендуется** для повседневного использования, но может выручить в изолированных средах.
*   `Unrestricted`: Позволяет выполнять любые скрипты, но перед запуском неподписанного скрипта из интернета запрашивает подтверждение. Более мягкий, но менее безопасный вариант по сравнению с `RemoteSigned`.

Если после смены политики npm все равно не работает, дай знать — будем разбираться дальше.

[Назад к оглавлению](#оглавление)


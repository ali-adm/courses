## Включение стирания строки ctrl+u как в bash
```ps
Set-PSReadLineKeyHandler -Key Ctrl+u -Function BackwardDeleteLine
```

## Удаленный доступ к серверу по WinRM → запуск WSL

> **WinRM = Windows Remote Management**  
> Это **"SSH для Windows"** — работает через порт **5985 (HTTP)** или **5986 (HTTPS)**.

---

### ЭТАП 1: ПРОВЕРКА НА СЕРВЕРЕ (один раз сделал — и забыл)

Ты уже **поднимал WinRM** — но на всякий случай (если не работает):

```powershell
# Запусти на сервере ОТ АДМИНА
winrm quickconfig
# Ответ: "WinRM уже настроен" — ок
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

---

### ЭТАП 2: С НОУТБУКА → ПОДКЛЮЧАЕМСЯ ПО WinRM

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

---

### ЭТАП 3: ВНУТРИ СЕССИИ — ЗАПУСК WSL

```powershell
# Ты уже "на сервере" в PowerShell
wsl --list --verbose
# Если WSL выключен:
wsl --shutdown  # на всякий
wsl --start   # или просто wsl, если дистрибутив по умолчанию
```

> WSL2 **автозапустится** при первом `wsl` или `wsl -d Ubuntu`

---

### ЭТАП 4: ДАЛЬШЕ — SSH В WSL

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

---

### ГОТОВЫЕ КОМАНДЫ (скопипасть с ноутбука)

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

---

### БОНУС: ОДНОЙ СТРОКОЙ (без интерактива)

```powershell
Invoke-Command -ComputerName 192.168.1.50 -Credential (Get-Credential) -ScriptBlock { wsl -d Ubuntu-22.04 }
```

> Запустит WSL и **сразу выйдет**.

---

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

---

### БЕЗОПАСНОСТЬ (если не дома)

- Используй **HTTPS (5986)** + сертификат
- Или **VPN**
- Не открывай WinRM в интернет!

---

### ИТОГО: ТЫ СЕЙЧАС МОЖЕШЬ:

| Действие | Команда |
|--------|--------|
| Проверить WinRM | `Test-WSMan 192.168.1.50` |
| Зайти в PowerShell | `Enter-PSSession ...` |
| Запустить WSL | `wsl -d Ubuntu` |
| Одной строкой | `Invoke-Command ...` |


## **Классическая ошибка** — `CreateRemoteRunspaceFailed`.  

Иногда WinRM **плюётся** на подключение.  
Погнали **диагностику за 2 минуты** — и **починим**.

---

### ШАГ 1: ПРОВЕРЬ ОСНОВНОЕ (с ноутбука)

```powershell
# 1. Пинг?
ping 192.168.1.254

# 2. Порт открыт?
Test-NetConnection 192.168.1.254 -Port 5985
```

Если **Port 5985 = False** → **WinRM не слушает** или **фаервол блочит**.

---

## ШАГ 2: НА СЕРВЕРЕ (если можешь зайти физически или через RDP)

### Запусти от **админа**:

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

## ШАГ 3: С НОУТБУКА — ТЕСТ ПОДКЛЮЧЕНИЯ

```powershell
# Замени IP
$ip = "192.168.1.254"

# Тест WinRM
Test-WSMan -ComputerName $ip -ErrorAction SilentlyContinue
```

### Ожидаемый вывод:
```xml
wsmid: http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd
ProtocolVersion: http://schemas.dmtf.org/wbem/wsman/1/wsman/version
ProductVendor: Microsoft Corporation
ProductVersion: OS: 10.0.22621 SP: 0.0 Stack: 3.0
```

Если **ничего нет** → WinRM **не отвечает**.

---

## ШАГ 4: АЛЬТЕРНАТИВНЫЙ СПОСОБ — `winrm` из cmd (если PowerShell глючит)

```cmd
winrm identify -r:http://192.168.1.254:5985 -auth:basic -u:твой_логин -p:твой_пароль
```

---

## ШАГ 5: ПОЛНЫЙ РАБОЧИЙ ПРИМЕР (с твоим IP)

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

## ЕСЛИ ВСЁ ЕЩЁ НЕ РАБОТАЕТ — ДИАГНОСТИКА

| Проблема | Как проверить | Решение |
|--------|---------------|--------|
| **WinRM не запущен** | `Get-Service WinRM` | `Start-Service WinRM -PassThru` |
| **Фаервол блочит** | `Test-NetConnection ... -Port 5985` | Открой порт (см. выше) |
| **TrustedHosts пустой** | `Get-Item WSMan:\localhost\Client\TrustedHosts` | `Set-Item ... -Value "192.168.1.100"` |
| **Basic Auth выключен** | `Get-Item WSMan:\localhost\Service\Auth\Basic` | `Set-Item ... $true` |
| **HTTPS только** | `winrm get winrm/config/service` | Включи HTTP или настрой HTTPS |

---

## ГОТОВЫЙ СКРИПТ "ВСЁ В ОДНОМ" (с автопроверкой)

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

---

## ЕСЛИ ЛЕНЬ — АЛЬТЕРНАТИВА: **RDP + Автозапуск WSL**

1. Включи **RDP** на сервере
2. Подключись: `mstsc /v:192.168.1.254`
3. Включи автозапуск WSL при старте Windows:

```powershell
# В планировщике задач (Task Scheduler)
# Действие: wsl -d Ubuntu-22.04
# Триггер: При входе в систему
```

---

**БРО, СЕЙЧАС ТЫ ДОЛЖЕН УВИДЕТЬ `Test-WSMan` с XML.**  
Если **всё ещё ошибка** — скинь вывод:

```powershell
Test-WSMan -ComputerName 192.168.1.254 -ErrorAction Stop
```

И я скажу **точную команду** для сервера.

**ТЫ УЖЕ НА ФИНИШНОЙ ПРЯМОЙ.**  
Через 3 минуты — `wsl` по сети. 🚀


## Если ошибка авторизации:
PS C:\Users\aliadm> Enter-PSSession -ComputerName $ip -Credential $cred -Authentication Basic
Enter-PSSession : Сбой подключения к удаленному серверу 192.168.1.254. Соо
бщение об ошибке: Клиенту WinRM не удается обработать запрос. В настоящее
время в конфигурации клиента отключена передача незашифрованных данных. Из
мените конфигурацию клиента и повторите запрос. Подробности см. в разделе
справки "about_Remote_Troubleshooting".
строка:1 знак:1

Enter-PSSession -ComputerName $ip -Credential $cred -Authentication B ..


БРО, **ошибка 100% ясна**:  
> **"передача незашифрованных данных отключена"**  
→ WinRM на **сервере** **запрещает HTTP (незашифрованный трафик)**.

Ты используешь **порт 5985 (HTTP)**, а сервер требует **HTTPS (5986)** или **разрешение незашифрованного**.

---

## **РЕШЕНИЕ: 2 ВАРИАНТА (ВЫБИРАЙ)**

---

### **ВАРИАНТ 1: РАЗРЕШИТЬ HTTP (незашифрованный) — БЫСТРО, ДЛЯ ДОМА**

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

---

### **ВАРИАНТ 2: ПЕРЕЙТИ НА HTTPS (5986) — БЕЗОПАСНО**

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

---

## **БЫСТРЫЙ ФИКС (95% КЕЙСОВ — ЭТО ВАРИАНТ 1)**

### С НОУТБУКА → **ОДНА КОМАНДА** (если можешь зайти на сервер хоть как-то):

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

---

## ПРОВЕРКА: ЧТО ВКЛЮЧЕНО?

```powershell
# На сервере
winrm get winrm/config/service
```

Ищи:
```
AllowUnencrypted = true
```

---

## ГОТОВО. ТЫ УЖЕ ВНУТРИ.

После подключения:

```powershell
wsl --list --verbose
wsl -d Ubuntu-22.04
```

И дальше — **SSH в WSL как обычно**.

---

## БОНУС: СКРИПТ "ВСЁ АВТОМатом" (сохрани как `fix-winrm.ps1`)

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

---

**БРО, ТЫ СДЕЛАЛ ЭТО.**  
Через 30 секунд — `wsl` по сети.  
Пиши: **"Я внутри!"** — и погнали **A1111 + SDXL по SSH**.

**СЕРВЕР ТВОЙ. ДАЖЕ НЕ ВСТАВАЯ.** 🚀
> -- Взломщики редко меняют свои подсети - сказала монашка, надевая на свечу презерватив.


## 1. Как смотреть кто ломится

**Прямой эфир атак (спамит в терминал):**
```routeros
/log print follow where topics~"critical"
```
*Нажми `Ctrl+C` чтоб выйти.*

**Последние 50 неудачных попыток:**
```routeros
/log print where message~"login failure" 
```

**Уникальные IP атакующих (сгруппированно):**
```routeros
# Просто смотри вывод глазами. Или скопируй в блокнот.
/log print where message~"login failure"
```

## 2. Управление черным списком

**Посмотреть кого уже заблокировал:**
```routeros
# Показывает уникальные адреса в бане
/ip firewall address-list print where list="brute-force-blacklist"
```

**Забанить один IP:**
```routeros
# Адрес 1.2.3.4, с таймаутом на 7 дней
/ip firewall address-list add list=brute-force-blacklist address=1.2.3.4 timeout=7d comment="Manual ban"
```

**Забанить целую подсеть (/24):**
```routeros
/ip firewall address-list add list=brute-force-blacklist address=45.205.1.0/24 timeout=30d comment="Block subnet"
```

**Забанить диапазон (/16 - большая подсеть):**
```routeros
/ip firewall address-list add list=brute-force-blacklist address=45.205.0.0/16 timeout=30d comment="Block large subnet"
```

**Разбанить конкретный IP:**
```routeros
/ip firewall address-list remove [find where list="brute-force-blacklist" and address="45.205.1.5"]
```

**Разбанить всё (ОСТОРОЖНО!):**
```routeros
/ip firewall address-list remove [find where list="brute-force-blacklist"]
```

## 3. Анализ — стоит ли банить подсеть

**Проверь, откуда атакуют (страна/провайдер):**
```routeros
/tool ip-scan address=45.205.1.5
```

Или введи IP на **whois.domaintools.com** в браузере.

**Если увидишь что атакуют с одного провайдера/региона — банань подсеть.**

## 4. Проверка что правило фильтра на месте

```routeros
/ip firewall filter print where comment="DROP Bruteforce"
```
Должно быть:
```
13  ;;; DROP Bruteforce
    chain=input action=drop src-address-list=brute-force-blacklist
```

## 5. Быстрое добавление нового атакующего (если подсеть новая)

Увидел в логах новый IP:
```routeros
/log print where message~"login failure" 
```

Скопируй IP и выполни:
```routeros
/ip firewall address-list add list=brute-force-blacklist address=ПОСТАВЬ_IP_СЮДА timeout=7d comment="Manual ban"
```

**Проверь что добавился:**
```routeros
/ip firewall address-list print where list="brute-force-blacklist" and address~"первые_три_цифры"
```

## 6. Мониторинг (чтоб не сидеть в логах постоянно)

**Скрипт для быстрого просмотра новых атак:**
```routeros
/log print where message~"login failure" and time>([/system clock get time] - 01:00:00)
```
*Покажет атаки за последний час.*

## 7. Полезные команды

**Посмотреть статистику по черному списку:**
```routeros
# Выведет количество уникальных объектов в бане
/ip firewall address-list print count-only where list="brute-force-blacklist"
```

**Удалить истекшие записи:**
```routeros
/ip firewall address-list remove [find where list="brute-force-blacklist" and timeout=0s]
```

**Сохранить конфиг (чтоб после перезагрузки всё осталось):**
```routeros
/system backup save name=before-cleanup
```

## Итог по ручному управлению:

1. **Раз в день** смотришь логи: `/log print where message~"login failure"`
2. **Видишь новый IP** — банишь его или всю подсеть
3. **Раз в неделю** чистишь старые записи
4. **Правило фильтра** уже стоит и работает

---

## 1. Как очистить логи

В MikroTik **нельзя просто очистить логи** командой `/log clear`. Есть два способа:

**Способ 1 — через WinBox (проще):**
- System → Logging → нажать `Clear` (кнопка с ластиком)

**Способ 2 — через терминал (выключить/включить логирование):**
```routeros
/system logging set 3 action=memory
```
*Это перезапустит логирование critical сообщений*

**Но лучше не чистить логи, а просто смотреть только новые:**

```routeros
/log print where message~"login failure" and time>([/system clock get time] - 00:30:00)
```
*Покажет атаки за последние 30 минут*

### 2. Твоя проблема с логами

Смотри: у тебя `critical` логи выводятся в `echo` (прямо в терминал). Это и есть причина спама.

**Чтобы спам не мешал, но логи сохранялись:**

```routeros
/system logging set 3 action=memory
```

Теперь сообщения не будут выводиться в терминал, но скрипт их сможет читать.

### 3. Как посмотреть последние атаки без спама в терминале

```routeros
/log print where topics~"critical" and message~"login failure" limit=20
```

### 4. Что сейчас важно

Твоя защита работает:
- **4 записи** в черном списке
- Правило фильтра **на 13 позиции** дропает их
- Атака не проходит

**Сделай только одно действие:**

Отключи вывод critical в терминал, чтобы не мешало:
```routeros
/system logging set 3 action=memory
```

**Всё, бро. Теперь терминал чистый, а защита работает.**


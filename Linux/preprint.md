- [Зомби процессы Linux](#зомби-процессы-linux)
- [SWAP-файлы VIM](#swap-файлы-vim)
- [Очистка Ubuntu с Docker](#очистка-ubuntu-с-docker)


## Зомби процессы Linux

Каждая программа, которая выполняется в Linux, - это системный процесс, у которого есть свой идентификатор. Каждый процесс может запускать дочерние процессы с помощью функции fork. Такие процессы остаются под контролем родительского процесса и не могут быть завершены без его ведома. Если один из дочерних процессов всё же завершился, а его родительский процесс не смог получить об этом информацию, то такой дочерний процесс становится зомби.

Зомби процессы Linux не выполняются и убить их нельзя, даже с помощью `sigkill`, они продолжают висеть в памяти, пока не будет завершён их родительский процесс.

Посмотреть такие процессы можно с помощью утилиты ps, здесь они отмечаются как defunct:
```bash
ps aux | grep defunct
```

Если вы попытаетесь убить такой процесс с помощью сигнала KILL, то ничего не выйдет. Чтобы его завершить, нужно найти "родителя" этого процесса. Для этого используйте команду:
```bash
ps -xal | grep defunct
```

Здесь идентификатор родительского процесса находится в четвёртой колонке (PPID). Теперь мы можем послать ему сигнал завершения, и такого процесса в системе больше не будет:
```bash
kill -KILL 3990
```

Для большего удобства вы можете использовать утилиты `top` или `htop`, но принцип их действия будет аналогичным, поэтому я не буду здесь его рассматривать. Теперь вы знаете, что делать, если в вашей системе появились зомби процессы Linux.

[Источник losst.pro](https://losst.pro/zombi-protsessy-linux)


## SWAP-файлы VIM

При октрытии файла (в данном случае `docker-compose.yml`) с помощью VIM, видим следующее:
```bash
E325: ATTENTION
Found a swap file by the name ".docker-compose.yml.swp"
          owned by: admin_d   dated: Tue Feb 10 11:37:18 2026
         [cannot be read]
While opening file "docker-compose.yml"
             dated: Tue Feb 10 11:27:01 2026

(1) Another program may be editing the same file.  If this is the case,
    be careful not to end up with two different instances of the same
    file when making changes.  Quit, or continue with caution.
(2) An edit session for this file crashed.
    If this is the case, use ":recover" or "vim -r docker-compose.yml"
    to recover the changes (see ":help recovery").
    If you did this already, delete the swap file ".docker-compose.yml.swp"
    to avoid this message.

Swap file ".docker-compose.yml.swp" already exists!
[O]pen Read-Only, (E)dit anyway, (R)ecover, (D)elete it, (Q)uit, (A)bort:
```

Это классическая ситуация с **Vim** и **swap-файлами**! Это не страшно, щас разберемся.

- Что происходит:

Когда ты редактируешь файл в Vim, он создает swap-файл (.filename.swp) для восстановления при сбоях. Если Vim завершился аварийно (краш, Ctrl+Z, убил процесс и т.д.), swap-файл остается.

- Как почистить:

Вариант 1: Самый простой и безопасный
```bash
# Просто удаляем все swap-файлы из текущей директории
rm -f .*.swp
rm -f .*.swo
rm -f .*.swn

# Или одной командой
find . -name ".*.sw[ponmlkjihg]" -type f -delete
```

Вариант 2: Посмотреть что есть и удалить
```bash
# Найти все swap файлы
ls -la .*.sw*

# Удалить конкретный файл
rm -f .docker-compose.yml.swp
```

Вариант 3: Если нужно восстановить изменения
```bash
# Восстановить из swap-файла
vim -r docker-compose.yml

# Или внутри Vim
:recover
```

Если не удаляется (частая проблема в Docker-директориях), по причине: мог остаться "висячий" процесс Vim или контейнер монтирует директорию.

- Решение:
```bash
# 1. Проверим процессы Vim
ps aux | grep vim
ps aux | grep docker-compose.yml

# 2. Если есть - убиваем
sudo pkill -9 vim
sudo pkill -9 nvim

# 3. Проверим, не монтирует ли контейнер эту директорию
docker ps --format "table {{.Names}}\t{{.Mounts}}" | grep $(pwd)

# 4. Если swap-файл все еще не удаляется, проверь его права
ls -la .docker-compose.yml.swp
sudo rm -f .docker-compose.yml.swp  # с sudo если нужно

# 5. Последний вариант - проверь inode
ls -i .docker-compose.yml.swp
sudo lsof | grep 12345  # где 12345 - inode файла
```

- Как избежать этого в будущем:

1. Настрой Vim:
Создай файл `~/.vimrc`:

```vim
" Автоматически удалять swap-файлы при выходе
set shortmess+=A

" Хранить swap-файлы в отдельной директории
set directory=~/.vim/swap//
set backupdir=~/.vim/backup//
set undodir=~/.vim/undo//

" Создать директории если их нет
if !isdirectory(&directory) | call mkdir(&directory, "p") | endif
if !isdirectory(&backupdir) | call mkdir(&backupdir, "p") | endif
if !isdirectory(&undodir) | call mkdir(&undodir, "p") | endif
```

2. Используй nano или micro для Docker-файлов:
```bash
# Установи micro (удобный современный редактор)
sudo snap install micro  # или sudo apt install micro

# Используй его
micro docker-compose.yml
```

3. Правильный выход из Vim:

- Сохранить и выйти: `:wq` или `:x` или `ZZ`
- Выйти без сохранения: `:q!`
- **Не делай Ctrl+Z** - это отправляет Vim в фон, а не закрывает!

4. Если все же застрял в Vim:
``` text
# На случай если не знаешь как выйти из Vim:
# 1. Нажми Esc (чтобы выйти из режима вставки)
# 2. Набери :q! (выйти без сохранения)
# 3. Enter

# Или если нужно сохранить:
# 1. Esc
# 2. :wq
# 3. Enter
```

- Что делать прямо сейчас:
```bash
# 1. Закрой все Vim процессы
sudo pkill -9 vim
sudo pkill -9 nvim

# 2. Удали swap-файлы
rm -f .*.swp .*.swo .*.swn

# 3. Проверь что удалилось
ls -la

# 4. Открой файл заново
vim docker-compose.yml

# ИЛИ лучше используй nano если с Vim проблемы
nano docker-compose.yml
```

Если все еще не удаляется - перезапусти терминал или даже систему, иногда помогает.


## Очистка Ubuntu с Docker

```bash
# Очистим Build Cache 
docker builder prune -a -f

# Очистим неиспользуемые образы
docker image prune -a -f

# Очистим контейнеры которые не запущены
docker container prune -f

# Проверим что стало
docker system df
df -h

# Очистим кеш apt
sudo apt clean
sudo apt autoremove -y

# Очистим старые логи
sudo journalctl --vacuum-time=1d

# Проверим что занимает место на диске
sudo du -sh /* 2>/dev/null | sort -h | tail -20
```

- Про расширение диска VM (если Thin provisioned => Yes)

Можно расширить диск в ESXi, например с 60GB до 100GB, но нужно сделать ДВА ШАГА:

**Шаг 1:** В ESXi (через vSphere Client, или web интерфейс):

1. Выключи ВМ
2. Settings → Hard Disk 1 → Expand
3. Установи 100GB → OK
4. Запусти ВМ

**Шаг 2:** Внутри Ubuntu:
```bash
# 1. Установи утилиты для LVM если нет
sudo apt update
sudo apt install -y cloud-guest-utils

# 2. Проверим текущую структуру
lsblk
sudo pvs
sudo vgs
sudo lvs

# 3. Скорее всего у тебя LVM, поэтому:
# Расширим физический том
sudo growpart /dev/sda 3  # или какой у тебя раздел (проверь через lsblk)

# 4. Расширим LVM физический том
sudo pvresize /dev/sda3  # опять же, проверь номер

# 5. Расширим логический том
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv

# 6. Расширим файловую систему
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv

# 7. Проверим
df -h
```

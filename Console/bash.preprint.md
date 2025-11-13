аналоги netstat
sudo lsof -i -P
sudo ss -tulpn

Более информативные docker ps

docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}\t{{.Image}}"
docker ps -a --format "table {{.ID}}\t{{.Names}}\t{{.Status}}\t{{.Image}}"

docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Networks}}\t{{.Mounts}}"
docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Networks}}\t{{.Mounts}}"

docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Command}}\t{{.Ports}}"
docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Command}}\t{{.Ports}}"

docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}\t{{.Command}}}\t{{.Ports}}\t{{.Networks}}\t{{.Mounts}}\t{{.Image}}"


### HTOP — КАК ПОЛЬЗОВАТЬСЯ (КРАТКО)

```bash
htop
```

| Клавиша | Что делает |
|--------|-----------|
| **F3** | Поиск (введи `webui`, `python`) |
| **Пробел** | Пометить процесс |
| **F9** | Убить помеченный (`SIGKILL`) |
| **F5** | Дерево процессов |
| **F4** | Фильтр (введи `webui`) |
| **q** | Выход |

> **Твой кейс**: `F3` → `<процесс>` → `Пробел` → `F9` → `9` → Enter

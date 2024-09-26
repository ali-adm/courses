Введение в SQL
===

Данные могут быть мощным инструментом, но только если вы знаете, как ими пользоваться. В такой ситуации SQL незаменим! На этом курсе вы узнаете, как использовать стандартизированный язык баз данных SQL для доступа и манипулирования данными, хранящимися в базах данных. Когда вы научитесь использовать SQL, вы сможете работать в ведущих компаниях (и даже правительствах!), которые используют данные для прогнозирования и принятия

<a id="back"></a>
### Оглавление:



Начало работы
===

Работа с данными
---

- **SQL** позволяет вам работать с данными, хранящимися в базе данных
- Запрос **SELECT** используется для получения данных из таблицы.

В этом курсе вы научитесь использовать **SQL** для работы с данными и принятия более умных решений. Давайте использовать **SQL-код** для доступа к информации о фильмах.

**movies**
|title        |year|
|-------------|----|
|Home Alone   |1990|
|Star Wars    |1977|
|Jurassic Park|1993|

Выбор данных `year` из таблицы `movies`:
```sql
SELECT year FROM movies
```
Мы используем SQL-код для доступа к данным. Точно так-же из таблицы `movies` можно выбрать `title`:
```sql
SELECT title FROM movies
```
**movies**
| id |title        |year|
|----|-------------|----|
| 1  |Home Alone   |1990|
| 2  |Star Wars    |1977|
| 3  |Jurassic Park|1993|
| 4  |Frozen       |2013|

Данные находятся в базах данных. Практически каждая компания и организация полагаются на какую-либо форму базы данных для хранения и организации информации. **SQL** позволит вам взаимодействовать с данными, хранящимися в базе данных. 

**SQL-код** используется для отправки запросов к базе данных. Эти запросы называются так и называются - **запросы (queries)**.

Большинство баз данных собирают данные в таблицы. Таблицы организуют данные в:  
- строки **records (записи)**
- столбцы **fields (поля)**

**Record (строка)** содержит информацию о субъекте, таком как конкретный сотрудник, клиент или продукт, например фильм.

**Field (столбец)** содержит информацию о субъектах, таких как имя, электронная почта или год выпуска продукта.

Например таблица **movies**, та что выше, содержит четыре **record (строки)**, и три **field (столбца)**. 

Строка **header** - это **верхняя строка таблицы** и содержит названия разных полей (столбцов). (id, title, year - в табл. movies).

Команда **SELECT** используется для извлечения данных поля из таблицы.
```sql
SELECT year FROM movies
```

Выполнение Queries
---
- Данные могут быть классифицированы как **структурированные** или **неструктурированные**
- **SQL** используется для работы со **структурированными данными**.


Подумайте о своем любимом приложении или технологии. Вероятно, оно не смогло бы работать без данных. В этом уроке вы будете писать, тестировать и выполнять настоящий SQL-код.

Данные, которые могут быть сохранены в таблицах, называются **структурированными данными**.

**SQL** позволяет очень быстро и эффективно работать со структурированными данными. Одним **запросом - query** можно получить доступ к тысячам и тысячам записей в мгновение ока.

**Код Плейграунд**

Готовы написать, выполнить и протестировать настоящий код? Откройте **Код Плейграунд** для кода. Затем нажмите **"Run"**, чтобы получить запрошенные данные. В нашем случае мы просто будем приводить код для запуска здесь, и описывать его работу.
**movies**
| id |title        |year|
|----|-------------|----|
| 1  |Home Alone   |1990|
| 2  |Star Wars    |1977|
| 3  |Jurassic Park|1993|
| 4  |Frozen       |2013|
| 5  |Pirates of the Caribbean|2003|
Запрос к вышеприведенной таблице:
```sql
SELECT year FROM movies
```
Даст такой ответ:
|year|
|----|
|1990|
|1977|
|1993|
|2013|
|2003|

Запрос к таблице - приводит к созданию меньшей таблицы с запрошенными данными.

Реальные базы данных могут содержать очень большое количество информации. **Query (Запрос)** - это способ получить только интересующие вас данные.

**Неструктурированные данные** - это информация, которую сложно хранить в таблицах.

**SQL** означает **Structured Query Language** (язык структурированных запросов). С помощью **SQL** вы сможете извлекать данные из массивных наборов данных с тысячами полей и записей. **SQL** используется для работы со структурированными данными в виде таблиц.

Реляционные базы данных
---

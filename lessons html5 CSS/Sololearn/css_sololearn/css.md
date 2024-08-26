Sololearn CSS.
===

Наш курс CSS научит вас, как управлять стилем и версткой веб-сайтов. Вы выполните ряд упражнений и попрактикуетесь при заполнении реальных шаблонов CSS — так вы получите реальный опыт программирования, который укрепит вашу уверенность и поможет вам в реализации ваших собственных проектов!

Начало работы с CSS
---

- CSS используется для стилизации элементов на веб-странице. CSS - это язык стилизации, который работает вместе с HTML, чтобы придать странице ее вид и макет.
- CSS основан на HTML. Атрибут ```style``` позволяет вам использовать свойства CSS для настройки визуального представления элементов HTML.

Изменение цвета текста параграфа с помощью атрибута ```style```:
```html
<p style="color: green">Text</p>
```

Свойство ```color property``` используется для управления цветом текста. Код синего заголовка:
```html
<h1 style="color: blue">Main Menu</h1>
```

**CSS свойства** контролируют стиль HTML элементов. 

Примеры CSS свойств - это цвет, граница, размер шрифта и отступ. Увеличение текста в параграфе:
```html
<p style="font-size: large">Text</p>
```

**Свойства CSS** требуют ***значений***.

**Значения** - это возможные настройки для свойства. 
- CSS свойства и значения разделяются с помощью двоеточия ```:```, 
- CSS код для HTML элемента должен быть заключен в двойные ```""``` или одинарные ```''``` кавычки, следуя за атрибутом ```style```. 
- Чтобы применить несколько свойств к элементу, разделяйте CSS свойства с помощью точки с запятой ```;```.

**CSS** означает **Каскадные Таблицы Стилей** и является одной из трех основных веб-технологий. Каскадность относится к набору правил, которые будут изложены ниже.

- Структура: HTML
- Стиль: CSS
- Интерактивность: Java Screept

Код для центрированного заголовка с фоном green:
```html
<h1 style="text-align: center; background-color: green">Items</h1>
```


Техники стилизации
---

- **Inline CSS** используется для стилизации отдельных элементов HTML
- **Internal CSS** сгруппировывает все стили для страницы внутри тега ```<style>```
- **Selectors** используются для выбора элементов HTML

Добавление CSS кода к каждому HTML элементу занимает время и делает вашу HTML структуру неорганизованной. Существует альтернативный способ стилизации ваших страниц, который делает ваш CSS код более эффективным.

Можно добавить CSS код *внутри HTML элементов*, это называется **inline CSS - встроенный CSS**:
```html
<p style="color: gray">Text</p>
```
Встроенный CSS легко добавить в ваш код, но он имеет некоторые недостатки. Например, для применения одного и того же стиля к более чем одному HTML элементу - необходимо повторить код CSS.

Альтернативной техникой стилизации является **internal CSS - внутренний CSS**. Внутренний CSS используется для стилизации всей страницы. Тег-контейнер ```<style>``` добавляется в документ HTML, чтобы сгруппировать весь CSS код для страницы.
```html
<style>
  p {
    color: orchid;
  }
</style>
<body>
  <p>Explore the city.</p>
  <p>Discover hidden gems.</p>
  <p>Take a free tour.</p>
</body>
```
```<style>``` - контейнерный тег это значит, что он требует как открывающего, так и закрывающего тега ```</style>```.

Способ добавления CSS кода зависит от техники стилизации, которая используется. В индивидуальные HTML элементы добавляется **встроенный CSS код**.

Стиль, определенный в приведенном внутреннем CSS-коде, будет применен ко всем заголовкам третьего уровня на странице:
```html
<style>
  h3 {
    color: red;
    font-size: small;
  }
</style>
```

В данном случае ```h3``` - выступает в роли **Селектора.** Селектор в коде CSS соответствует HTML-тегам, которые нужно стилизовать. Селекторы используются с внутренним CSS. Например чтобы стилизовать кнопки на странице, нужно использовать селектор ```button```:
```css
button {
  color: green;
  }
```
Чтобы применить один и тот же стиль к различным элементам, нужно разделить несколько селекторов запятой. Это упрощает код CSS.
```html
<style>
  h1, p {
    color: black;
    background-color: yellow;
  }
</style>
```

Лучшей практикой считается включать весь внутренний CSS-код в <head> страницы.
```html
<head>
  <style>
    h1 {
      color: orchid;
      background-color: lime;
    }
    p {
      color: orchid;
    }
    button {
      font-size: large;
      color: lightyellow;
      background-color: orchid;
    }
  </style>
</head>
<body>
  <h1>Explore the city.</h1>
  <p>Discover hidden gems.</p>
  <button>Take a free tour</button>
</body>
```

Анатомия CSS
---

- Код CSS состоит из **правил стилизации**
- Правило состоит из селектора и набора деклараций
- Декларация состоит из пары **свойство: значение**

CSS контролирует все аспекты дизайна веб-страницы. Это включает в себя шрифты, размеры, цвета, позицию, расстояние, макет, анимации и многое другое.

CSS код создает **правила стилизации.** Простейшее правило стилизации состоит из **селектора**, плюс **объявление** в **фигурных скобках {}.**
```css
button {
  font-size: large;
  color: blue;
  }
```

Приведенный выше код, будет применять стили для всех кнопок на странице. Можно добавить столько объявлений, сколько нужно, аждое объявление должно заканчиваться на точку с запятой. Объявление состоит из двух частей: **property (свойства)** и **value (значения).** Свойство и значение внутри объявления всегда идут парами. Декларация состоит из пары **свойство: значение**. Пара **свойство: значение** в декларации отделяется двоеточием ```:```. 
CSS код может содержать столько стилевых правил, сколько нужно.

----обрыв записи------
---

Стилизация текста
---

- ```text-align``` контролирует горизонтальное выравнивание текста
-  ```text-decoration``` добавляет декоративные эффекты к тексту
-  ```text-transform``` изменяет написание текста
-  ```text-shadow``` применяет теневые эффекты за текстом

Еще одним важным элементом веб-дизайна является стилизация текста. 
```text-align: center``` - выравнивание текста (по аналогии - ```right```, ```left```)

Используйте ```text-align: justify``` для выравнивания текста по обоим краям, регулируя расстояние между словами, чтобы гарантировать, что каждая строка имеет одинаковую ширину
```
p {
  text-align: justify;
}
```

Можно добавить ```text-decoration``` (подчеркивание, надчеркивание, зачеркивание), чтобы передать смысл или привлечь внимание к определенным частям текста, например, к ссылкам.
```html
<html>
<body>
  <h1>Underlined text</h1>
  <h2>Overlined text</h2>
  <h3>Line-through text</h3>
  <h4>Underlined and overlined text</h3>
</body>
</html>
```
```css
body {
  background-color: #333333;
}
h1 {
  /*Underlined text*/
  text-decoration: underline;
  color: #F28D35;
}
h2 {
  /*Overlined text*/
  text-decoration: overline;
  color: #6BBE92;
}
h3 {
  /*Line-through text*/
  text-decoration: line-through;
  color: #D83367;
}
h4 {
  /*Underlined and overlined text*/
  text-decoration: underline overline;
  color: #149EF2;
}
```

Некоторые свойства CSS могут принимать несколько значений. Вы можете контролировать цвет декорации, добавив название цвета, rgb или hex-код после типа декорации.
```html
html>
  <body>
    <h1>My Personal Blog</h1>
    <h2 class="article-title">Adventures in New Zealand</h2>
    <p>During my trip to New Zealand, I had the chance to visit...</p>
    <h2 class="article-title">Gourmet Cooking on a Budget</h2>
    <p>Believe it or not, it's possible to cook gourmet meals without breaking the bank...</p>
  </body>
</html>
```
```css
body {
  background-color: #F3F4F6;
  color: #333333;
}
h1 {
  text-align: center;
  color: #555555;
}
.article-title {
  text-decoration: underline #FF4500;
  font-size: 24px;
}
```

Текстовое оформление может принимать различные стили, такие как точечный, двойной, пунктирный и волнистый.
```html
<body>
  <div class="container">
    <p class="double">
      This is a double underline.</p>
    <p class="dotted">
      This is a dotted underline.</p>
    <p class="dashed">
      This is a dashed underline.</p>
    <p class="wavy">
      This is a wavy underline.</p>
  </div>
</body>
```
```css
body {
  background-color: #000A23;
  color: #EDEDED;
}
p {
  font-size: 18px;
}
.double {
  text-decoration: double underline #E67112;
}
.dotted {
  text-decoration: underline dotted #2A9D8F;
}
.dashed {
  text-decoration: dashed underline #E76F51;
}
.wavy {
  text-decoration: wavy underline #62767E;
}
```

Свойство ```text-decoration``` - это короткий и простой способ ссылаться на различные подсвойства, такие как ```text-decoration-line```, ```text-decoration-color``` и ```text-decoration-style```.

```css
text-decoration: wavy overline #2A9D8F;

text-decoration-line: overline;
text-decoration-color: #2A9D8F;
text-decoration-style: wavy;
```

Свойство ```text-transform``` позволяет вам контролировать использование заглавных букв в текстовом контенте (каждое слово с заглавной, все заглавные и все строчные).
Оно может принимать 3 значения: ```capitalize```, ```uppercase``` и ```lowercase```.
```html
<html>
  <body>
    <p class="capitalize">
    this is a sentence with capitalize transformation.</p>
    <p class="uppercase">
     This is a sentence with uppercase transformation.</p>
    <p class="lowercase">
     THIS IS A SENTENCE WITH LOWERCASE TRANSFORMATION.</p>
  </body>
</html>
```
```css
.capitalize { 
  text-transform: capitalize; 
}
.uppercase { 
  text-transform: uppercase; 
}
.lowercase { 
  text-transform: lowercase; 
}
body{
  background-color: #000A23;
  color: white;
}
```

Например CSS правило для кнопки с текстом в верхнем регистре, размером шрифта 18px и зеленым фоном:
```css
button {
  text-transform: apitalize;
  background-color: green;
  font-size: 18px;
}  
```

Свойство ```text-shadow``` создает эффект глубины, придает выразительность или просто добавляет стильный акцент в вашу типографику.

Оно принимает два обязательных значения в следующем порядке: сначала горизонтальное смещение, затем вертикальное.
- Горизонтальное смещение - это насколько далеко вправо (положительные значения) или влево (отрицательные значения) будет тень.
- Вертикальное смещение - это насколько далеко вниз (положительные значения) или вверх (отрицательные значения) будет тень.

Как пример - применить теневой эффект текста со смещением в 5px вправо и 6px вверх:
```css
h1 {
  text-shadow: 8px 6px;
}
```

```text-shadow``` может принимать два дополнительных, необязательных значения.
- ```blur radius```: степень размытия, применяемая к тени
- ```color```: цвет тени
```html
<html>
  <body>
    <h1>Harry Potter</h1>
  </body>
</html>
```
```css
body {
  background-color: #1a1a1a;
}

h1 {
  color: #FFFFFF; /* white colored text */
  text-shadow: 4px 4px 4px #4296CE; 
  font-size: 4rem;
}
```

Важно сохранять правильный порядок значений для свойства ```text-shadow```, иначе оно может не дать желаемого эффекта.


Стили шрифтов
---

- ```font-family``` позволяет вам указывать тип шрифта

- вы можете использовать ```font-weight``` для контроля толщины текста

Шрифты играют важную роль в веб-дизайне, влияя на читаемость, эстетику и пользовательский опыт. Они оживляют слова на странице и задают тон содержимого.

Свойство ```font-family``` в CSS позволяет вам указать **шрифт** для вашего текста. Это определяет, как текст выглядит на веб-странице.
```html
<body>
  <p id="font-georgia">Georgia</p>
  <p id="font-arial">Arial</p>
  <p id="font-courier">Courier New</p>
  <p id="font-comic">Comic Sans MS</p>
</body>
```
```css
body {
  background-color: #000A23;
  font-size: 24px;
  color: #FFFFFF;
}
#font-georgia {
  font-family: Georgia;
}
#font-arial {
  font-family: Arial;
}
#font-courier {
  font-family: "Courier New";
}
#font-comic {
  font-family: "Comic Sans MS";
}
```

Многие шрифты установлены по умолчанию на всех устройствах. Они известны как **веб-безопасные** шрифты.

Другие шрифты могут потребовать установки на устройстве пользователя, поэтому вам нужно указать веб-безопасный шрифт в качестве запасного, на случай, если у пользователя их нет.
```html
<html>
<body>
  <h2 id="font1">Daily Brews</h2>
  <h2 id="font2">Daily Brews</h2>
  <h2 id="font3">Daily Brews</h2>
  <h2 id="font4">Daily Brews</h2>
</body>
</html>
```
```css
/*некоторые веб-безопасные шрифты:
Arial, Courier New, Times New Roman,
Trebuchet MS, Verdana
*/
#font1 {
  font-family: Georgia;
}
#font2 {
  font-family: Tahoma;
}
#font3 {
  font-family: Lucida Console;
}
#font4 {
  font-family: Comic Sans MS;
}
/* Вот еще веб-безопасные шрифты, которые вы можете попробовать: Arial, Courier New, Times New Roman, Trebuchet MS, Verdana */
```

Свойство ```font-family``` указывает список шрифтов, от самого приоритетного до наименее приоритетного. Выбор шрифта останавливается на первом шрифте в списке, который есть в системе пользователя.

Например, если ```Helvetica``` недоступен браузер сначала пробует ```Georgia```, затем семейства шрифтов ```Arial```:
```css
p {
  font-family: Helvetica, Georgia, Arial;
}
```

**Обобщенные семейства шрифтов** - это группы шрифтов с похожими начертаниями, и они используются в качестве универсальных резервных вариантов. Это лучшая практика, чтобы помещать их в качестве последнего варианта в свойстве font-family. Если предпочтительные шрифты недоступны, браузеры будут использовать шрифт из этого семейства.

Ниже приведен код пяти общих обобщенных семейств шрифтов:
```html
<body>
  <h2 class="serif-font">This is a serif font.</h2>
  <h2 class="sans-serif-font">This is a sans-serif font.</h2>
  <h2 class="monospace-font">This is a monospace font.</h2>
  <h2 class="cursive-font">This is a cursive font.</h2>
  <h2 class="fantasy-font">This is a fantasy font.</h2>
</body>
```
```css
.serif-font {
  /*Шрифты имеют декоративные
  штрихи или засечки.*/
  font-family: serif;
}
.sans-serif-font {
  /*В шрифтах отсутствуют 
  декоративные штрихи.*/
  font-family: sans-serif;
}
.monospace-font {
  /*Шрифты имеют одинаковый 
  интервал между символами.*/
  font-family: monospace;
}
.cursive-font {
  /*Шрифты имитируют почерк для 
  придания персонального или 
  художественного штриха.*/
  font-family: cursive;
}
fantasy-font {
  /*Декоративные или уникальные шрифты, 
  которые не подходят ни в одну 
  другую категорию.*/
  font-family: fantasy;
}
body {
  background-color: #0C1527;
  color: #FFFFFF;
}
```

Используйте кавычки для обертывания названий шрифтов, состоящих из нескольких слов. Это хорошая практика. 
```css
p {
  font-family: "Courier New", Monaco, monospace;
}
```

Свойство ```font-weight``` контролирует толщину (или жирность) шрифта (или текста).
```css
.button {
  font-weight: 500;
}
```

Можно использовать числовые значения от **100** (самый тонкий) до **900** (самый жирный) для указания веса шрифта, увеличивая на **100 единиц**.
```html
<body>
  <p id="light">This is light text.</p>
  <p id="normal">This is normal text.</p>
  <p id="bold">This is bold text.</p>
  <p id="bolder">This is bolder text.</p>
</body>
```
```css
p {
  font-family: Arial, sans-serif;
  font-size: 1.5em;
}
#light {
  font-weight: 100;
}
#normal {
  font-weight: 400;
}
#bold {
  font-weight: 700;
}
#bolder {
  font-weight: 900;
}
```

Пример - выравнивание текста по левому краю, размер шрифта 22px и вес 300
```css
p {
  text-align: left;
  font-size: 22px;
  font-weight: 300;
}
```

Некоторые значения веса, такие как **400** и **700**, имеют именованные эквиваленты, которые можно использовать непосредственно в качестве значений: **normal** и **bold**.

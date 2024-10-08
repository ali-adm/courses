# JavaScript – Средний уровень

Вы уже знакомы с основами JavaScript и хотели бы пополнить свои знания? Тогда вы в правильном месте. На этом курсе вы научитесь создавать более сложные и гибкие программы, а также ещё более интерактивные сайты. Этот курс является продолжением нашего курса Введение в Javascript. Мы рекомендуем вам ознакомиться содержанием курса "Введение в Javascript", прежде чем начать этот курс.

<a name="back"></a>
### Оглавление:
### [Объекты](#obj)
#### [Введение в объекты](#intro_obj)
#### [Создание cобственных Объектов](#oun_obj)
#### [Приземлились! (практика)](#pract_1)
#### [Инициализация объекта](#init_obj)
#### [Добавление методов](#add_methods)
#### [Расчет скидки (практика)](#discount_calc)
#### [ipsum](#lorem)
#### [ipsum](#lorem)
#### [ipsum](#lorem)
#### [ipsum](#lorem)
#### [ipsum](#lorem)
#### [ipsum](#lorem)
#### [ipsum](#lorem)
#### [ipsum](#lorem)
#### [ipsum](#lorem)




<a name="obj"></a>
# Объекты

### [Назад к оглавлению](#back)


<a name="intro_obj"></a>
## Введение в объекты

### Объекты JavaScript
Переменные JavaScript являются контейнерами для значений данных. 

**Объекты** также являются переменными, но они могут содержать много значений.

Считайте объект списком значений, которые записаны как пары `имя:значение`, где имена и значения разделены двоеточиями.

Пример:
```js
var person = {
 name: "John", age: 31, 
 favColor: "green", height: 183
};
```
Эти значения называются **properties**.

![properties](https://lecontent.sololearn.com/material-images/2386c565169d4902b10c39ecc16368fe-2765.png)

Относительно объекта, `color`, `height`, `weight` и `name` являются примерами **свойства**.

### Свойства объекта
Вы можете получить доступ к свойствам объекта двумя способами.
```js
objectName.propertyName
//or
objectName['propertyName']
```
Этот пример демонстрирует, как получить доступ к `age` нашего объекта person.
```js
var age = person.age /* проверить позже */
```

Встроенное свойство <b>length</b> в JavaScript используется для подсчета количества символов в свойстве или строке.
```js
var course = {name: "JS", lessons: 41};
document.write(course.name.length);
```

Объекты являются одной из основных концепций в JavaScript.

### Методы объекта
**Метод объекта** - это свойство, содержащее **определение функции**.

Используйте следующий синтаксис для доступа к методу объекта.
```js
objectName.methodName()
```
Как вы уже знаете, <b>console.log()</b> регистрирует текст в консоли. Функция <b>log()</b> на самом деле является методом объекта <b>console</b>.
```js
console.log("This is some text");
```
**Методы** - это функции, которые хранятся в качестве свойств объекта.

### Объем кубоида (практика)

ПРАКТИЧЕСКОЕ УПРАЖНЕНИЕ

#### Введение в объекты
Данный класс представляет собой параллелепипед (например, прямоугольный), который содержит свойства длины, ширины и высоты.

Дополните программу, чтобы рассчитать и вывести в консоль объем данного параллелепипеда.

>> Подсказка: чтобы вычислить объем параллелепипеда, используйте формулу `length*width*height`.
```js
var cuboid = {
    length: 25,
    width: 50,
    height: 200
};

//your code goes here

console.log(cuboid.length * cuboid.width * cuboid.height)
```

Доступ к свойству <b>color</b> объекта <b>hair</b> используя синтаксис с точкой:
```js
hair.color
```

### [Назад к оглавлению](#back)


<a name="oun_obj"></a>
## Создание cобственных Объектов

### Конструктор объекта
В предыдущем уроке мы создали объект, используя **синтаксис литерала** (или инициализатора) объекта (объектный литерал).
```js
var person = {
  name: "John", age: 42, favColor: "green"
};
```
>> **Литерал** — это фиксированное значение, которое напрямую указывается в коде программы. Это может быть число, строка, логическое значение или объект, которое не требует вычисления или вызова функций.
>>
>> - Числовой литерал: 42
>> - Строковый литерал: "Hello, World!" или 'Hello, World!'
>> - Булевый литерал: true или false
>> - Объектный литерал: { name: "John", age: 42 }

Это позволяет вам создать только один объект.

Иногда нам нужно установить **"тип объекта"**, который может быть использован для создания нескольких объектов одного типа.

Стандартный способ создания "типа объекта" - использовать функцию **конструктора объекта**.
```js
function person(name, age, color) {
  this.name = name;
  this.age = age;
  this.favColor = color;
}
```
Вышеуказанная функция (<b>person</b>) является конструктором объекта, который принимает параметры и присваивает их свойствам объекта.

> Подсказка: ключевое слово **this** относится к **текущему объекту**.
>
> Обратите внимание, что this не является переменной. Это ключевое слово, и его значение не может быть изменено.

Пример создания функции конструктора:
```js
function movie(title, director) {
  this.title = title;
  this.director = director;
}
```

### Создание объектов
Как только у вас есть конструктор объектов, вы можете использовать ключевое слово **new** для создания новых объектов того же типа.
```js
function person(name, age, color) {
    this.name = name;
    this.age = age;
    this.favColor = color;
}

var p1 = new person("John", 42, "green");
var p2 = new person("Amy", 21, "red");

document.write(p1.age); 
```
> `p1` и `p2` теперь являются объектами типа <b>person</b>. Их свойства присваиваются соответствующим значениям.

Для создания экземпляра объекта используется ключевое слово - **new**.

### Создание объектов
Рассмотрим следующий пример.
```js
function person (name, age) {
    this.name = name;
    this.age = age;
}
var John = new person("John", 25);
var James = new person("James", 21);

document.write(John.age);
```
Доступ к свойствам объекта осуществляется с использованием **синтаксиса с точкой**, как вы делали это ранее.
![prop](https://lecontent.sololearn.com/material-images/b04e074ca656477cb0e961e056a5bed1-2766.png)

> Понимание создания объектов является важным.

### [Назад к оглавлению](#back)


<a name="pract_1"></a>
### Приземлились! (практика)

ПРАКТИЧЕСКОЕ УПРАЖНЕНИЕ

### Создание собственных объектов
Боба наняли информационным офицером аэропорта, и ему нужно генерировать статусные сообщения для каждого рейса. Давайте поможем ему!

Дополните данную программу, исправив конструктор, создав объект рейса и присвоив его данной переменной, чтобы правильно выполнить соответствующее сообщение.

ID рейса и статус рейса (приземлился, вовремя, задержка и т.д.) принимаются в качестве входных данных.

```js
Пример ввода:
NGT 929
приземлился

Пример вывода:
Flight NGT 929 has landed
```
> Используйте ключевое слово <b>new</b> для создания нового объекта с использованием конструктора.

Оригинальный код:
```js
function main() {
    //take flight number and its status
    var flightNumber = readLine();
    var flightStatus = readLine();
    
    var flight1;
    //assign a flight object to flight1 variable
    
    //output
    console.log('The flight ' + flight1.number + ' is ' + flight1.status)
    
}

function Flight(flightNumber, status) {
    //fix the constructor
    number = flightNumber;
    status = status;
};
```

### Решение от GPT-4o
<spoiler title="Решение от GPT-4o">

Окей, давай разберем твою задачу шаг за шагом и объясню, что нужно сделать.

### 1. **Ошибка в конструкторе**
В конструкторе функции `Flight` у тебя объявлены переменные `number` и `status`, но они не привязаны к объекту, который создается с помощью этого конструктора. В JavaScript, чтобы создать свойства объекта внутри конструктора, нужно использовать ключевое слово `this`.

### 2. **Исправляем конструктор**
Когда создается объект с помощью `new Flight(...)`, нам нужно привязать свойства `number` и `status` к самому объекту, используя `this`. Это позволит обращаться к этим свойствам у объекта.

Вот как нужно исправить:

```js
function Flight(flightNumber, status) {
    this.number = flightNumber; // Привязываем параметр к объекту через this
    this.status = status;       // То же самое со статусом
}
```

Теперь свойства `number` и `status` станут частью объекта, который мы создадим через `new Flight()`.

### 3. **Создание объекта**
Теперь, когда конструктор исправлен, можно создать объект рейса и присвоить его переменной `flight1`.

```js
var flight1 = new Flight(flightNumber, flightStatus);
```

Это создаст новый объект `flight1`, где:
- `flight1.number` будет равно значению `flightNumber`
- `flight1.status` будет равно значению `flightStatus`

### 4. **Окончательный код**
Теперь соберем всё вместе:

```js
function main() {
    //take flight number and its status
    var flightNumber = readLine();
    var flightStatus = readLine();
    
    // Создаем объект рейса, используя конструктор
    var flight1 = new Flight(flightNumber, flightStatus);
    
    // Выводим сообщение с использованием свойств объекта
    console.log('The flight ' + flight1.number + ' is ' + flight1.status);
}

function Flight(flightNumber, status) {
    // Привязываем свойства к объекту через this
    this.number = flightNumber;
    this.status = status;
}
```

### 5. **Объяснение для чайника**

- **Конструктор `Flight`** — это как шаблон для создания объекта рейса. Когда ты создаёшь объект (например, `flight1`), конструктор берет параметры (номер рейса и статус) и сохраняет их в свойствах объекта с помощью `this`.
  
  `this.number = flightNumber` означает: «В объекте, который сейчас создаётся, создай свойство `number` и присвой ему значение переменной `flightNumber`».

- **Создание объекта `flight1`** через `new Flight(...)` означает: «Создай новый объект рейса, используя указанный номер рейса и статус».

- **`flight1.number`** и **`flight1.status`** — это свойства объекта `flight1`, к которым мы можем обращаться и выводить их значения.

Теперь программа будет выводить корректное сообщение о статусе рейса!
</spoiler>

### Продолжение урока. Создание объектов
Рассмотрим следующий пример.
```js
function person (name, age) {
    this.name = name;
    this.age = age;
}
var John = new person("John", 25);
var James = new person("James", 21);

document.write(John.age);
```
Доступ к свойствам объекта осуществляется с использованием синтаксиса с точкой, как вы делали это ранее.

![table](https://lecontent.sololearn.com/material-images/b04e074ca656477cb0e961e056a5bed1-2766.png)

> Понимание создания объектов является важным.

В качестве примера - два компонента необходимых для использования информации, содержащейся в объекте:
- имя объекта
- имя свойства

### [Назад к оглавлению](#back)


<a name="init_obj"></a>
## Инициализация объекта

Используйте синтаксис **объектного литерала** или **инициализатора** для создания отдельных объектов.
```js
var John = {name: "John", age: 25};
var James = {name: "James", age: 21};
```

Объекты состоят из свойств, которые используются для описания объекта. Значения свойств объекта могут содержать как примитивные типы данных, так и другие объекты.
```js
simba = {
    category: "lion", 
    gender: "male"
}
```

### Использование инициализаторов объектов

Пробелы и переносы строк не важны. Определение объекта может занимать несколько строк.

 Независимо от того, как создан объект, синтаксис для доступа к свойствам и методам не меняется.
```js
var John = {
    name: "John",
    age: 25
};
var James = {
    name: "James",
    age: 21
};

document.write(John.age);
//альтернатива: document.write(John['age']);
```

Код выше отобразит 25. Не заывайте об альтернативном способе доступа к свойству объекта: `document.write(John['age']);`.

Например следующее выражение отобразит свойство <b>category</b> объекта <b>simba</b> на экране:
```js
document.write(simba.category);
```

### [Назад к оглавлению](#back)


<a name="add_methods"></a>
## Добавление методов

### Методы - это функции, которые хранятся в свойствах объекта. 

Используйте следующий синтаксис для создания метода объекта:
```js
methodName = function() { code lines }
```

Доступ к методу объекта осуществляется с использованием следующего синтаксиса:
```js
objectName.methodName()
```

**Метод** - это функция, принадлежащая объекту. Она может быть вызвана с использованием ключевого слова **this**. 

Ключевое слово **this** используется как **ссылка на текущий объект**, что означает, что вы можете получить доступ к свойствам и методам объекта, используя его.

Определение методов производится внутри функции-конструктора.
```sql
function person(name, age) {
    this.name = name;  
    this.age = age;
    this.changeName = function (name) {
        this.name = name;
    }
}

var p = new person("David", 21);
p.changeName("John");

document.write(p.name);
```

В приведенном выше примере мы определили метод с именем `changeName` для нашего `person`, который является функцией, принимающей параметр `name` и присваивающей его свойству `name` объекта.

`this.name` относится к свойству `name` объекта.

>> Метод <b>changeName</b> изменяет свойство `name` объекта на его аргумент.

### [Назад к оглавлению](#back)


<a name="discount_calc"></a>
## Расчет скидки (практика)

ПРАКТИЧЕСКОЕ УПРАЖНЕНИЕ

### Добавление методов
  

Менеджеру магазина нужна программа для установки скидок на товары.  Программа должна принимать ID продукта, цену и скидку в качестве ввода и выводить цену со скидкой. Однако метод <b>changePrice</b>, который должен рассчитывать скидку, неполный. Исправьте это!
```js
Пример ввода
LD1493
1700
15

Пример вывода
LD1493 цена: 1700
LD1493 новая цена: 1445
```
> Подсказка: первый ввод - это ID продукта, второй - цена до скидки, а третий - процент скидки.
>
>Так что после применения скидки новая цена будет 1700-(0.15*1700) = 1445.
```js
function main() {
    var prodID = readLine();
    var price = parseInt(readLine(),10);
    var discount = parseInt(readLine(),10);
    
    var prod1= new Product(prodID, price);
    console.log(prod1.prodID + " price: " + prod1.price);
    
    prod1.changePrice(discount);
    console.log(prod1.prodID + " new price: " + prod1.price);
}

function Product(prodID, price) {
    this.prodID = prodID;
    this.price = price;

    this.changePrice = function(discount) {
        //your code goes here
        
    }
}
```


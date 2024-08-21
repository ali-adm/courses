class Person {
    constructor(name, age, happynes) {
        this.name = name;
        this.age = age;
        this.happynes = happynes;
    }

    info() {
        console.log("Человек: " + this.name + ", Возраст: " + this.age + ", Состояние удовлетворенности: " + this.happynes);
    }
}

var alex = new Person('Alex', 45, true);
var bob = new Person('Bob', 25, false);

bob.happynes = true

alex.info();
bob.info();

console.log(alex.happynes);
console.log(bob.happynes);

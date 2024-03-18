class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self):
        print("Hello")

class Dog(Animal):
    def __init__(self, breed, name, age, sex):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        print("Hau hau")


class Cat(Animal):
    def __init__(self, breed, name, age, sex):
        super().__init__(name,age,sex)
        self.breed = breed

    def sound(self): print("Miau")



dog = Dog("Czarny", "<NAME>", 18, "male")
dog.sound()
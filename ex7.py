class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def sound(self):
        print(self.name,"is barking")


pimpek = Dog("Pimpek", 12, "gray").sound()
dingo = Dog("Dingo", 3, "white").sound()
barry = Dog("Barry", 10, "black").sound()
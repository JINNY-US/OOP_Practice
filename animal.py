class Animal:
    def __init__(self,name, age):
        self.name = name
        self.age=age
    def speak(self):
        print("Animals")
    
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
    def speak(self):
        print("댕댕")

class Cat(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
    def speak(self):
        print("애옹")

cute_dog = Dog("초코","3")
cute_dog.speak()

cute_cat = Cat("애기","1")
cute_cat.speak()

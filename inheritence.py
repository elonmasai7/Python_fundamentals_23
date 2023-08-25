# inheritance allows one class to inherit attibutes
# and methods from another class
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"
# this are objects
doggy=Dog("Buddy")
cat=Cat("Whiskers")
print(doggy.speak())
print(cat.speak())


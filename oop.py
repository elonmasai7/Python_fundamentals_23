# A class is a blueprint for creating object
# Objects are instances of a class

class Students:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def sayhello(self):
        print("My name is ", self.name, "im ", self.age, "years ", self.gender)

# creating anobject
myobje = Students("Erick", "Male", 30)

myobje.sayhello()

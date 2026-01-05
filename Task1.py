class Person:
    def __init__(self):
        self.__name = "Mitul"
        self.__age = 25
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age

person = Person()
print(person.get_name())
print(person.get_age())
person.set_name("Mitul1")
person.set_age(26)
print(person.get_name())
print(person.get_age())


class Animal:
    def speak(self):
        print('I don\'t know what sound i make')

class Dog(Animal):
    def speak(self):
        print('woof')

class Cat(Animal):
    def speak(self):
        print('meow')

animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()
dog.speak()
cat.speak()


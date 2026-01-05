class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

person=Person("Mitul",25)
student=Student("Mitul1",25,10)
print(person.name)
print(person.age)
print(student.name)
print(student.age)
print(student.grade)
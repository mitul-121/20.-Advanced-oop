class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)

class manager(employee):
    def __init__(self,name,age,position):
        self.name = name
        self.age = age
        self.position = position
    def get_poisition(self):
        print(self.position)

class engeener(employee):
    def __init__(self,name,age,specialty):
        self.name = name
        self.age = age
        self.specialty = specialty
    def get_specialty(self):
        print(self.specialty)

class intern(employee):
    def __init__(self,name,age,duration):
        self.name = name
        self.age = age
        self.duration = duration
    def get_duration(self):
        print(self.duration)

m1 = manager("A",30,"Head Manager")
m1.display()
m1.get_poisition()
e1 = engeener("B",25,"Java developer")
e1.display()
e1.get_specialty()
i1 = intern("C",25,"3 months")
i1.display()
i1.get_duration()

class Vehicle:
    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):
    def start(self):
        print("Car engine starting")

    def stop(self):
        print("Car comes to stop")

class Truck(Vehicle):
    def start(self):
        print("Truck engine starts")

    def stop(self):
        print("Truck slowly stop")


class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle revs up")

    def stop(self):
        print("Motorcycle comes to stop")

vehicle = Vehicle()
vehicle.start()
vehicle.stop()
car = Car()
car.start()
car.stop()
truck = Truck()
truck.start()
truck.stop()
motorcycle = Motorcycle()
motorcycle.start()
motorcycle.stop()

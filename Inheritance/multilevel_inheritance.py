class Vehicle:
    def start(self):
        print("Vehicle is Starting")

class Car(Vehicle):
    def drive(self):
        print("Drive car")

class ElectricCar(Car):
    def charge(self):
        print("Electric car need to be charged")

electric_car = ElectricCar()
electric_car.charge()
electric_car.drive()
electric_car.start()


class Vehicle:
    speed=0
    def __init__(self,speed):
        self.speed=speed
        print(" Rahma has a vehicle")
    
class Car(Vehicle):
    brand=''
    def __init__(self,speed,brand):
        self.brand=brand
        Vehicle.__init__(self, speed)

    def display(self):
        print(self.speed)
        print(self.brand)

r1= Car(1000000,"kia")
r1.display()
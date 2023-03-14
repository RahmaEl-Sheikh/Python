from abc import ABC, abstractmethod
class Animal:
    @abstractmethod
    def speak():
        pass
        
class Dog(Animal):
    def speak(self):
        print("dog sound")

class Cat(Animal):
    def speak(self):
        print("cat sound")

d1=Dog()
c1=Cat()
d1.speak()
c1.speak()
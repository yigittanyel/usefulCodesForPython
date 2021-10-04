#Abstract sınıflardan obje oluşturulamaz,initiliaze edilemez ve abstract sınıftaki metotlar sub sınıfta muhakkak kullanılmak zorundadır.

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def run(self): pass
    @abstractmethod
    def walk(self):pass

class Bird(Animal):
    def __init__(self):
        print("Bird")
    def run(self):
        print("run")
    def walk(self):
        print("walk")

b1=Bird()
b1.walk()
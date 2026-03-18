from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self):
        pass

    @abstractmethod
    def run(self) :
        pass

    @abstractmethod
    def __str__(self):
        pass

class Taxi(Vehicle) :
     def run(self) :
        print('택시 달리다')

     def __str__(self):
             return '자식 클래스 택시'

class Bus(Vehicle) :
     def run(self) :
        print('버스 달리다')

     def __str__(self):
             return '자식 클래스 버스'
   
class Truck(Vehicle) :
    def run(self) :
        print('트럭 달리다')

    def __str__(self):
             return '자식 클래스 트럭'
    


taxi = Taxi()
bus = Bus()
truck = Truck()

print(taxi)
taxi.run()
print(bus)
bus.run()
print(truck)
truck.run()


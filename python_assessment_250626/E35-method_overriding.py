class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def fuel_type(self):
        return "Petrol"    

class ElectricCar(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        
    def fuel_type(self):
        return "Electricity" 

car = ElectricCar("Tesla")  
print(car.brand,car.fuel_type())        
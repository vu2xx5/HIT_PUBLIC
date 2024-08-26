class Vehicle():
  def __init__(self, make):
    self.make = make
  def description(self):
    return f"Thông tin phương tiện {self.make}"

class Car(Vehicle):
  def __init__(self, make, model):
    super().__init__(make)
    self.model = model
  def description(self):
    return f"Thông tin ô tô {self.model} và thương hiệu {self.make}"

class ElectricCar(Car):
  def __init__(self, make, model, battery_size):
    super().__init__(make, model)
    self.battery_size = battery_size
  def description(self):
    return f"Thông tin ô tô điện {self.model} thương hiệu {self.make} có dung lượng pin {self.battery_size}"

Vin=Vehicle("Vinfast")
Car1=Car("Vinfast", "VF3")
Car2= ElectricCar("Vinfast","VF3",3000)
print(Vin.description())
print(Car1.description())
print(Car2.description())
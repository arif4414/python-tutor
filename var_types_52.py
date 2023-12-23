class Car:
    wheels = 4 # class or static var
    # def __init__(self):
    #     self.brand = 'toyota' # instance var
    #     self.make = 'rav4'


#carObj1 = Car()
carObj2 = Car()
carObj2.brand = 'honda'
carObj2.make = 'odyssey'

Car.wheels = 6 # updating the class variable

#print('car1: ', carObj1.brand, carObj1.make, carObj1.wheels)
print('car2: ', carObj2.brand, carObj2.make, carObj2.wheels)

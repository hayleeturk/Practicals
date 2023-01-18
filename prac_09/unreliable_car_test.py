"""CP1404 Practical 9 - Unreliable Car test"""

from prac_09.unreliable_car import UnreliableCar

new_unreliable_car = UnreliableCar("Toyota", 50, 60.5)
new_unreliable_car.drive(25)
print("Unreliable car:", new_unreliable_car.name)
print(f"Drove: {new_unreliable_car.odometer}km")

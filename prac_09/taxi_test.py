"""CP1404 Practical 9 - Taxi Test"""

from prac_09.taxi import Taxi

# Create new taxi object
my_taxi = Taxi("Prius 1", 100, 1.23)
# Drive the taxi 40 km
my_taxi.drive(40)
# Print the taxi's details and the current fare
print(my_taxi)
print("Current fare: ", my_taxi.get_fare())
# Restart the meter (start a new fare) and then drive the car 100 km
my_taxi.start_fare()
my_taxi.drive(100)
# Print the details and the current fare
print(my_taxi)
print("Current fare: ", my_taxi.get_fare())
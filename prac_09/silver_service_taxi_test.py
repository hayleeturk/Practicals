"""CP1404 Practical 9 - Silver Service Taxi Tests"""

from prac_09.silver_service_taxi import SilverServiceTaxi

new_silver_taxi = SilverServiceTaxi("Cab", 50, 5)
print(new_silver_taxi)

# 18 km trip in a SilverServiceTaxi with fanciness of 2, the fare should be $48.78

new_silver_taxi = SilverServiceTaxi("Hummer", 100, 2)
new_silver_taxi.drive(18)
print(new_silver_taxi)
print("Fare cost: $", new_silver_taxi.get_fare())
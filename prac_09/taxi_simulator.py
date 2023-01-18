"""CP1404 Practical 9 - Taxi Simulator"""

from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "(Q)uit, (C)hoose taxi, (D)rive"


def main():
    """Taxi simulator program with classes."""
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "D":
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("Drive how far?: "))
                current_taxi.drive(distance)
                current_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${current_cost:.2f}")
                total_cost += current_cost
            else:
                print("Choose a taxi before you drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Print taxis information."""
    for i, taxi in enumerate(taxis):
        print(i, taxi, sep=" - ")


if __name__ == '__main__':
    main()

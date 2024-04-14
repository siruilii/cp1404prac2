from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):

    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def main():
    print("Let's drive!")
    current_taxi = None
    bill_to_date = 0
    taxis = [Taxi("Prius", 100, 1.23), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    while True:
        print(f"Bill to date: ${bill_to_date:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == "q":
            print(f"Total trip cost: ${bill_to_date:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break

        elif choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            choice = int(input("Choose taxi: "))
            if 0 <= choice < len(taxis):
                current_taxi = taxis[choice]
                print(f"Bill to date: ${bill_to_date:.2f}")
            else:
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                bill_to_date += trip_cost

if __name__ == "__main__":
    main()

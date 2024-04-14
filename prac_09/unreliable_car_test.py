from unreliable_car import UnreliableCar  # Import the UnreliableCar class from unreliable_car.py

def main():

    my_unreliable_car = UnreliableCar("Unreliable Car", 100, 50)  # 50% reliability


    distance_driven = my_unreliable_car.drive(10)


    print(f"Distance driven: {distance_driven}")

if __name__ == '__main__':
    main()

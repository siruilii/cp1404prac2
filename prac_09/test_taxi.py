from  taxi import Taxi
def main():

    my_taxi = Taxi("Prius 1", 100, 1.23)

    my_taxi.drive(40)

    print(" after driving 40 km:")
    print(my_taxi)
    print()

    my_taxi.start_fare()
    my_taxi.drive(100)

    print("Taxi details afterdriving 100 km:")
    print(my_taxi)

if __name__ == '__main__':
    main()

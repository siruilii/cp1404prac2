from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, price_per_km, fanciness):
        super().__init__(name, fuel, price_per_km * fanciness)
        self.fanciness = fanciness

    def get_fare(self):

        return super().get_fare() + self.flagfall

    def __str__(self):

        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

# Test code
def test_silver_service_taxi():

    my_silver_taxi = SilverServiceTaxi("Hummer", 200, 2.46, 4)

    my_silver_taxi.drive(18)

    fare = my_silver_taxi.get_fare()

    assert fare == 48.78

if __name__ == "__main__":
    test_silver_service_taxi()
    print("All tests passed!")

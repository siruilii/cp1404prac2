class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        current_year = 2024
        return current_year - self.year


def test_guitar_methods():

    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)


    expected_age = 102
    age = guitar1.get_age()
    print(f"{guitar1.name} get_age() - Expected {expected_age}. Got {age}")


test_guitar_methods()

MIN_BONUS=0.1
MAX_BONUS=.15
sales = 0
while sales >= 0:
    sales = float(input("YOUR sales is: $"))

    if sales < 1000:
        bonus = sales * MIN_BONUS
    else:
        bonus = sales * MAX_BONUS
    print(f"Bonus is: ${bonus}")
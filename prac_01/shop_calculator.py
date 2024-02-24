total_price = 0
number = 0
number = int(input("Number of items: "))
while number <= 0:
    print("Invalid number !")
    number = int(input("Number of items: "))
for i in range(1, number + 1):
    price = float(input("Price of item: $"))
    total_price += price
if total_price > 100:
    total_price *= 0.9

print(f"Total price for {number} items is : ${total_price:.2f}")
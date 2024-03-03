#1
user_name = input("Enter your name: ")
with open("name.txt", 'w') as file:
    file.write(user_name)

# 2
with open("name.txt", 'r') as file:
    name = file.read()
    print(f"Your name is {name}")

# 3
with open("numbers.txt", 'r') as file:
    number=0
    number1 = int(file.readline())
    number += number1
    print(number)

# 4
total = 0
with open("numbers.txt", 'r') as file:
    for line in file:
        number = int(line)
        total += number
    print(total)
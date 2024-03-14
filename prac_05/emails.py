users = {}

while True:
    email = input("Email: ")
    if email == "":
        break

    name = email.split('@')[0].split('.')

    yes_or_no = input(f"Is your name {name}? (Y/n) ").lower()

    if yes_or_no == "n":
        name = input("Name: ").title()

    users[email] = name

for email, name in users.items():
    print(f"{name} ({email})")
PASSWORD_LENGTH = 10
def main():
    password = get_password()
    print_password(password)

def get_password():
    password = input("Your password is: ")
    while len(password) < PASSWORD_LENGTH:
        print("Your password is wrong")
        password = input("Your password is: ")
    return password


def print_password(password):
    print("*" * len(password))

main()

def main():
    menu = ["(G)et a valid score", "(P)rint result", "(S)how stars", "(Q)uit"]
    score = get()
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        print(menu)
        if choice == "G":
            score = get()
        elif choice == "P":
            print(score)
        elif choice == "S":
            stars(score)
        elif choice == "Q":
            print("QUIT!")
        else:
            print("Invalid choice. ")
def get():
    score = int(input("Enter a score (0-100): "))
    while score < 0 or score > 100:
        score = int(input("Enter a score (0-100): "))
    return score

def result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
def print(score):
    results =result(score)
    print(f" {score} is {results}.")

def stars(score):
    print("*" * score)



main()
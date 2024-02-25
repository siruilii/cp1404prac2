import random


def main():
    user_score = get_score()
    result = level(user_score)
    print(result)
    random_score = random.randint(0, 100)
    print("Random score:", random_score)
    result = level(random_score)
    print(result)


def get_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def level(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

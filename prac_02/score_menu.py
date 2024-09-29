menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
def main():
    score = 1
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Score: "))
            score = get_valid_score(score)
        elif choice == "P":
            determine_grade(score)
        elif choice == "S":
            print("*"*score)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell!")


def determine_grade(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def get_valid_score(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def valid_score(score):
    if score < 0 and score > 100:
        print("Invalid score!")
    return


main()
import random

def main():
    while True:
        try:
            number_of_picks = int(input("How many quick picks would you like to generate? "))
            if number_of_picks <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print("\nHere are your quick picks:")
    for i in range(number_of_picks):
        print(', '.join(f'{num:2}' for num in random_numbers()))

def random_numbers():
    quick_pick = []
    while len(quick_pick) < 6:
        numbers = random.randint(1, 45)
        if numbers not in quick_pick:
            quick_pick.append(numbers)
    return sorted(quick_pick)



main()

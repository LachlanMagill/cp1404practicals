from guitar import Guitar


def load_guitars(filename):
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, year, cost = line.strip().split(',')
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print("File not found. Starting with an empty list of guitars.")
    return guitars


def save_guitars(filename, guitars):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def display_guitars(guitars):
    if guitars:
        for guitar in guitars:
            print(guitar)
    else:
        print("No guitars to display.")


def add_new_guitar():
    name = input("Enter the guitar's name: ")

    while True:
        try:
            year = int(input("Enter the guitar's year: "))
            break
        except ValueError:
            print("Invalid year. Please enter a valid number.")

    while True:
        try:
            cost = float(input("Enter the guitar's cost: "))
            break
        except ValueError:
            print("Invalid cost. Please enter a valid number.")

    return Guitar(name, year, cost)


def main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    print("Guitars loaded from file:")
    display_guitars(guitars)

    guitars.sort()

    print("\nSorted guitars (oldest to newest):")
    display_guitars(guitars)

    while True:
        add_another = input("\nDo you want to add a new guitar? (y/n): ").lower()

        if add_another == 'y':
            new_guitar = add_new_guitar()
            guitars.append(new_guitar)
        elif add_another == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    save_guitars(filename, guitars)
    print("\nAll guitars saved to file.")


if __name__ == "__main__":
    main()
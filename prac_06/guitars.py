"""estimated time 20 min
started at 6:54 pm
finished at 7:25 pm
total time 31 min"""
from guitar import Guitar


def main():
    guitars = []
    print("Enter your guitars (leave the name blank to finish):")

    name = input("Name: ").title()
    while name != "":
        is_valid_year = False
        while not is_valid_year:
            try:
                year = int(input("Year: "))
                is_valid_year = True
            except ValueError:
                print("Year must be an integer")

        is_valid_cost = False
        while not is_valid_cost:
            try:
                cost = float(input("Cost: ").replace("$", ""))
                is_valid_cost = True
            except ValueError:
                print("Cost must be a float")

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar.name} added.")
        name = input("Name: ").title()

    print("\nThese are my guitars:")
    max_name_length = max(len(guitar.name) for guitar in guitars)
    max_cost_length = max(len(f"${guitar.cost:,.2f}") for guitar in guitars)

    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year:>4}), "
              f"worth ${guitar.cost:>{max_cost_length},.2f}{vintage_string}")


if __name__ == "__main__":
    main()

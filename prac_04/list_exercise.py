def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    input_username = input("What is your username? ")
    if input_username in usernames:
        print("Access granted.")


        numbers = []
        get_number(numbers)


        smallest = min(numbers)
        largest = max(numbers)
        average = sum(numbers) / len(numbers)


        print("The first number is", numbers[0])
        print("The last number is", numbers[-1])
        print("Smallest number is:", smallest)
        print("largest number is:", largest)
        print("Average:", average)
    else:
        print("Access denied.")

def get_number(numbers):
    for i in range(1, 6):
        number = float(input(f"Enter number {i}: "))
        numbers.append(number)


main()

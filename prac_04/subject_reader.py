"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.py"



def main():

    data = load_data()
    print(data)



def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data_list = []
    for line in input_file:
        print(line)  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_list = [parts] + data_list
        print(data_list)

    input_file.close()


main()

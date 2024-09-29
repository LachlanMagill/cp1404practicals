def main():
    password = get_password()
    star_password(password)


def star_password(password):
    print('*' * len(password))


def get_password():
    minimum_length = int(input('Minimum length of the password: '))
    password = input('Password: ')
    while minimum_length > len(password):
        print('Error! Password not long enough!')
        password = input('Password: ')
    return password


main()
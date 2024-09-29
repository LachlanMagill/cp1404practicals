def main():
    minimum_length = int(input('Minimum length of the password: '))
    password = input('Password: ')
    while minimum_length > len(password):
        print('Error! Password not long enough!')
        password = input('Password: ')
    print('*'*len(password))




main()
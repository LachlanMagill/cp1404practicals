

def main():
    users = {}

    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation != '' and confirmation != 'y':
            name = input("Please enter your name: ").strip()

        users[email] = name


    for email, name in users.items():
        print(f"{name} ({email})")

def extract_name(email):
    username = email.split('@')[0]
    name = username.replace('.', ' ').title()
    return name

if __name__ == "__main__":
    main()

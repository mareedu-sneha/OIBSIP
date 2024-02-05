details= {}

def register(usr, paswrd):
    if usr in details:
        print("Username already taken.")
    else:
        details[usr] = paswrd
        print("Registration successful!")

def login(usr, paswrd):
    if usr in details and details[usr] == paswrd:
        print("Login successful!")
        return True
    else:
        print("Login failed,Try again!")
        return False

def secured_page(usr):
    print(f"Welcome to the secured page, {usr}!")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        option= input("Enter your choice: ")

        if option == '1':
            usr = input("Enter a username: ")
            paswrd = input("Enter a password: ")
            register(usr, paswrd)
        elif option == '2':
            usr = input("Enter your username: ")
            paswrd= input("Enter your password: ")
            if login(usr, paswrd):
                secured_page(usr)
        elif option == '3':
            print("Exit")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()

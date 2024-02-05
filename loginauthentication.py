data= {}

def register(username, password):
    if username in data:
        print("Username already taken.")
    else:
        data[username] = password
        print("Registration successful!")

def login(username, password):
    if username in data and data[username] == password:
        print("Login successful!")
        return True
    else:
        print("Login failed,Try again!")
        return False

def secured_page(username):
    print(f"Welcome to the secured page, {username}!")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        option= input("Enter your choice: ")

        if option == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            register(username, password)
        elif option == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if login(username, password):
                secured_page(username)
        elif option == '3':
            print("Exit")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if__name__=="__main__":
    main()

username = ""
email = ""
password = ""

while True:

    print("1. Registration")
    print("2. Login")
    print("3. Stop Programm")

    choice = input("Choose: ")

    if choice == "1":

        username = input("Enter user name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        print("Registration successfully!")

    elif choice == "2":

        login_email = input("Enter email: ")
        login_password = input("Enter password: ")

        if login_email == email and login_password == password:

            print("Login successfully!")
            break

        else:
            print("Incorrect email or password!")

    elif choice == "3":

        print("Program stopped.")
        break

    else:
        print("Invalid choice!")
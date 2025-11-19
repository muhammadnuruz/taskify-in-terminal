from register import register
from login import login, clear_screen


def AuthenticationFunction():
    clear_screen()
    while True:
        print("|-----------|")
        print("|1. Register|")
        print("|2. Login   |")
        print("|3. Exit    |")
        print("|-----------|")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            status, msg = register()
            clear_screen()
            print(msg, "\n")

        elif choice == "2":
            status, msg = login()
            clear_screen()
            print(msg, "\n")
            if status:
                return True

        elif choice == "3":
            clear_screen()
            return False
        else:
            clear_screen()
            print("Invalid choice\n")

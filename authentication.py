from login import login, clear_screen
from register import register


def AuthenticationFunction():
    clear_screen()
    while True:
        print("|-----------|")
        print("|1. Register|")
        print("|2. Login   |")
        print("|3. Exit    |")
        print("|-----------|")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            register_response, msg = register()
            if register_response:
                clear_screen()
                print(msg)
            else:
                clear_screen()
                print(msg, end="\n")
        elif choice == '2':
            login_response, msg = login()
            if login_response:
                clear_screen()
                print(msg, end="\n")
                return True
            else:
                clear_screen()
                print(msg, end="\n")
        elif choice == '3':
            clear_screen()
            return False
        else:
            clear_screen()
            print("""|--------------|
|Invalid choice|
|--------------|\n""")

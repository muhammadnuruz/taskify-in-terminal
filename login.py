import os

USERS = {
    "admin@mail.com": ["Main Admin", "admin"]
}


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def login():
    clear_screen()
    attempts = 0
    while attempts < 3:
        attempts += 1
        print("""|----------------------------------|
|Enter 0 to return to the main menu|
|----------------------------------|\n""")

        gmail = input("Enter your email: ")
        if gmail == "0":
            return False, "Returned to main menu"

        if gmail not in USERS:
            clear_screen()
            print("User not found\n")
            continue

        password = input("Enter your password: ")
        if password == USERS[gmail][1]:
            return True, "User logged in successfully"
        else:
            clear_screen()
            print("Incorrect password\n")

    return False, "Your device has been blocked"

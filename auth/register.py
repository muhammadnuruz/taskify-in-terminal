from auth.login import USERS, clear_screen


def validate_password(password: str) -> bool:
    return len(password) >= 8


def validate_email(email: str) -> bool:
    return len(email) >= 6 and "@" in email


def register():
    attempts = 0
    clear_screen()
    while attempts < 3:
        attempts += 1

        print("""|----------------------------------|
|Enter 0 to return to the main menu|
|----------------------------------|\n""")

        name = input("Enter your name: ")
        if name == "0":
            return False, "Returned to main menu"

        gmail = input("Enter your email: ")
        if gmail == "0":
            return False, "Returned to main menu"

        if not validate_email(gmail):
            clear_screen()
            print("Invalid email address\n")
            continue

        if gmail in USERS:
            clear_screen()
            print("User already exists\n")
            continue

        password = input("Enter your password: ")
        if password == "0":
            return False, "Returned to main menu"

        if not validate_password(password):
            clear_screen()
            print("Password must be at least 8 characters.\n")
            continue

        confirm_password = input("Confirm your password: ")
        if confirm_password == "0":
            return False, "Returned to main menu"

        if password != confirm_password:
            clear_screen()
            print("Passwords do not match\n")
            continue

        USERS[gmail] = [name, password]
        return True, "User registered successfully. Please log in."

    return False, "Your device has been blocked"

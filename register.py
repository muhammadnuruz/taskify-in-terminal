from login import USERS, clear_screen


def register():
    clear_screen()
    name = input("Enter your name: ")
    gmail = input("Enter your email: ")
    if gmail in USERS:
        return False, """|-------------------|
|User already exists|
|-------------------|\n"""
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    if password != confirm_password:
        return False, """|----------------------|
|Passwords do not match|
|----------------------|\n"""
    USERS[gmail] = [name, password]
    return True, """|----------------------------|
|User registered successfully|
|----------------------------|\n"""

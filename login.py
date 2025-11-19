import os

USERS = {"admin@mail.com": ['Main Admin', 'admin']}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def login():
    clear_screen()
    gmail = input("Enter your email: ")
    if gmail in USERS:
        password = input("Enter your password: ")
        if password == USERS[gmail][1]:
            return True, """|------------------------|
|User logged successfully|
|------------------------|\n"""
        else:
            return False, """|---------------------|
|Password is incorrect|
|---------------------|\n"""
    else:
        return False, """|--------------|
|User not found|
|--------------|\n"""

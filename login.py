import os
import uuid

USERS = {"admin@mail.com": ['Main Admin', 'admin']}
LOGIN_USERS = {}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def login():
    clear_screen()
    gmail = input("Enter your email: ")
    if gmail in USERS:
        password = input("Enter your password: ")
        if password == USERS[gmail][1]:
            uid = uuid.uuid4().hex
            user_information = {gmail: uid}
            LOGIN_USERS.update(user_information)
            return True, user_information
        else:
            return False, """|---------------------|
|Password is incorrect|
|---------------------|\n"""
    else:
        return False, """|--------------|
|User not found|
|--------------|\n"""


def check_login(user_information: dict) -> bool:
    if user_information in LOGIN_USERS:
        return True
    else:
        return False

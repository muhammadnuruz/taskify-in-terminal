from auth.login import clear_screen
from tasks.create import createTask
from tasks.view import viewTask


def taskManager(current_user: list, gmail: str):
    clear_screen()
    while True:
        print("Logged in as:", current_user[0], "\n")
        print("""|----------------|
|1. View Tasks   |
|2. Create Task  |
|3. Log Out      |
|----------------|""")

        cmd = input("\nEnter your choice: ")
        if cmd == "1":
            viewTask(gmail)
            clear_screen()
        elif cmd == "2":
            createTask(gmail)
            clear_screen()
        elif cmd == "3":
            return False
        else:
            clear_screen()
            print("\nInvalid command.")

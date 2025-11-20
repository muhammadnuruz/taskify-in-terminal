from auth.login import clear_screen
from tasks.storage import tasks


def createTask(gmail: str):
    clear_screen()
    print("""|----------------------------------|
|Enter 0 to return to the main menu|
|----------------------------------|\n""")
    name = input("Enter task name: ")
    if name == '0':
        clear_screen()
        return False
    description = input("Enter task description: ")
    if description == '0':
        clear_screen()
        return False
    deadline = input("Enter task deadline(DD:MM:YYYY): ")
    if deadline == '0':
        clear_screen()
        return False

    task_id = len(tasks) + 1

    tasks[task_id] = {
        "Name": name,
        "Description": description,
        "Deadline": deadline,
        "Status": "In progress",
        "User": gmail
    }
    clear_screen()
    print(f"Task has been created successfully.\n")
    return True

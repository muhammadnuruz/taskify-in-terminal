from auth.login import clear_screen
from tasks.storage import tasks


def deleteTask(task_id):
    clear_screen()
    task = tasks.pop(task_id)
    print("""|--------------------------|
| Task successfully deleted|
|--------------------------|\n""")
    print(f"Task ID: {task_id}")
    print(f"Name: {task['Name']}")
    print(f"Description: {task['Description']}")
    print(f"Deadline: {task['Deadline']}")
    print(f"Status: Completed\n")
    input("Press Enter to continue...")

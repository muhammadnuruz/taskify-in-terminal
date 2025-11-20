from auth.login import clear_screen
from tasks.delete import deleteTask
from tasks.storage import tasks
from tasks.update import updateTask


def viewTask(gmail: str):
    clear_screen()
    while True:
        print("""|----------------------------------|
| Enter 0 to return to the main menu |
|----------------------------------|\n""")
        user_tasks = {tid: t for tid, t in tasks.items() if t['User'] == gmail}
        if len(user_tasks) == 0:
            clear_screen()
            print("You don't have any tasks.\n")
            return False
        for tid, task in user_tasks.items():
            print(f"{tid}) {task['Name']}")
        task_id = input("\nEnter Task ID: ")
        if task_id == "0":
            return False

        if not task_id.isdigit() or int(task_id) not in user_tasks:
            print("Invalid Task ID.")
            continue
        task_id = int(task_id)
        while True:
            clear_screen()
            task = user_tasks[task_id]
            print(f"""Task ID: {task_id}
Name: {task['Name']}
Description: {task['Description']}
Deadline: {task['Deadline']}
Status: {task['Status']}\n""")
            print("""
|-------------------------|
|1. Complete the task     |
|2. Delete Task           |
|3. Return to Task List   |
|-------------------------|\n""")
            cmd = input("Enter your choice: ")
            if cmd == '1':
                updateTask(task_id)
                break
            elif cmd == '2':
                deleteTask(task_id)
                break
            elif cmd == '3':
                clear_screen()
                break
            else:
                clear_screen()
                print("Invalid choice.")

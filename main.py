from core.tasks import TaskManager
from utils.helpers import print_slow


def main() -> None:
    tasks = TaskManager()
    tasks.load_tasks("tasks.json")  # Load tasks at the start

    while True:
        print(
            """
    ------------------------------
    | 1. Add a task              |
    |----------------------------|
    | 2. View tasks              |
    |----------------------------|
    | 3. Mark task as completed  |
    |----------------------------|
    | 4. Delete task             |
    |----------------------------|
    | 5. Save tasks              |
    |----------------------------|
    | 6. Exit                    |
    ------------------------------   
"""
        )
        print_slow("Enter your choice: ")
        choice = int(input())

        if choice == 6:
            tasks.save_tasks("tasks.json")  # Save tasks on exit
            break
        elif choice == 1:
            task_to_add: str = input("Enter a task to add: ")
            tasks.add_task(task_to_add.strip())
        elif choice == 2:
            tasks.view_task()
        elif choice == 3:
            tasks.view_task()  # Display tasks with IDs
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                tasks.mark_completed(task_id)
            except ValueError:
                print("Invalid task ID, please enter a number.")
        elif choice == 4:
            tasks.view_task()  # Display tasks with IDs
            try:
                task_id = int(input("Enter task ID to remove: "))
                tasks.delet_task(task_id)
            except ValueError:
                print("Invalid task ID, please enter a number.")
        elif choice == 5:
            tasks.save_tasks("tasks.json")


if __name__=="__main__":
    main()
from core.auth import AuthenticationManager
from core.storage import Storage
from core.tasks import TaskManager
from util.helpers import print_slow

# Track user after login
current_user = ""

def handle_task_options(username):
    """Handles task management options after successful login."""
    while True:
        print("What would you like to do?\n")
        print("1. Add Task\n2. View Task\n3. Mark Task as completed\n4. Delete Task\n5. Export tasks\nQ. Exit\n")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter your task: ")
            TaskManager.add_task(username, task)
        elif choice == "2":
            TaskManager.view_tasks(username)
        elif choice == "3":
            task_id = input("Enter task ID: ")
            TaskManager.mark_task_completed(username, task_id)
        elif choice == "4":
            task_id = input("Enter task ID: ")
            TaskManager.delete_task(username, task_id)
        elif choice == "5":
            print("1. JSON or 2. CSV\nQ. Exit\n")
            choice = input("Enter your choice: ")
            if choice == "1":
                Storage.export_data(username, format="json")
            elif choice == "2":
                Storage.export_data(username, format="csv")
            elif choice.lower() == "q":
                print("Goodbye")
                break
            else:
                print("Invalid choice")
        elif choice.lower() == "q":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

def main():
    while True:
        print("Hello, Welcome to Task Manager\n")
        print("----------------------------------------")
        print("1. Login\n2. Register\nQ. Exit\n")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if AuthenticationManager.login_user(username, password):
                global current_user
                current_user = username
                print("Logged in successfully!")
                print(f"\nWelcome {username} ")
                handle_task_options(username)
            else:
                print("Invalid credentials")

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            name = input("Enter your name: ")
            AuthenticationManager.register_user(username, password, name)

        elif choice.lower() == "q":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

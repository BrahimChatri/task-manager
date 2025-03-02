"""This the main part of the task manager (UI part)"""

from core.auth import AuthenticationManager, min_
from core.storage import Storage
from core.tasks import TaskManager
import utils.logger
# Track user after login
current_user = ""


def handle_task_options(username):
    """Handles task management options after successful login."""
    while True:
        print("What would you like to do?\n")
        print(
            "1. Add Task\n2. View Task\n3. Mark Task as completed\n4. Delete Task\n5. Export tasks\nQ. Exit\n"
        )
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                task = input("Enter your task: ")
                TaskManager.add_task(username, task)
            case "2":
                TaskManager.view_tasks(username)
            case "3":
                task_id = input("Enter task ID: ")
                TaskManager.mark_task_completed(username, task_id)
            case "4":
                task_id = input("Enter task ID: ")
                TaskManager.delete_task(username, task_id)
            case "5":
                print("1. JSON or 2. CSV\nQ. Exit\n")
                choice = input("Enter your choice: ")
                if choice == "1":
                    Storage.export_data(username, formate="json")
                elif choice == "2":
                    Storage.export_data(username, formate="csv")
                elif choice.lower() == "q":
                    print("Goodbye")
                    break
                else:
                    print("Invalid choice")
            case choice if choice.lower() == "q":
                utils.logger.Info_logger.info("Goodbye")
                break
            case _:
                utils.logger.Error_logger.error("Invalid choice")

def main():
    """This function handles user input"""
    while True:
        print("Hello, Welcome to Task Manager\n")
        print("----------------------------------------")
        print("1. Login\n2. Register\nQ. Exit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter your username: ")
            if not username:
                utils.logger.Error_logger.error("exiting due to lack of username")
                break
            password = input("Enter your password: ")
            if (not password) or (len(password) < min_):
                utils.logger.Error_logger.error("exiting due to the password being too short")
                break
            if AuthenticationManager.login_user(username, password):
                global current_user
                current_user = username
                utils.logger.Info_logger.info("Logged in successfully!")
                utils.logger.Info_logger.info(f"\nWelcome {username} ")
                handle_task_options(username)
            else:
                utils.logger.Error_logger.error("Invalid credentials")
                break
        elif choice == "2":
            username = input("Enter your username: ")
            if not username:
                utils.logger.Error_logger.error("exiting due to lack of username")
                break
            password = input("Enter your password: ")
            if (not password) or (len(password) < min_):
                utils.logger.Error_logger.error("exiting due to the password being too short")
                break
            name = input("Enter your name: ")
            if not name:
                utils.logger.Error_logger.error("exiting due to lack of name")
                break
            AuthenticationManager.register_user(username, password, name)

        elif choice.lower() == "q":
            utils.logger.Info_logger.info("Goodbye")
            break
        else:
            utils.logger.Error_logger.error("Invalid choice")
            break

if __name__ == "__main__":
    main()

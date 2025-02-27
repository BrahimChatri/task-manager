from core.auth import AuthenticationManager
from core.storage import Storage
from core.tasks import TaskManager
from util.helpers import print_slow

# Track user after login 
current_user = ""

# Main func to handle logic of CLI
def main():
    while True:
        print_slow("Hello Welcome to Task manager \n")
        print("----------------------------------------")
        print_slow("""1. Login \n2. Register\n Q.exit\nEnter ur choice""")
        choice =input(":")
        if choice=="1":
            username =input("Enter ur username: ")
            password =input("Enter ur password: ")
            if AuthenticationManager.login_user(username,password):
                global current_user 
                current_user= username
                print_slow("Logged in successfully !")
                print_slow(f"Welcome {username}")
                print_slow("What would you like to do?\n")
                print_slow("1. Add Task\n2. View Task\n3. Mark Task as completed\n4. Delete Task\n, 5.export tasks\nQ.exit\nEnter ur choice")
                choice = input(":")
                if choice=="1":
                    task = input("Enter ur task: ")
                    TaskManager.add_task(username,task)
                elif choice=="2":
                    TaskManager.view_tasks(username)
                elif choice=="3":
                    task_id = input("Enter task id: ")
                    TaskManager.mark_task_completed(username,task_id)
                elif choice=="4":
                    task_id = input("Enter task id: ")
                    TaskManager.delete_task(username,task_id)
                elif choice=="5":
                    print_slow("1.JSON or 2.CSV \nQ.exit\nEnter ur choice")
                    choice = input(":")
                    if choice=="1":
                        Storage.export_data(username,format="csv")
                    elif choice=="2":
                        Storage.export_data(username,format="json")
                    elif choice=="Q" or choice=="q":
                        print_slow("Goodbye")
                        break
                elif choice=="Q" or choice=="q":
                    print_slow("Goodbye")
                    break
                else:
                    print_slow("Invalid choice")
                
            else:
                print_slow("Invalid credentials")

        elif choice=="2":
            username =input("Enter ur username: ")
            password =input("Enter ur password: ")
            name =input("Enter ur name: ")
            AuthenticationManager.register_user(username,password,name)

if __name__=="__main__" :
    main()

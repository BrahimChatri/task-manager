import json, os
from typing import Any
from utils.helpers import task_count_decorator

# Class to manage the Task manager
class TaskManager:
    def __init__(self,) -> None:
        self.tasks:list[str|Any] = []

    @task_count_decorator
    def add_task(self, task: str) -> None:
        task_dict = {"task": task, "completed": False,"task_id": len(self.tasks)+1}
        self.tasks.append(task_dict)
        print(f"Task added: {task}")
    
    def view_task(self) -> None:
        for task in self.tasks:
            print(f"{task['task_id']}. {task['task']} - {'Completed' if task['completed'] else 'Not completed'}")
        
    def mark_completed(self, task_id: int) -> None:
        for task in self.tasks:
            if task['task_id'] == task_id:
                task['completed'] = True
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task with ID {task_id} not found.")


    def delet_task(self, task_id: int) -> None:
        for task in self.tasks:
            if task["task_id"] == int(task_id):
                self.tasks.remove(task)
                print(f"{task["task"]} has been removed successfully")
                return
        else:
            print("Task not found !")


    def save_tasks(self, filename:str) -> None:
        tasks_json ={"tasks": self.tasks}
        with open(filename,"w")as f:
            json.dump(tasks_json,f , indent=4)
            print(f"tasks saved to {filename} successfully ")

    def load_tasks(self, filename:str) -> None:
        if os.path.exists(filename):
            with open(filename, "r") as f:
                try:
                    loaded_tasks = json.load(f)
                    self.tasks=loaded_tasks["tasks"]
                except json.JSONDecodeError:
                    print("The tasks file is empty or corrupted. Starting with an empty task list.")
                    self.tasks=[]
        else :
            self.tasks=[]
            print("No task file found. Starting with an empty task list.")
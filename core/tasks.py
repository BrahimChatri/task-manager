from core.storage import Storage
import utils.logger as logger

class TaskManager:
    @staticmethod
    def add_task(username: str, task_description: str) -> None:
        data = Storage.load_data()
        if username in data:
            task_id = len(data[username]["tasks"]) + 1
            task = {"task": task_description, "completed": False, "id": task_id}
            data[username]["tasks"].append(task)
            Storage.save_data(data)
            logger.Info_logger.info(f"Task added for {username}.")
        else:
            logger.Error_logger.error(f"User {username} not found.")

    @staticmethod
    def view_tasks(username: str) -> None:
        data = Storage.load_data()
        if username in data:
            tasks = data[username]["tasks"]
            if tasks:
                logger.Info_logger.info(f"Tasks for {username}:")
                for task in tasks:
                    status = "✅ Completed" if task["completed"] else "❌ Not Completed"
                    logger.Info_logger.info(f"{task['id']}: {task['task']} - {status}")
            else:
                logger.Error_logger.error(f"{username} has no tasks.")
        else:
            logger.Error_logger.error(f"User {username} not found.")

    @staticmethod
    def mark_task_completed(username: str, task_id: int) -> None:
        data = Storage.load_data()
        if username in data:
            tasks = data[username]["tasks"]
            for task in tasks:
                if task["id"] == task_id:  # Fixed key name
                    task["completed"] = True
                    Storage.save_data(data)
                    print(f"Task {task_id} for {username} marked as completed.")
                    return
            logger.Error_logger.error(f"Task {task_id} not found for {username}.")
        else:
            logger.Error_logger.error(f"User {username} not found.")

    @staticmethod
    def delete_task(username: str, task_id: int) -> None:
        data = Storage.load_data()
        if username in data:
            tasks = data[username]["tasks"]
            new_tasks = [task for task in tasks if task["id"] != task_id]  # Remove task
            if len(new_tasks) == len(tasks):
                print(f"Task {task_id} not found for {username}.")
                return
            data[username]["tasks"] = new_tasks
            Storage.save_data(data)
            logger.Info_logger.info(f"Task {task_id} deleted successfully for {username}.")
        else:
            logger.Error_logger.error(f"User {username} not found.")

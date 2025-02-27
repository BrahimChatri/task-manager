import json
import os
import csv
from typing import Any

class Storage:
    @staticmethod
    def load_data() -> dict[str, Any]:
        """Load data from JSON file and return it as a dictionary."""
        file_path = os.path.join(os.path.dirname(__file__), "../data/data.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    print("The users file is empty or corrupted. Starting with an empty user list.")
                    return {}
        print("No user file found. Starting with an empty user list.")
        return {}

    @staticmethod
    def save_data(user_data: dict) -> None:
        """Save the user data to the JSON file."""
        file_path = os.path.join(os.path.dirname(__file__), "../data/data.json")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            json.dump(user_data, f, indent=4)
        print("Data saved successfully.")

    @staticmethod
    def export_data(username: str, formate: str):
        """Export user tasks to CSV or JSON format."""
        data = Storage.load_data()
        if username not in data:
            print(f"User '{username}' not found!")
            return
        tasks = data[username]["tasks"]
        file_path = f"{username}.{formate.lower()}"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if formate.upper() == "CSV":
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["task", "completed", "task_id"])
                for task in tasks:
                    writer.writerow([task["task"], task["completed"], task["task_id"]])
            print(f"Tasks exported successfully to {file_path}")

        elif formate.upper() == "JSON":
            with open(file_path, "w") as file:
                json.dump(tasks, file, indent=4)
            print(f"Tasks exported successfully to {file_path}")

        else:
            print("Invalid file type! Use 'CSV' or 'JSON'.")

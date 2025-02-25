# Task Manager - Python Learning Project

## 🚀 About the Project
This is a **Task Manager** project built as part of my learning journey in Python. The goal is to enhance my skills in **OOP, decorators, file handling, authentication**, and other advanced Python concepts.

The project will be developed in **two versions**:
1. **CLI Version** (First Phase) - A command-line interface for managing tasks.
2. **GUI Version** (Second Phase) - A graphical user interface for better user experience.

## 🎯 Learning Goals
This project is designed to strengthen my understanding of:
- Object-Oriented Programming (OOP)
- Python Decorators
- File Handling (JSON Storage CSV Export)
- User Authentication & Data Persistence
- Password hashing 
- Modular Code Structure
- Best Practices in Python

## 📂 Folder Structure
```
📂 task_manager/
│-- 📂 utils/          # Utility functions (printing, logging, validation)
│   │-- __init__.py    
│   │-- helpers.py     # General utility functions (print_slow, etc.)
│   │-- logger.py      # Handles logging (errors, activity)
│
│-- 📂 core/           # Core functionality of the task manager
│   │-- __init__.py
│   │-- tasks.py       # Task management (add, delete, update, etc.)
│   │-- storage.py     # File handling (JSON, CSV, or DB storage)
│   │-- auth.py        # User authentication (login, signup)
│
│-- 📂 data/           # Stores user-related files (JSON, DB, etc.)
│   │-- users.json     # Stores all users data (tasks passwords ...)
│
│-- .gitignore
│-- README.md
│-- main.py           # Entry point for the app
│-- requirements.txt   
```


## 🛠️ Features (Planned)
### ✅ CLI Version (First Phase)
- User Authentication (Register/Login)
- Add, View, Mark, and Delete Tasks
- Task Management per User
- Save & Load Tasks (JSON-Based)
- Error Handling & Input Validation

### 🎨 GUI Version (Second Phase)
- Interactive UI for Task Management
- Advanced User Authentication
- Data Visualization (Task Progress, Deadlines)
- Database Integration (Optional)

## 👨‍💻 How to Run
1. Clone this repository:
   ```sh
   git clone https://github.com/BrahimChatri/task-manager.git
   ```
2. Navigate to the project directory:
   ```sh
   cd task-manager
   ```
3. Install all Dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the CLI version:
   ```sh
   python main.py
   ```

## 📜 License
This project is for **educational purposes** and is open for contributions and feedback!

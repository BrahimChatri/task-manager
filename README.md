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
## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/BrahimChatri/task-manager.git
   ```
2. Navigate to the project directory:
   ```sh
   cd task-manager
   ```
3. (Optional) Create a virtual environment:
   ```sh
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
4. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the main script:
```sh
python main.py
```
Follow the on-screen instructions to login or register and manage tasks.

## Future Enhancements
- Adding a GUI using Tkinter
- Task due dates and notifications
- Enhanced data visualization

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
│   │-- data.json     # Stores all users data (tasks passwords ...)
│
│-- .gitignore
│-- README.md
│-- main.py           # Entry point for the app
│-- requirements.txt   
```
## 📜 License
This project is licensed under the MIT License.


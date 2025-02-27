from core.storage import Storage
import bcrypt

class AuthenticationManager:
    def __init__(self):
        pass

    @staticmethod
    def hash_pass(password: str):
        try:
            if not password or len(password) < 6:  # You can set a minimum password length
                raise ValueError("Password must be at least 6 characters long")
            hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            return hashed.decode("utf-8")
        except Exception as e:
            print(f"Error hashing password: {e}")
            return None

    @staticmethod
    def compare_pass(password: str, hashed_password: str):
        try:
            if not hashed_password:
                raise ValueError("Invalid hash provided for comparison")

            return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

        except Exception as e:
            print(f"Error comparing passwords: {e}")
            return False
        
    @staticmethod
    def register_user(username: str, password: str, name: str,) -> None:
        data = Storage.load_data()
        if username in data:
            print("Username already exists.")
        else :
            password_hash=AuthenticationManager.hash_pass(password=password)
            data[username] = {"user_info":{"name":name,"password": password_hash},"tasks":[]}
            Storage.save_data(data)
            
    @staticmethod
    def login_user(username: str, password: str) -> bool:
        data = Storage.load_data()
        
        if username not in data:
            print("Account not found Please register first!")
            return False
        
        password_hash = data[username]["user_info"]["password"]
        if AuthenticationManager.compare_pass(password, password_hash):
            print("Logged in successfully!")
            return True
        else:
            print("Invalid password!")
            return False

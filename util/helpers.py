import time

# decorator to count the tasks after adding
def task_count_decorator(func):
    def wrapper(self, task):# -> Any:
        # Call the original function (add_task)
        result = func(self, task)
        # Count the tasks after adding
        print(f"You now have {len(self.tasks)} tasks.")
        return result
    return wrapper

# Function to print text slowly
def print_slow(text:str, delay=0.06):
    for char in text:
        print(char, sep="",end="")
        time.sleep(delay)
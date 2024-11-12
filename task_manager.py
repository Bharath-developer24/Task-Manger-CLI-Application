import json
import os

# Dummy credentials:
EMAIL_ID = "bharath@gmail.com"
PASSWORD = "bharath@123"


# Define Task Class:
# The Task class defines a structure for individual tasks With properties for an ID, title, completion status.

class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

    @staticmethod
    def from_dict(task_dict):
        return Task(task_dict["id"], task_dict["title"], task_dict["completed"])




# Task Manager Functions:
# The TaskManager class manages a list of tasks.
# By loading them from a file (tasks.json).
# Includes methods to add, view, delete and mark tasks as complete.

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, title):
        new_id = max([task.id for task in self.tasks], default=0) + 1
        new_task = Task(new_id, title)
        self.tasks.append(new_task)
        print(f"Task '{title}' added with ID {new_id}.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"ID: {task.id}, Title: {task.title}, Status: {status}")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        print(f"Task with ID {task_id} deleted.")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                print(f"Task with ID {task_id} marked as completed.")
                return
        print(f"Task with ID {task_id} not found.")

   
   
   
   
    # File handling functions:
    # The save_tasks function writes the current list of tasks to a JSON file
    # For persistent storage. The load_tasks function loads tasks from the JSON file
    # if it exists, handling potential errors gracefully by returning an empty list if the file is empty or corrupted.

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)
        print("Tasks saved successfully.")

    def load_tasks(self):
        """Load tasks from the JSON file."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r") as f:
                tasks_data = json.load(f)
                return [Task.from_dict(task) for task in tasks_data]
        except json.JSONDecodeError:
            print(f"Error reading {self.filename}. It may be empty or corrupted. Returning empty task list.")
            return []





# Login Function:
# The login function prompts the user to enter their email and password
# Then checks if they match predefined credentials (EMAIL_ID and PASSWORD).
# Otherwise it notifies the user of invalid credentials.

def login():
    print("Welcome to the Task Manager CLI Application.")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email == EMAIL_ID and password == PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False




# Main execution starts here:

if login():
    manager = TaskManager()
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as complete: "))
            manager.complete_task(task_id)
        elif choice == "5":
            manager.save_tasks()
        elif choice == "6":
            manager.save_tasks()
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")













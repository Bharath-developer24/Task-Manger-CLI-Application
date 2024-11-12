


#>>>>>>>>>>>>>>>>>    TITLE OF THE PROJECT : TASK MANAGER CLI APPLICATION 


#>>> DESCRIPTION : A simple command-line application for managing tasks. This application allows users to add, view, mark as complete and delete tasks and it saves the tasks to a JSON file for persistence.The application uses a simple Task class to represent each task and provides easy-to-use methods for managing tasks.

#>>>>>>> Features:
#Add Task: Create a new task with a title.
View Tasks: Display all tasks with their status (completed or not).
Delete Task: Remove a task by ID.
Mark Task as Complete: Update the task status to completed.
Save & Load: Automatically saves tasks to tasks.json and loads them on startup.



#>>>>>> Project Structure and overview:
task_manager.py: Main script containing the application logic.
tasks.json: JSON file for storing asks data.
README.md: Documentation file.
Getting Started Clone the repository.


#>>>>>>> Instructions and how to Run the application with:
bash Copy code python task_manager.py
Follow the on-screen menu to manage tasks.


#>>>>>> Usage Example:
Add a Task: Enter the title when prompted.
View Tasks: Lists all tasks with their IDs and completion status.
Delete a Task: Input the task ID to remove it.
Mark as Complete: Input the task ID to mark it as complete.



#>>>>>>> Requirements >>> Python 3.x






#IF WE WANT TO ADD ANOTHER TASK TO CHANGE THE LOGIN CREDENTIALS THEN WE DEFINE ANOTHER METHOD LIKE THE FOLLOWING CODE IN THE MAIN CODE(task_manager.py File) 



def change_credentials():
    #hear we declare globle variables then it will be we can access enataire code 
    global EMAIL_ID, PASSWORD  
    new_email = input("Enter new email: ")
    new_password = input("Enter new password: ")
    EMAIL_ID = new_email
    PASSWORD = new_password
    print("Credentials updated successfully.")

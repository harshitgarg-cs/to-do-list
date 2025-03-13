class toDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, priority="None", status="Not Started"):

    def view_tasks(self):

    def remove_task(self, task_id):

    def delete_task(self, task_id):   

while True:
    print("Welcome to the To-Do List App!")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Update a task")
    print("6. Exit")

    menu_choice = input("Please choose an option (1-6): ")
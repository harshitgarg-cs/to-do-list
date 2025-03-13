class toDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, priority="None", status="Not Started"):
        task_id = len(self.tasks) + 1 #Assigning a unique ID to each task
        self.tasks[task_id] = {"task": task, "priority": priority, "status": status}
        print(f"Task {task} added successfully with ID {task_id}.")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Current Tasks")
            for task_id, task_info in self.tasks.items():
                print(f"ID: {task_id}, Task: {task_info['task']}, Priority: {task_info['priority']}, Status: {task_info['status']}")
'''
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
'''
todo = toDoList()
todo.view_tasks()
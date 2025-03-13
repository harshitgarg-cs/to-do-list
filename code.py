class toDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, priority="None", status="Not Started"):
        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority. Please enter High, Medium, or Low.")
            return
        
        if status not in ["Not Started", "In Progress", "Completed"]:
            print("Invalid status. Please enter Not Started, In Progress, or Completed.")
            return
        
        task_id = len(self.tasks) + 1 #Assigning a unique ID to each task
        self.tasks[task_id] = {"task": task, "priority": priority, "status": status}
        print(f"Task {'task'} added successfully with ID {task_id}.")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        else:
            print("Current Tasks")
            for task_id, task_info in self.tasks.items():
                print(f"ID: {task_id}, Task: {task_info['task']}, Priority: {task_info['priority']}, Status: {task_info['status']}")

    def completed_tasks(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['status'] = 'Completed'
            print(f"Task {'task_id'} marked as completed.")

    def remove_task(self, task_id):
        if task_id in self.tasks:
                deleted_task = self.tasks.pop(task_id)
                print(f"Task {deleted_task['task']} deleted successfully!")
        else:
            print("Task ID not found")

    def update(self, task_id):   
        if task_id in self.tasks:
            print(f"Updating task {task_id} - {self.tasks[task_id]['task']}")
            new_description = input("Update description: ")
            new_priority = input("Update priority (High, Medium, Low): ")
            new_status = input("Update status (Not Started, In Progress, Completed): ")
            self.tasks[task_id] = {"task": new_description, "priority": new_priority, "status": new_status}
            print(f"Task {task_id} updated successfully.")

        else:
            print("Task ID not found.")

todo = toDoList()

while True:
    
    print("\n==============================")
    print("Welcome to the To-Do List App!")
    print("==============================")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Update a task")
    print("6. Exit")
    
    menu_choice = input("Please choose an option (1-6): ")

    if menu_choice == "1":
        task = input("Enter the task description: ")
        priority = input("Enter the priority (High, Medium, Low): ")
        todo.add_task(task, priority)

    elif menu_choice == "2":
        todo.view_tasks()

    elif menu_choice == "3":
        task_id = int(input("Enter the task ID: "))
        todo.completed_tasks(task_id)

    elif menu_choice == "4":
        task_id = int(input("Enter the task ID: "))
        todo.remove_task(task_id)

    elif menu_choice == "5":
        task_id = int(input("Enter the task ID: "))
        todo.update(task_id)

    elif menu_choice == "6":
        print("Exiting the To-Do List App. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")
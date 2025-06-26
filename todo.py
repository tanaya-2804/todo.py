import os

TODO_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file"""
    if not os.path.exists(TODO_FILE):
        return []
    
    with open(TODO_FILE, 'r') as file:
        tasks = [line.strip() for line in file.readlines() if line.strip()]
    return tasks

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(tasks):
    """Add a new task"""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")

def remove_task(tasks):
    """Remove a task by index"""
    if not tasks:
        print("No tasks to remove!")
        return
    
    print("\nCurrent Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    
    try:
        task_num = int(input("\nEnter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("No tasks in the list!")
        return
    
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def main():
    """Main program loop"""
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

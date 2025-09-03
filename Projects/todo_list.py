# todo_list.py
# Simple To-Do List Program

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "4":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice, try again.")

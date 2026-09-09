# Simple To-Do List App
# Created by Preethi Gopula

tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter your new task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == '2':
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '3':
        if not tasks:
            print("No tasks to delete!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Task '{removed}' deleted!")
            else:
                print("Invalid number!")

    elif choice == '4':
        if not tasks:
            print("No tasks to mark!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(tasks):
                print(f"Task '{tasks[num-1]}' marked as Done! ✅")
            else:
                print("Invalid number!")

    elif choice == '5':
        print("Goodbye! Thanks for using To-Do List App!")
        break

    else:
        print("Invalid choice! Try again.")

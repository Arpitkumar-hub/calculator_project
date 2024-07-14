# import os

# def load_tasks():
#     if os.path.exists("tasks.txt"):
#         with open("tasks.txt", "r") as file:
#             return [line.strip() for line in file.readlines()]
#     return []

# def save_tasks(tasks):
#     with open("tasks.txt", "w") as file:
#         for task in tasks:
#             file.write(task + "\n")

# def display_tasks(tasks):
#     if not tasks:
#         print("No tasks in the list.")
#     else:
#         for i, task in enumerate(tasks, 1):
#             print(f"{i}. {task}")

# def add_task(tasks):
#     task = input("Enter a new task: ")
#     tasks.append(task)
#     print("Task added successfully.")

# def remove_task(tasks):
#     display_tasks(tasks)
#     if tasks:
#         try:
#             index = int(input("Enter the number of the task to remove: ")) - 1
#             if 0 <= index < len(tasks):
#                 removed_task = tasks.pop(index)
#                 print(f"Removed task: {removed_task}")
#             else:
#                 print("Invalid task number.")
#         except ValueError:
#             print("Please enter a valid number.")

# def main():
#     tasks = load_tasks()
    
#     while True:
#         print("\n--- To-Do List Application ---")
#         print("1. Display tasks")
#         print("2. Add a task")
#         print("3. Remove a task")
#         print("4. Save and quit")
        
#         choice = input("Enter your choice (1-4): ")
        
#         if choice == "1":
#             display_tasks(tasks)
#         elif choice == "2":
#             add_task(tasks)
#         elif choice == "3":
#             remove_task(tasks)
#         elif choice == "4":
#             save_tasks(tasks)
#             print("Tasks saved. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How may task you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
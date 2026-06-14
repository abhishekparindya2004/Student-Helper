from storage import load_data, save_data

TASK_FILE = "tasks.json"

def add_task():
    tasks = load_data(TASK_FILE, [])
    title = input("Task title: ").strip()
    subject = input("Subject: ").strip()
    due_date = input("Due date (YYYY-MM-DD): ").strip()
    priority = input("Priority (High/Medium/Low): ").strip().title()

    if not title:
        print("Task title cannot be empty.")
        return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "subject": subject,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    save_data(TASK_FILE, tasks)
    print("Task added successfully.")

def view_tasks():
    tasks = load_data(TASK_FILE, [])
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} | {task["subject"]} | Due: {task["due_date"]} | {task["priority"]} | {status}')

def complete_task():
    tasks = load_data(TASK_FILE, [])
    view_tasks()
    try:
        task_id = int(input("Enter task ID to mark complete: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_data(TASK_FILE, tasks)
                print("Task marked as completed.")
                return
        print("Task not found.")
    except ValueError:
        print("Invalid task ID.")

def delete_task():
    tasks = load_data(TASK_FILE, [])
    view_tasks()
    try:
        task_id = int(input("Enter task ID to delete: "))
        tasks = [task for task in tasks if task["id"] != task_id]
        for index, task in enumerate(tasks, start=1):
            task["id"] = index
        save_data(TASK_FILE, tasks)
        print("Task deleted successfully.")
    except ValueError:
        print("Invalid task ID.")

def task_menu():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Back")
        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

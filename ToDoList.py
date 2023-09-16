import json

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    tasks.append({'task': task, 'completed': False})

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{i}. {task['task']} ({status})")

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
    else:
        print("Invalid task index.")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]
    else:
        print("Invalid task index.")

def main():
    filename = 'tasks.json'
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
            print("Task added successfully.")
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            index = int(input("Enter the task index to mark as completed: ")) - 1
            complete_task(tasks, index)
        elif choice == '4':
            view_tasks(tasks)
            index = int(input("Enter the task index to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '5':
            save_tasks(filename, tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

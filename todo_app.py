tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})
    save_tasks()

def view_tasks():
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else " "
        print(f"{i+1}. [{status}] {task['task']}")

def delete_task(index):
    tasks.pop(index-1)
    save_tasks()

def mark_done(index):
    tasks[index-1]["done"] = True
    save_tasks()

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task['task']},{task['done']}\n")

# Load tasks on startup
try:
    with open("tasks.txt", "r") as f:
        for line in f:
            task, done = line.strip().split(",")
            tasks.append({"task": task, "done": done == "True"})
except FileNotFoundError:
    pass

# CLI Loop
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Mark Done\n5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    # Add more handlers...
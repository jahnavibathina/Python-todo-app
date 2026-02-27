"""
Simple Todo App - A CLI-based task management application
"""

tasks = []

def add_task(task):
    """Add a new task to the list"""
    if not task.strip():
        print("❌ Task cannot be empty!")
        return
    tasks.append({"task": task, "done": False})
    save_tasks()
    print(f"✅ Task '{task}' added successfully!")

def view_tasks():
    """Display all tasks with their status"""
    if not tasks:
        print("📋 No tasks yet! Add one to get started.")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else " "
        print(f"{i+1}. [{status}] {task['task']}")
    print()

def delete_task(index):
    """Delete a task by index"""
    try:
        if index < 1 or index > len(tasks):
            print(f"❌ Invalid task number! Please enter a number between 1 and {len(tasks)}")
            return
        task_name = tasks[index-1]["task"]
        tasks.pop(index-1)
        save_tasks()
        print(f"✅ Task '{task_name}' deleted successfully!")
    except (ValueError, IndexError):
        print("❌ Error deleting task. Please try again.")

def mark_done(index):
    """Mark a task as complete"""
    try:
        if index < 1 or index > len(tasks):
            print(f"❌ Invalid task number! Please enter a number between 1 and {len(tasks)}")
            return
        tasks[index-1]["done"] = True
        save_tasks()
        print(f"✅ Task '{tasks[index-1]['task']}' marked as done!")
    except (ValueError, IndexError):
        print("❌ Error marking task. Please try again.")

def save_tasks():
    """Save all tasks to tasks.txt file"""
    try:
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(f"{task['task']},{task['done']}\n")
    except IOError as e:
        print(f"❌ Error saving tasks: {e}")

def load_tasks():
    """Load tasks from tasks.txt file on startup"""
    global tasks
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split(",", 1)
                    if len(parts) == 2:
                        task, done = parts
                        tasks.append({"task": task, "done": done == "True"})
    except FileNotFoundError:
        print("📝 No existing tasks found. Starting fresh!")
    except IOError as e:
        print(f"⚠️  Error loading tasks: {e}")

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("      📝 TODO APP MENU")
    print("="*40)
    print("1. ➕ Add Task")
    print("2. 📋 View Tasks")
    print("3. ❌ Delete Task")
    print("4. ✅ Mark Task as Done")
    print("5. 🚪 Exit")
    print("="*40)

# Load tasks on startup
load_tasks()

# CLI Loop
if __name__ == "__main__":
    print("\n🎉 Welcome to Todo App!")
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            task = input("Enter task description: ").strip()
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to delete: ").strip())
                delete_task(index)
            except ValueError:
                print("❌ Please enter a valid number!")
        elif choice == "4":
            view_tasks()
            try:
                index = int(input("Enter task number to mark as done: ").strip())
                mark_done(index)
            except ValueError:
                print("❌ Please enter a valid number!")
        elif choice == "5":
            print("\n👋 Thank you for using Todo App! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")
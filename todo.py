tasks = []
filename = "task.txt"


def load_tasks():
    """Load tasks from file"""
    try:
        with open(filename, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        open(filename, "w").close()


def add_task(task):
    """Add task to the file and saves it"""
    tasks.append(task)
    with open(filename, "a") as file:
        file.write(task + "\n")


def view_tasks():
    """Displays all the tasks"""
    if not tasks:
        print("No tasks")
    else:
        print("\nYour to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


# Load existing tasks from file
load_tasks()

# Prompt user to enter a task
task_input = input("Enter a task to add: ")
add_task(task_input)

# Display updated task list
view_tasks()

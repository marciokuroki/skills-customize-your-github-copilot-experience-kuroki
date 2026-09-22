"""Starter code for the Task Manager with JSON assignment."""

import json

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from TASKS_FILE, or return an empty list if it does not exist."""
    # Open TASKS_FILE and return the decoded JSON list.
    pass


def save_tasks(tasks):
    """Save tasks to TASKS_FILE as readable JSON."""
    # Write tasks to TASKS_FILE using json.dump(..., indent=2).
    pass


def next_task_id(tasks):
    """Return an unused integer ID for a new task."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def list_tasks(tasks):
    """Print all tasks in a readable format."""
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "done" if task["completed"] else "pending"
        print(f'{task["id"]}. [{status}] {task["title"]}')


def add_task(tasks):
    """Prompt for a title and append a new task."""
    # Reject blank titles, create a task, and save the list.
    pass


def complete_task(tasks):
    """Mark a task as completed by its ID."""
    # Read an ID, find the matching task, update it, and save the list.
    pass


def remove_task(tasks):
    """Remove a task by its ID."""
    # Read an ID, remove the matching task, and save the list.
    pass


def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

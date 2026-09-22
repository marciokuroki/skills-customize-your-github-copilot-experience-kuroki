# 📘 Assignment: Task Manager with JSON

## 🎯 Objective

Build a command-line task manager that stores tasks in a JSON file. Practice dictionaries, lists, functions, file I/O, JSON serialization, and basic error handling in Python.

## 📝 Tasks

### 🛠️ Load and Save Tasks

#### Description
Implement the functions that load existing tasks from `tasks.json` and save updated tasks back to the file. The program should also work when the file does not exist yet.

#### Requirements
The completed program must:

- use the standard-library `json` module to read and write data
- return an empty list when `tasks.json` does not exist
- save tasks as readable JSON using indentation
- preserve task data between separate program runs

### 🛠️ Create and List Tasks

#### Description
Add the ability to create new tasks and display all saved tasks. Each task must have a unique integer ID, a title, and a completion status.

#### Requirements
The completed program must:

- create a task with a unique ID, a non-empty title, and `completed` set to `False`
- list every saved task with its ID, completion status, and title
- reject blank task titles with a clear message
- save new tasks to `tasks.json`

### 🛠️ Update and Remove Tasks

#### Description
Complete the remaining task-management operations so users can mark tasks as complete and remove tasks by ID.

#### Requirements
The completed program must:

- mark an existing task as completed
- delete an existing task by its ID
- display a clear message when a requested ID does not exist
- keep the menu running until the user chooses to exit
- save every change to `tasks.json`

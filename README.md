# Task Tracker CLI

A production-ready, zero-dependency Command Line Interface (CLI) designed to track your tasks and manage your todo list from the terminal. 

Built strictly using Python's native standard libraries as per the [roadmap.sh Task Tracker](https://roadmap.sh/projects/task-tracker) specifications.

## Features
* **Zero Dependencies:** No external packages required. Runs anywhere Python 3 is installed.
* **JSON File Storage:** Tasks are automatically saved, read, and updated in a structured JSON file locally.
* **Auto-Incrementing IDs:** Every task is assigned a unique tracking ID automatically.
* **Status Filtering:** View all tasks, or filter dynamically by `done`, `todo`, or `in-progress`.

--- 

## Installation

### For Developers / Local Users

1. Clone this repository and navigate into the root directory:
   ```bash
   git clone (https://github.com/jessielynpuli/task-tracker.git)
   cd task-tracker


#USAGE GUIDE

Once installed, use the global command executable `tasktrack` followed by your actions.

##1. Adding Tasks
Create a new task. The status defaults to todo.

Bash
tasktrack add "Buy groceries"
Output: Task added successfully (ID: 1)

##2. Updating and Deleting Tasks
Modify or remove an existing task by targeting its unique ID:

Bash
### Update description
tasktrack update 1 "Buy groceries and cook dinner"

### Delete a task
tasktrack delete 1

##3. Changing Task Status
Quickly toggle the progress state of your tasks using their IDs:

Bash
### Mark as in progress
tasktrack mark-in-progress 1

### Mark as done
tasktrack mark-done 1


##4. Listing Tasks
List everything in your tracker, or isolate tasks dynamically by their current execution status:

Bash
### List all tasks
tasktrack list

### List tasks that are done
tasktrack list done

### List tasks that are still to be done
tasktrack list todo

### List tasks currently in progress
tasktrack list in-progress

Data Structure
Your data is stored safely in your project directory in a structured tasks.json file following this schema:

JSON
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-06-26T18:11:38",
    "updatedAt": "2026-06-26T18:11:38"
  }
]

#Task tracker CLI project

#imports
import os
import sys
import json
import time

#initializng file
JSON_FILE = "tasks.json"

def load_tasks():
    #Load all task function
    if not os.path.exists(JSON_FILE):
        return[]
    #always with open, (DECLARED_NAME, "r" for read)
    with open(JSON_FILE, "r") as file:
        try: #load the file
            #print("reading the file...")
            return json.load(file)
        except json.JSONDecodeError:
            return[]
        
def save_tasks(tasks):
    #Save task reusable function
    # "w" for write
    with open(JSON_FILE, "w") as file:
        #it will write the tasks, in the file (JSON_FILE), and will have to indent to 4
        json.dump(tasks, file, indent=4)

def add_task(description):
    #calls load_tasks() function
    tasks = load_tasks()

    #check if there are no tasks, the new id will set to 1
    if len(tasks) == 0:
        new_id = 1
    else:
        #if there's a task, append 1 to id
        new_id = tasks[-1]["id"] + 1

    #passing a dictionary
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": time.strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    #append the task in the file
    tasks.append(new_task)
    #save the file
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def update_task(target_id, new_description):
    #load task function
    tasks = load_tasks()

    found = False

    #loop to find the target id
    for task in tasks:
        if task['id'] == int(target_id):        
            task['description'] = new_description
            task['updatedAt'] = time.strftime("%Y-%m-%d %H:%M:%S")
            
            found = True
            print(f"Task {target_id} updated.")
            break   
    
    if not found:
       print("Task id does not exist.")
    
    save_tasks(tasks)

def mark_progress(target_id):
    #update in-progress function

    tasks = load_tasks()
    
    found = False

    #loop to find the target id
    for task in tasks:
        if task['id'] == int(target_id):
            task['status'] = "in-progress" 
            task['updatedAt'] = time.strftime("%Y-%m-%d %H:%M:%S")

            print(f"Task {target_id} updated as in-progress.")

            found = True
            break
    
    if not found:
        print("Task id does not exist.")

    save_tasks(tasks)

def mark_done(target_id):
    #update function status as done

    tasks = load_tasks()
    
    found = False

    #loop to find the target id
    for task in tasks:
        if task['id'] == int(target_id):
            task['status'] = "done" 
            task['updatedAt'] = time.strftime("%Y-%m-%d %H:%M:%S")

            print(f"Task {id} updated as done.")

            found = True
            break
    
    if not found:
        print("Task id does not exist.")

    save_tasks(tasks)

def delete_task(target_id):
    #delete function

    tasks = load_tasks()

    found = False

    for task in tasks:
        if task['id'] == int(target_id):
            tasks.remove(task)
            found = True
            print(f"Task {target_id} deleted.")
            break   

    if not found:
       print("Task id does not exist.")
    
    save_tasks(tasks)

def list_task():
    #list all task in the file

    tasks = load_tasks()

    for task in tasks:
        print(str(task['id']) + " " + task['description'] + " " + task['status'])
    
def list_status(status):
    #list all task filtered by status (done, in-progress, todo)

    tasks = load_tasks()
    
    for task in tasks:
        if task['status'] == status:
            print(str(task['id']) + " " + task['description'] + " " + task['status'])


def main():
    
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py [action]")
        return
    
    #initialize the action
    action = sys.argv[1]

    if action == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a task description.")
            return
        
        description = sys.argv[2]
        print(f"Adding task: {description}...")
        add_task(description)
    
    elif action == "update":
        if len(sys.argv) < 4:
            print("Error: Please provide new task description.")
            return
        
        new_description = sys.argv[3]
        target_id = sys.argv[2]
        print(f"Updating {target_id}...")
        update_task(target_id, new_description)
    
    elif action == "delete":
        if len(sys.argv) < 3:
            print("Error: Please specify task id.")
            return
        
        target_id = sys.argv[2]
        print(f"Deleting {target_id}...")
        delete_task(target_id)

    elif action == "list":
        if len(sys.argv) == 2:
            print("Listing...")
            list_task()

        if len(sys.argv) == 3:
            status = sys.argv[2]
            print(f"Listing {status}...")
            list_status(status)

    elif action == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Please specify task id.")

        target_id = sys.argv[2]
        mark_progress(target_id)

    elif action == "mark-done":
        if len(sys.argv) < 3:
            print("Error: Please specify task id.")

        target_id = sys.argv[2]
        mark_done(target_id)

    else:
        print(f"Unkown command: {action}\n\n"
        "Specify action:\n"
        "add       to add a task\n"
        "update    to update a task description\n"
        "delete    to delete a task\n"
        "list      to list all saved tasks\n"
        "mark-in-progress    to update task as in-progress\n"
        "mark-done           to update task as done\n\n"
        "tasktrack [action]")
        sys.exit(1)

if __name__ == "__main__":
    main()
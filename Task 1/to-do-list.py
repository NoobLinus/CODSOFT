#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Storing to-do list data in list
tasks = []

def add_task():
    # Function to add new tasks to to-do list 
    while True:
        task = input("Enter the task: ")
        tasks.append(task)
        more_tasks = input("Do you want to add more tasks? (yes/no): ")
        if more_tasks.lower() != 'yes':
            break

def view_tasks():
    # Function to display all the tasks that user has entered 
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def update_task():
    # Function to display one specific task from the list 
    view_tasks()
    task_number = int(input("Enter the task number to update: "))
    new_task = input("Enter the new task: ")
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] = new_task
    else:
        print("Invalid task number")

def delete_task():
    # Function to delete a task from the list 
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if 0 < task_number <= len(tasks):
        del tasks[task_number - 1]
    else:
        print("Invalid task number")

def todo():
    # Function that will run our program
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Quit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                add_task()
            case 2:
                view_tasks()
            case 3:
                update_task()
            case 4:
                delete_task()
            case 5:
                break
 
# Call the todo function to run the program 
if __name__ == "__main__":
    todo()


# In[ ]:





# In[ ]:





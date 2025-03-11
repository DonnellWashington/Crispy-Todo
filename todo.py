import json
import os

TASK_FILE = "tasks.json"


# A function to load the tasks into the json file
# File is opened in read mode
# Added error checking for if and or when the file doesnt exist
def load_task():

    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Saving tasks that the user wanted to the json file
# Done this by setting write permission in the file and adding the task
# If the file doesnt exist it is created and if it already exists it is over written
# After writing the file is automatically closed
def save_tasks():

    with open(TASK_FILE) as file:
        json.dump(tasks, file, indent=4)

def print_tasks():

    if not tasks: print("You currently have no tasks")

    else:
        print("\nHere are your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")



def remove_task():

    print_tasks()

    task = input("Which task would you like to remove?: ")

    if task in tasks:
        tasks.remove(task)
        print(f"Removed task: {task}")

    else: print("Task not found...")



def add_task():

    if len(tasks) >= 10 : 
        print("You have to many task! Stop being a lazy bum and get shit done first...")
        return

    add = input("What task would you like to add?: ")
    tasks.append(add)
    print(f"Added tasks: {add}")
    

def print_menu():

    print("====Welcome to the Crispy Todo List====")

    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display tasks")
    print("4. Quit")



if __name__ == "__main__":

    while True:

        tasks = []

        print_menu()
        try:
            choice = int(input("What would you like to do?: "))

        except ValueError:
            print("Invalid choice please select a number between 1-4")
            continue

        if choice == 1: add_task()
        
        elif choice == 2 : remove_task()

        elif choice == 3 : print_tasks()

        elif choice == 4 :
            print("See you later!")
            break

        else : print("Invalid choice please select a number between 1-4")


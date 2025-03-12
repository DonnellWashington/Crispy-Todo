import spacy
import dateparser
import json

nlp = spacy.load("en_core_web_sm")
TASK_FILE = "tasks.json"

def handle_nlp_command(command):
    
    action = detect_command(command)
    task = extract_tasks(command)

    if action == "add":
        tasks.append(task)
        save_tasks()
        print(f"Added task: {task}")

    elif action == "remove":
        if tasks in tasks:
            tasks.remove(task)
            save_tasks()
            print(f"Remove task: {task}")
        else:
            print("Task not found...")

    else:
        print("Sorry, I didnt understand that.")

def detect_command(command):

    doc = nlp(command)

    for token in doc:
        if token.lemma__ in ["add", "include"]:
            return "add"
        elif token.lemm__ in ["remove", "delete", "clear"]:
            return "remove"
        
    return None

# Extract main task description and detect due dates if a there are any
def extract_tasks(command):

    doc = nlp(command)
    keywords = [token.text for token in doc if token.pos_ in ("NOUN", "VERB")]
    task_description = " ". join(keywords)

    parsed_date = dateparser.parse(command)

    return {"task": task_description, "due_date": str(parsed_date) if parsed_date else None}

# A function to load the tasks into the json file
# File is opened in read mode
# Added error checking for if the file might not exist 
# Retunr an empty list list if the file is missing or empty
def load_task():

    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Saving tasks that the user wanted to the json file
# Done this by setting write permission in the file and adding the task
# If the file doesnt exist it is created and if it already exists it is over written
# After writing the file is automatically closed
def save_tasks():

    with open(TASK_FILE, "w") as file:
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
        save_tasks()
        print(f"Removed task: {task}")

    else: print("Task not found...")



def add_task():

    if len(tasks) >= 10 : 
        print("You have to many task! Stop being a lazy bum and get shit done first...")
        return

    add = input("What task would you like to add?: ")
    tasks.append(add)
    save_tasks()
    print(f"Added tasks: {add}")
    

def print_menu():

    print("====Welcome to the Crispy Todo List====")

    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display tasks")
    print("4. Quit")



if __name__ == "__main__":

    tasks = load_task()

    while True:

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


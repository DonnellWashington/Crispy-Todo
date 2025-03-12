import os
import spacy
import dateparser
import json


nlp = spacy.load("en_core_web_sm")
TASK_FILE = "tasks.json"

def handle_nlp_command(command):

    global tasks
    
    action, task, task_date = detect_command(command)

    if action == "add":
        task_data = {"task": task, "due_date": task_date}
        tasks.append(task_data)
        save_tasks()
        print(f"Added task: {task}")

    elif action == "remove":
        if any(t["task"] == task for t in tasks):
            tasks[:] = [t for t in tasks if t["task"] != task]
            save_tasks()
            print(f"Remove task: {task}")
        else:
            print("Task not found...")


    elif action == "display": print_tasks()

    elif action == "quit":
        print("Goodbye")
        exit()
    
    else:
        print("Sorry, I didnt understand that.")


# A function to detect the command in the users tasks (add/remove/show) and such
# Detect verbs, tasks and dates
def detect_command(user_input):

    doc = nlp(user_input.lower())

    verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    nouns_chunks = [chunk.text for chunk in doc.noun_chunks]
    task = " ".join(nouns_chunks)

    detected_date = dateparser.parse(user_input)
    format_date = detected_date.strftime("%Y-%m-%d") if detected_date else None

    if "add" in verbs or "create" in verbs:
        return ("add", task, format_date)

    elif "remove" in verbs or "delete" in verbs:
        return ("remove", task, None)
    
    elif "show" in verbs or "display" in verbs or "list" in verbs:
        return ("display", None, None)
    
    elif "quit" in verbs or "exit" in verbs:
        return ("quit", None, None)

    return "unknown", None, None

# Extract main task description and detect due dates if a there are any
def extract_tasks(command):

    doc = nlp(command)
    keywords = [chunk.text for chunk in doc.noun_chunks]
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

    global tasks
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def print_tasks():

    if not tasks: print("You currently have no tasks")

    else:
        print("\n==== Your Tasks ====")
        for i, task in enumerate(task, 1):
            print(f"{i}. {task['task']} (Due: {task['due_date'] or 'No due date'})")


# A function to remove a task from the list by selecting a number
def remove_task():

    global tasks
    print_tasks()

    try:
        task_num = int(input("Which number task would you like to remove? "))

        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks()
            print(f"Removed task: {removed_task['task']}")
        else: print("Invalid taks number")

    except ValueError:
        print("Please enter a valid number.")


# Add a new task with natural language processing
def add_task():

    global tasks

    if len(tasks) >= 10 : 
        print("You have too many task! Stop being a lazy bum and get shit done first...")
        return

    add = input("What task would you like to add?: ")
    extracted_task = extract_tasks(add)

    if extracted_task["task"]:
        tasks.append(extracted_task)
        save_tasks()
        print(f"Added tasks: {extracted_task}")
    else : print("Sorry I couldnt understand that. Please try again...")


# A function to print the menu
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
            user_input = int(input("What would you like to do?: "))

        except ValueError:
            print("Invalid choice please select a number between 1-4")
            continue

        if user_input == 1: add_task()
        
        elif user_input == 2 : remove_task()

        elif user_input == 3 : print_tasks()

        elif user_input == 4 :
            print("See you later!")
            break

        else : print("Invalid choice please select a number between 1-4")


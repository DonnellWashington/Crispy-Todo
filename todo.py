def print_tasks():

    print("The tasks are to be printed here")

def todo_list():
    tasks = []

    while True:
        print("====Welcome to the Crispy Todo List====")
        print("What would you like to do?")
        print("\n")

        print("1. Add a task")
        print("2. Remove a Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input()

        if choice == 1:
            print("What would you like to add?")

        elif choice == 2:
            # Add a condition here to say if the list is empty
            # Tell them the list is empty


        elif choice == 3:
            print_tasks()
        
        
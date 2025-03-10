def print_tasks():

    for task in tasks:
        print(task)


def remove_task():

    print_tasks()

    task = input("Which task would you like to remove?: ")

    if task in tasks: tasks.remove(task)

    else: 
        print("That task couldnt be found")
        exit()



def add_task():

    print("What task would you like to add")
    add = input()

    tasks.append("HELLOW")
    
    


def print_menu():

    print("====Welcome to the Crispy Todo List====")
    print("What would you like to do?\n")

    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display tasks")
    print("4. Quit")



if __name__ == "__main__":

    tasks = []

    while True:
        print_menu()

        choice = input()

        if choice == 1: 
            if len(tasks) >= 10: 
                print("You currently have more than 10 tasks...\n")
                print("Stop being a lazy bum and get shit done...")
                exit()
            else: add_task()
        
        elif choice == 2 : 
            if len(tasks) == 0: 
                print("You currently have no tasks...\n")
                print("Would you like to add one?")
                choice = input()
                if choice == 'y': add_task()
                elif choice == 'n': exit()
            else : remove_task()

        elif choice == 3 : print_tasks()

        elif choice == 4 : exit()


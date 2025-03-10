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

    tasks.append(add)
    
    


def print_menu():

    print("====Welcome to the Crispy Todo List====")
    print("What would you like to do?\n")

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
            

        if choice == 1: add_task()
        
        elif choice == 2 : remove_task()

        elif choice == 3 : print_tasks()

        elif choice == 4 :
            print("See you later!")
            break

        else : print("Invalid choice please select a number between 1-4")


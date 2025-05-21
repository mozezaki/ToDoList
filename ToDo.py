import os

def menu() :
    print("--- TO-DO LIST --- \n "
    "1. Add Task \n "
    "2. Show Tasks \n "
    "3. Delete Task \n "
    "4. Delete All \n "
    "5. Edit Task \n "
    "6. Exit")

def addTask(task , task_list) :      # user enters task #
    task_list.append(task)
    save_to_file(task_list)

def showTasks(task_list) :       # shows all tasks #
    for i, task in enumerate(task_list):
        print(f"{i + 1}. {task}")

def save_to_file(task_list):
    with open("todo.txt", "w") as f:
        for task in task_list:
            f.write(task + "\n")


def deleteTask(x , task_list) :        # user enters index of task #
    del task_list[x]
    save_to_file(task_list)

def deleteAll(task_list) :
    task_list.clear()
    save_to_file(task_list)

def editTask(x , task , task_list) :
    task_list[x] = task
    save_to_file(task_list)


def main() :
    task_list = []
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as f:
             task_list = [line.strip() for line in f.readlines()]
    
    while True :
        menu()
        choice = input("Press the number of your desired action ")
        if  choice == "6" :
            print("Exiting... ")
            break
        elif choice == "1" :
            task = input("Type your task: ")
            addTask(task , task_list) 
            print("Task Added. ")
        elif choice == "2" :
            if not task_list :
                print("No tasks... ")
            else :
                showTasks(task_list)
        elif choice == "3" :
            if not task_list :
                print("No tasks to delete... ")
            else :
                num = int(input("Enter the number of task you want to delete "))
                if 1 <= num <= len(task_list) :
                    deleteTask(num - 1 , task_list)
                    print("Task deleted. ")
                else :
                     print("Error")
                    
        elif choice == "4" :
            if not task_list :
                print("No tasks to delete... ")
            else :
                deleteAll(task_list)
                print("Tasks Deleted. ")
        elif choice == "5" :
            num = int(input("Enter number of task you want to edit "))
            task = input("Enter edit ")
            if 1 <= num <= len(task_list) :
                editTask(num - 1 ,task , task_list)
                print("Edited. ")
            else :
                print("Error")
        else :
            print("ERROR")
            
            


if __name__ == "__main__" :
    main()

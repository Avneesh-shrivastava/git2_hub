def main():    
    print("\nwelcome to to-do list\n")
    print("Main menu")
    print("1. Add list ")
    print("2. View list")
    print("3. Delete list")
    print("4. Mark list as done")
    print("5. Exit")
    global select 
    print()
    select = input("select any one option (1 - 5): ")
    
global todo 
todo = []
task_done = -1

def enter_list():
        
        print("\nTO-DO LIST")
        i=0
        while i <= len(todo) :
            things_todo = input("type the things you want to do today: ")
            todo.append(things_todo)
            print("list added : " + things_todo)
            
            a = int(input("Do you want to add another list? (1 -> yes, 2 -> No) : "))
            if a == 1:
                i = i + 1
            else: 
                break

def done_func():
    global task_done
    task_done = int(input("enter the list no. you wanted to be marked as done : "))
    task_done = task_done - 1
    todo[task_done] = "✅"+" "+todo[task_done]
    m = 0
    j = 1
    while m < len(todo):
        print(j,"."," ",todo[m])
        m = m + 1
        j = j + 1

def show_list():
    print()
    print("Viewing list")
    j = 1
    i = 0
    while i < len(todo):
        print(j,"."," ",todo[i])
        j = j + 1
        i = i + 1
    print()

def delete_list():
    show_list()
    d = int(input("which index do you want to delete from the list : "))
    del todo[d - 1]

def permit():
    print()
    per = 1
    while per <= 5:
        cont = input("Press Enter to continue 😎 ")
        if cont == "":
            break
        else:
            print("Can't you see the Enter button, You idiot! 😤")
        per = per + 1

    if per == 6:
        print("Im done with you Bye Bye YOU Idiot! 🤬")        

def main_game():
    i = -1
    while i < len(todo):
        main()
        if select == "1":
            enter_list()
        elif select == "2":
            show_list()
            permit()

        elif select == "3":
            delete_list()
            permit()

        elif select == "4":
            show_list()
            done_func()
            permit()
        elif select == "5":
            print("Bye have a nice day\n")
            print()
            break
            
main_game()
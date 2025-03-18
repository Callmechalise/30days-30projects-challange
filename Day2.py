import sys

list=[]

def add_task():
    print("Enter Task")
    task=input()
    list.append(task)
def view_task():
    x=0
    for i in list:
        print(f"Task{x+1}:\n{i}")
        x=x+1
def delete_task():
    view_task()
    print('Enter Task no you want to delete:\n')
    try:
        d=int(input("==>"))
        list.pop(d-1)
    except Exception as e:
        print(e)
def complete_task():
    view_task()
    print('Enter Task no you completed:\n')
    try:
        d=int(input("==>"))
        list.pop(d-1)
        print("Congratulations task is completed")
    except Exception as e:
        print(e)
def quit():
    with open('task.txt', 'w') as f:
        f.write(str(list))
    sys.exit()
def menu():
    print("Enter operation you want to perform\n")
    print("=====================================")
    print('1:View task\n')
    print('2:Add Task\n')
    print('3:Task completed\n')
    print('4:Delete Task\n')
    print('5:Quit')
    try:
        inp=input(":::->")
        if(inp=='1'):
            view_task()
        elif(inp=='2'):
            add_task()
        elif(inp=='3'):
            complete_task
        elif(inp=='4'):
            delete_task()
        elif(inp=='5'):
            quit()
    except ValueError:
            print('Oops invalid input\n')
    except Exception as e:
            print(e)
if __name__=="__main__":
    while True:
        menu()

print("Enter 'M' to create tasks, 'S' to show task and 'D' to delete task")
while True:
    ch = input("Enter your choice : ")
    if ch == "M":
        todo = []
        while True:
            task = input("Enter task (enter done to end) : ")
            if task == "done":
                print("todo saved")
                break
            todo.append(task)

    if ch == "S":
        try:
            for i in todo:
                print(i)
        except:
            print("No any task is saved")
        
    if ch == "D":
        del_task = input("Enter the task that you want to delete : ")
        if del_task in todo:
            print("print task deleted")
            todo.remove(del_task)
        else:
            print("the task is not in list")


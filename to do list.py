tasks = []

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    select = input("Number Selected: ")
    
    if select == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")
    
    elif select == '2':
        if tasks:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks to show.")
    
    elif select == '3':
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' removed!")
        else:
            print("Invalid task number.")
    
    elif select == '4':
        print("Exiting the program.Bye!")
        break
    
    else:
        print("Invalid.")

tasks = []

while True:
    print("\n-------------TO DO LIST----------------")
    print("1. Add task")
    print("2. View task")
    print("3. Delete task")
    print("4. Exit")

    choice= input("Enter choice:")

    if choice == "1":
        task= input("enter task:")
        tasks.append(task)
        print("task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t}")

    elif choice == "3":
        task = int(input("Enter task to delete:"))
        tasks.pop(task- 1)
        print("Task deleted!")

    elif choice == "4":
        print("goodbye")

    else: 
        print("invalid input")



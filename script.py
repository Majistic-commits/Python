from os import WCONTINUED

task = {}  # MOVED OUTSIDE LOOP - tasks now persist
running = True

while running:
    print("-" * 30)
    print("1.List Current Tasks\n2.Add A Task\n3.Mark Task As In Progress\n4.Mark Task As Done\n5.Exit")
    print("-" * 30)

    # IMPROVED ERROR HANDLING - keeps asking until valid input
    while True:
        try:
            print("-" * 30)
            c = int(input("Enter Your Choice: "))
            print("-" * 30)
            if 1 <= c <= 5:
                break  # Valid input, exit the input loop
            else:
                print("Invalid Choice! Please enter 1-5")
        except ValueError:
            print("Invalid input! Please enter a number")

    if c == 1:
        if not task:
            print("No Tasks")
        else:
            print("Here Are Your Tasks:")
            for key, value in task.items():
                print(f"  {key}: {value}")

    elif c == 2:
        key = input("Enter Your Task: ")
        value = input("How would you like to mark this task: ")
        task[key] = value
        print(f"Task '{key}' added successfully!")

    elif c == 3:
        if not task:  # CHECK IF TASKS EXIST
            print("No tasks available to mark as in progress")
        else:
            print("Available tasks:")
            for key, value in task.items():
                print(f"  {key}: {value}")

            # ASK WHICH TASK TO UPDATE
            task_to_update = input("Enter the task name to mark as in progress: ")

            if task_to_update in task:
                in_progress = input("Do You Want To Mark Task As In Progress y/n: ")
                if in_progress.lower() == 'y':
                    task[task_to_update] = "In Progress"
                    print(f"Task '{task_to_update}' marked as In Progress")
                elif in_progress.lower() == 'n':
                    print("Operation cancelled")
                else:
                    print("Invalid Choice")
            else:
                print("Task not found!")

    elif c == 4:
        if not task:  # CHECK IF TASKS EXIST
            print("No tasks available to mark as done")
        else:
            print("Available tasks:")
            for key, value in task.items():
                print(f"  {key}: {value}")

            # ASK WHICH TASK TO UPDATE
            task_to_update = input("Enter the task name to mark as done: ")

            if task_to_update in task:
                done = input("Do You Want To Mark Task As Done y/n: ")  # FIXED TEXT
                if done.lower() == 'y':
                    task[task_to_update] = "Done"
                    print(f"Task '{task_to_update}' marked as Done")
                elif done.lower() == 'n':
                    print("Operation cancelled")
                else:
                    print("Invalid Choice")
            else:
                print("Task not found!")

    elif c == 5:
        # SHOW FINAL TASKS BEFORE EXIT
        if task:
            print("Your final tasks:")
            for key, value in task.items():
                print(f"  {key}: {value}")

        escape = input("Do You Want To Exit Or Continue? (Y/N): ")
        if escape.upper() == 'Y':
            print("Thank you for using the task manager!")
            print("Goodbye! 👋")
            running = False
        elif escape.upper() == 'N':
            print("Continuing with your tasks...")
        else:
            print("Invalid Choice. Please enter Y or N")
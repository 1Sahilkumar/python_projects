tasks = []
# Add Task Function
def addTask(Tasks):
    tasks.append({"task": Tasks, "status": "Pending"})

# Remove Task Function    
def removeTask(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"'{removed['task']}' removed from list.")
    except IndexError:
        print("Invalid task number.")


# Update Task Function
def updateTask(index):
    try:
        print(f"Current Task: {tasks[index - 1]['task']}")
        new_task = input("Enter the Updated Task: ")
        tasks[index - 1]['task'] = new_task   
        print("Task updated successfully.") 
    except IndexError:
        print("Invalid task number.")

# Mark AS Complete Function        
def markAsCompleted(index):
    try:
        if tasks[index-1]["status"] == "Pending":
            tasks[index-1]["status"] = "Completed"
            print("Task marked as completed.")
        else:
            print("Already completed.")
    except IndexError:
        print("Invalid task number.")
          
print("----------ToDo List--------------")
print("1.View List")
print("2.Add Task")
print("3.Remove Task")
print("4.Update Task")
print("5.Mark As Completed")
print("6.Exit")

while True:
  try:  
    option = int(input("Enter option number : "))
    if option == 1:
        if not tasks:
            print("There is no todo task added yet")
        else:    
            print("Your ToDO List: \n")
            for i ,n in enumerate(tasks , start=1):
                 print(f"{i}. {n['task']} [{n['status']}]")
    elif option == 2:
        Tasks = input("Enter task:")
        addTask(Tasks)
    elif option == 3:
        if not tasks:
                print("📭 No tasks to remove.")
        else:
                for i, n in enumerate(tasks, start=1):
                    print(i, ".", n)
                delete = int(input("Enter task number to delete: "))
                removeTask(delete) 
    elif option == 4:
         if not tasks:
                print("No tasks to update.")
         else:
            for i ,n in enumerate(tasks , start=1):
                 print(f"{i}. {n['task']} [{n['status']}]")
            update = int(input("Enter task number to update: "))
            updateTask(update)
    elif option == 5:
         if not tasks:
                print("No tasks to update.")
         else:
            for i ,n in enumerate(tasks , start=1):
                 print(f"{i}. {n['task']} [{n['status']}]")
            mark = int(input("Enter task number To Mark it as completed :"))
            markAsCompleted(mark)
    elif option == 6:
         print("See You Soon")
         break
    else:
         print("Invalid Option")           
  
  except ValueError:
         print("Please enter numbers only.")
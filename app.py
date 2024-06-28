#To-Do List task will be seperated by incomplete and completed
tasks = []
completed_tasks = []

#This will add a task to the task list while also adding the "incomplete" tag
def add_task():
    try:
        task = input("Enter a new task that you would like to add to the To-Do List: ")
        tasks.append(task + " (incomplete)")
        print("You have successfully added a new task! ")
    except Exception as e:
        print(f"Error occurred whjile adding task: {e}")

#This will view the tasks showing which are incomplete and completed tasks
def view_task():
    try:                                        
        if len(tasks) == 0:
            print("No tasks available ")
        else:
            print("To-Do List")
            for i,  task in enumerate(tasks):
                print(f"{i + 1}) {task}")
    
        if len(completed_tasks) == 0:
            print("No completed tasks ")
        else:
            for i, completed_task in enumerate(completed_tasks):
                print(f"{i + 1}) {completed_task}")
    except Exception as e:
        print(f"Error occurred while viewing tasks: {e}")    

#This will mark a task as completed and also remove it from the incomplete tasks
def mark_task_as_complete():
    try:
        global tasks, completed_tasks       
    
        if len(tasks) == 0:
            print("No tasks available ")
            return
    
        print("Which task would you like to mark as complete? ")
        for i, task in enumerate(tasks):
            print(f"{i + 1}) {task}")
    
        choice = int(input("Enter the number of the task you wish to mark as complete: "))

        if 1 <= choice <= len(tasks):
            completed_task = tasks[choice - 1].replace("(incomplete)", "(completed)")
            completed_tasks.append(completed_task)  # Append completed task to completed_tasks
            del tasks[choice - 1]           #delete task from task list
            print("You have successfully marked a task as completed! ")
        else:
            print("Error Invalid Input!")
    except ValueError:
        print("Error: Please enter a valid number.")
    except Exception as e:
        print(f"Error occurred while marking task as complete: {e}")

#This will delete a task from the list
def delete_task():
    try:
        if len(tasks) == 0:
            print("There are no tasks available to delete")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}) {task}")
    
        choice = int(input("Enter the number of the task you wish to delete: "))
        
        if 0 < choice <= len(tasks):
            del tasks[choice -1]
            print("Task successfully deleted!")
        else:
            print("Error Invalid Input!")
    except ValueError:
        print("Error please enter a valid number: ")
    except Exception as e:
        print(f"Error  occurred while deleting task: {e}")

#Our starting point which includes the interface of the app and the options
def main():
    try:
        while True:
            print("\n===== To-Do List =====")
            print("1. Add a Task")
            print("2. View Tasks")
            print("3. Mark a Task as Complete")
            print("4. Delete a Task")
            print("5. Quit")
        
            choice = int(input("Choose an option: "))
        
            if choice == 1:
                add_task()
            elif choice == 2:
                view_task()
            elif choice == 3:
                mark_task_as_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                break
            else:
                print("Invalid input. Please try again. ")
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        print("Exiting program. Goodbye!")

if __name__ == "__main__":
    main()

tasks = []

def display_menu():
    """Prints the main menu options to the user."""
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Quit")
    print("-----------------------")

def add_task():
    """Prompts the user for a task and adds it to the list."""
    task_description = input("Enter the task you want to add: ").strip()
    if task_description: 
        tasks.append(task_description)
        print(f"'{task_description}' has been added to your to-do list.")
    else:
        print("Task description cannot be empty. Please try again.")

def view_tasks():
    """Displays all tasks in the list, with their numbers."""
    if not tasks: 
        print("Your to-do list is empty. Add some tasks!")
    else:
        print("\n--- Your Tasks ---")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
        print("------------------")

def mark_task_complete():
    """Allows the user to mark a task as complete by its number."""
    view_tasks() 
    if not tasks:
        return 

    try:
        task_num_str = input("Enter the number of the task to mark as complete: ")
        task_number = int(task_num_str) 

        
        task_index = task_number - 1

        if 0 <= task_index < len(tasks): 
            tasks[task_index] = tasks[task_index] + " (DONE)"
            print(f"Task '{task_index + 1}' marked as complete.")
        else:
            print("Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_task():
    """Allows the user to delete a task by its number."""
    view_tasks() 
    if not tasks:
        return 

    try:
        task_num_str = input("Enter the number of the task to delete: ")
        task_number = int(task_num_str)

        
        task_index = task_number - 1

        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index) 
            print(f"Task '{removed_task}' has been deleted.")
        else:
            print("Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def run_todo_list():
    """Main function to run the To-Do List application."""
    print("Welcome to your Command-Line To-Do List!")

    while True: 
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break 
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# This line calls the main function to start the program
if __name__ == "__main__":
    run_todo_list()

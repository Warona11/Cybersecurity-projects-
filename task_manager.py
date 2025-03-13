
import os
from datetime import datetime

def read_file(file_name):
    """Read the content of a file, creating it if it doesn't exist."""
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            pass
    with open(file_name, 'r') as file:
        return file.readlines()

def write_file(file_name, lines):
    """Write lines to a file."""
    with open(file_name, 'w') as file:
        file.writelines(lines)

def append_file(file_name, line):
    """Append a line to a file."""
    with open(file_name, 'a') as file:
        file.write(line + '\n')

def format_date(date_str):
    """Convert a date string into a datetime object."""
    return datetime.strptime(date_str, "%d %b %Y")

def login():
    """Authenticate the user before granting access."""
    users = read_file('user.txt')
    credentials = {line.strip().split(';')[0]: line.strip().split(';')[1] for line in users}
    
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username in credentials and credentials[username] == password:
            print("Login successful!\n")
            return username
        else:
            print("Invalid username or password. Try again.")

def reg_user():
    """Register a new user with unique username and password confirmation."""
    users = read_file('user.txt')
    usernames = [line.split(';')[0] for line in users]
    
    while True:
        username = input("Enter new username: ")
        if username in usernames:
            print("Username already exists. Try again.")
        else:
            break
    
    password = input("Enter new password: ")
    confirm_password = input("Confirm password: ")
    
    if password == confirm_password:
        append_file('user.txt', f"{username};{password}")
        print("User registered successfully.")
    else:
        print("Passwords do not match.")

def add_task():
    """Add a new task assigned to a specific user."""
    users = read_file('user.txt')
    usernames = [line.split(';')[0] for line in users]
    
    while True:
        username = input("Enter username to assign task: ")
        if username not in usernames:
            print("User does not exist. Try again.")
        else:
            break
    
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (dd MMM yyyy): ")
    current_date = datetime.now().strftime("%d %b %Y")
    completed = "No"
    
    append_file('tasks.txt', f"{username};{title};{description};{current_date};{due_date};{completed}")
    print("Task added successfully.")

def generate_reports():
    """Generate reports on task and user statistics."""
    tasks = read_file('tasks.txt')
    users = read_file('user.txt')
    usernames = [line.split(';')[0] for line in users]
    
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task.strip().split(';')[5] == "Yes")
    incomplete_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in tasks if task.strip().split(';')[5] == "No" and format_date(task.strip().split(';')[4]) < datetime.now())
    
    write_file('task_overview.txt', [
        f"Total tasks: {total_tasks}\n",
        f"Completed tasks: {completed_tasks}\n",
        f"Incomplete tasks: {incomplete_tasks}\n",
        f"Overdue tasks: {overdue_tasks}\n",
        f"Percentage incomplete: {incomplete_tasks / total_tasks * 100:.2f}%\n" if total_tasks > 0 else "Percentage incomplete: 0.00%\n",
        f"Percentage overdue: {overdue_tasks / total_tasks * 100:.2f}%\n" if total_tasks > 0 else "Percentage overdue: 0.00%\n"
    ])
    
    user_stats = []
    for username in usernames:
        user_tasks = [task for task in tasks if task.split(';')[0] == username]
        total_user_tasks = len(user_tasks)
        completed_user_tasks = sum(1 for task in user_tasks if task.strip().split(';')[5] == "Yes")
        incomplete_user_tasks = total_user_tasks - completed_user_tasks
        
        user_stats.append(
            f"{username}:\n"
            f"  Total tasks assigned: {total_user_tasks}\n"
            f"  Percentage of total tasks: {total_user_tasks / total_tasks * 100:.2f}%\n" if total_tasks > 0 else "  Percentage of total tasks: 0.00%\n",
            f"  Percentage completed: {completed_user_tasks / total_user_tasks * 100:.2f}%\n" if total_user_tasks > 0 else "  Percentage completed: 0.00%\n",
            f"  Percentage incomplete: {incomplete_user_tasks / total_user_tasks * 100:.2f}%\n" if total_user_tasks > 0 else "  Percentage incomplete: 0.00%\n"
        )
    
    write_file('user_overview.txt', user_stats)
    print("Reports generated successfully.")

def main():
    """Main function that displays the menu after authentication."""
    current_user = login()
    
    while True:
        print("\nSelect an option:")
        print("r - Register user")
        print("a - Add task")
        print("gr - Generate reports")
        print("e - Exit")
        
        choice = input(": ").lower()
        if choice == 'r':
            reg_user()
        elif choice == 'a':
            add_task()
        elif choice == 'gr':
            generate_reports()
        elif choice == 'e':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

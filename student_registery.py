# Ask the user how many students are registering
num_students = int(input("Enter the number of students registering: "))

# Open a file named reg_form.txt in write mode
with open("reg_form.txt", "w") as file:
    # Loop for the number of students
    for i in range(num_students):
        # Ask the user to enter the student ID
        student_id = input(f"Enter the ID for student {i + 1}: ")
        # Write the student ID followed by a dotted line to the file
        file.write(student_id + "\n")
        file.write("-" * 30 + "\n")  # Add a dotted line for clarity

print("Student registration completed. Check the 'reg_form.txt' file.")

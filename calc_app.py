import os

def perform_calculation():
    try:
        # Get inputs from the user
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        # Perform the calculation based on the operator
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operator. Please use one of +, -, *, /.")
            return

        # Display the result
        equation = f"{num1} {operator} {num2} = {result}"
        print("Result:", equation)

        # Write the equation to the file
        with open("equations.txt", "a") as file:
            file.write(equation + "\n")

    except ValueError:
        print("Error: Please enter valid numeric inputs.")

def display_equations():
    # Check if the file exists
    if not os.path.exists("equations.txt"):
        print("No previous calculations found.")
        return

    # Read and display the content of the file
    with open("equations.txt", "r") as file:
        content = file.read()
        if content.strip():
            print("Previous calculations:")
            print(content)
        else:
            print("No previous calculations found.")

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Perform a calculation")
        print("2. View previous calculations")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            perform_calculation()
        elif choice == "2":
            display_equations()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

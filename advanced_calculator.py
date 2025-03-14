import math

# Function to display the menu
def display_menu():
    print("\nAdvanced Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm (base 10)")
    print("11. Exit")

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

# Function to perform exponentiation
def power(x, y):
    return x ** y

# Function to perform square root
def square_root(x):
    if x < 0:
        return "Error: Negative input!"
    return math.sqrt(x)

# Function to perform sine
def sine(x):
    return math.sin(math.radians(x))  # Convert degrees to radians

# Function to perform cosine
def cosine(x):
    return math.cos(math.radians(x))  # Convert degrees to radians

# Function to perform tangent
def tangent(x):
    return math.tan(math.radians(x))  # Convert degrees to radians

# Function to perform logarithm (base 10)
def logarithm(x):
    if x <= 0:
        return "Error: Invalid input!"
    return math.log10(x)

# Main function
def calculator():
    while True:
        display_menu()
        choice = input("Enter your choice (1-11): ")

        if choice == '11':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {power(num1, num2)}")
        elif choice == '6':
            try:
                num = float(input("Enter the number: "))
                print(f"Result: {square_root(num)}")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif choice == '7':
            try:
                angle = float(input("Enter the angle in degrees: "))
                print(f"Result: {sine(angle)}")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif choice == '8':
            try:
                angle = float(input("Enter the angle in degrees: "))
                print(f"Result: {cosine(angle)}")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif choice == '9':
            try:
                angle = float(input("Enter the angle in degrees: "))
                print(f"Result: {tangent(angle)}")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif choice == '10':
            try:
                num = float(input("Enter the number: "))
                print(f"Result: {logarithm(num)}")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        else:
            print("Invalid choice! Please select a valid option.")

# Run the calculator
if __name__ == "__main__":
    calculator()
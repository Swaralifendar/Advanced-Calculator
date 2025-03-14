import tkinter as tk
from tkinter import messagebox
import math

# Function to update the display
def update_display(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        expression = display.get()
        result = str(eval(expression))  # Evaluate the expression
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function for square root
def square_root():
    try:
        value = float(display.get())
        if value < 0:
            messagebox.showerror("Error", "Negative input!")
        else:
            result = math.sqrt(value)
            display.delete(0, tk.END)
            display.insert(0, result)
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

# Function for trigonometric functions (sin, cos, tan)
def trig_function(func):
    try:
        value = float(display.get())
        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        display.delete(0, tk.END)
        display.insert(0, result)
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x500")

# Create the display
display = tk.Entry(root, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('√', 5, 1), ('sin', 5, 2), ('cos', 5, 3),
    ('tan', 6, 0)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=("Arial", 18), command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, font=("Arial", 18), command=clear_display)
    elif text == '√':
        button = tk.Button(root, text=text, font=("Arial", 18), command=square_root)
    elif text in ['sin', 'cos', 'tan']:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda f=text: trig_function(f))
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: update_display(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Configure row and column weights
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
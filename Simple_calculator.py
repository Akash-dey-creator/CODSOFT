import tkinter as tk
from tkinter import messagebox

def button_click(number):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current + str(number))

def button_clear():
    entry_display.delete(0, tk.END)

def button_backspace():
    current = entry_display.get()
    if current:
        entry_display.delete(len(current) - 1, tk.END)

def button_point():
    current = entry_display.get()
    if '.' not in current:
        entry_display.insert(tk.END, '.')

def buttnon_addition():
    try:
        num1 = float(entry_display.get())
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(num1) + "+")
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")

def buttnon_subtraction():
    try:
        num1 = float(entry_display.get())
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(num1) + "-")
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")

def buttnon_multiply():
    try:
        num1 = float(entry_display.get())
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(num1) + "*")
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")

def buttnon_division():
    try:
        num1 = float(entry_display.get())
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(num1) + "/")
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")

def buttnon_equal():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression")

root = tk.Tk()
root.title("Simple Calculator")

entry_display = tk.Entry(root, width=25, font=('Times New Roman', 14))
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady= 10)

buttons = [
    ('DEL', 1, 2), ('AC', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('/', 5, 3),
]

for (text, row, column) in buttons:
    if text == 'AC':
        button = tk.Button(root, text=text, width=5, height=2, command=button_clear)
    elif text == 'DEL':
        button = tk.Button(root, text=text, width=5, height=2, command=button_backspace)
    elif text == '=':
        button = tk.Button(root, text=text, width=5, height=2, command=buttnon_equal)
    elif text in ('+', '-', '*', '/'):
        button = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: buttnon_addition() if t == '+' else buttnon_subtraction() if t == '-' else buttnon_multiply() if t == '*' else buttnon_division())
    else:
        button = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: button_click(t))
    button.grid(row=row, column=column, padx=5, pady=5)

root.mainloop()
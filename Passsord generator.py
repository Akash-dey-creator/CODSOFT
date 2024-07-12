import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "@&#"

    password = []
    password.append(random.choice(lowercase_letters))
    password.append(random.choice(uppercase_letters))
    password.append(random.choice(digits))
    password.append(random.choice(special_characters))

    for _ in range(length - 4):
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    random.shuffle(password)

    return ''.join(password)

def generate_password_button_clicked():
    try:
        length = int(length_entry.get())
        if length <= 4:
            messagebox.showerror("Error", "Length must be greater than 4.")
        elif length >= 51:
            messagebox.showerror("Error", "Length must be less than 51.")
        else:
            password = generate_password(length)
            generated_password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for length.")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter the length of the password:")
length_label.pack(pady=10)

length_entry = tk.Entry(root, width=30)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_button_clicked)

generate_button.pack(pady=10)

generated_password_label = tk.Label(root, text="")
generated_password_label.pack(pady=10)

root.mainloop()

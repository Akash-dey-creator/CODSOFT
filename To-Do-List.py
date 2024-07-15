import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")
root.configure(bg='black')

root.geometry("500x500")

task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
task_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear All Tasks", command=clear_tasks)
clear_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
from tkinter import *
import random

tasks = []
random_tasks = ["Program Two Hours", "Wash the Dishes", "Take Out The Trash", "Drink Daily Tea", "Wait for Mother"]

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    global tasks

    tasks.append(txt_input.get())
    tasks = set(tasks)
    update_listbox()
    tasks = list(tasks)

def delete_all():
    global tasks

    tasks = []
    update_listbox()

def delete_task():
    del tasks[-1]
    update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def choose_random_task():
    global tasks

    tasks.append(random.choice(random_tasks))
    tasks = set(tasks)
    update_listbox()
    tasks = list(tasks)

def check_number_of_tasks():
    global tasks

    tasks_length = len(tasks)
    number_of_tasks = Label(root, text=str(len(tasks)))
    number_of_tasks.grid(row=13, column=1)
    if tasks_length != len(tasks):
        number_of_tasks = Label(root, text=str(len(tasks)))
        number_of_tasks.grid(row=13, column=1)
    

def exit():
    root.destroy()

root = Tk()
root.configure(bg="white")
root.title("My To-Do List")
root.geometry("130x450")

lbl_title = Label(root, text="To Do List", bg="white")
lbl_title.grid(row=1, column=1)

lbl_display = Label(root, text="", bg="white")
lbl_display.grid(row=2, column=1)

txt_input = Entry(root, width=15)
txt_input.grid(row=3, column=1)

button_add_task = Button(root, text="Add Task",fg="green", bg="white", command=add_task)
button_add_task.grid(row=4, column=1)

button_delete_all = Button(root, text="Delete All Tasks",fg="green", bg="white", command=delete_all)
button_delete_all.grid(row=5, column=1)

button_delete_one = Button(root, text="Delete",fg="green", bg="white", command=delete_task)
button_delete_one.grid(row=6, column=1)

button_sort_asc = Button(root, text="Sort List (ASC)",fg="green", bg="white", command=sort_asc)
button_sort_asc.grid(row=7, column=1)

button_sort_desc = Button(root, text="Sort List (DESC)",fg="green", bg="white", command=sort_desc)
button_sort_desc.grid(row=8, column=1)

button_choose_random = Button(root, text="Add Random Task",fg="green", bg="white", command=choose_random_task)
button_choose_random.grid(row=9, column=1)

button_number_of_tasks = Button(root, text="Number of Tasks",fg="green", bg="white", command=check_number_of_tasks)
button_number_of_tasks.grid(row=10, column=1)

button_exit = Button(root, text="Exit Program",fg="green", bg="white", command=exit)
button_exit.grid(row=11, column=1)

lb_tasks = Listbox(root)
lb_tasks.grid(row=12, column=1)

root.mainloop()

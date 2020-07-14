from tkinter import *
import random
import os
import json


def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    global tasks

    tasks.append("'" + txt_input.get() + "'")
    # tasks = set(tasks)
    update_listbox()
    tasks = list(tasks)

def delete_all():
    global tasks

    tasks = []
    update_listbox()

def delete_task():
    del tasks[int(delete_input.get())-4]
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
    number_of_tasks.grid(row=16, column=4)
    if tasks_length != len(tasks):
        number_of_tasks = Label(root, text=str(len(tasks)))
        number_of_tasks.grid(row=16, column=4)
    

def exit():
    f = open("save_data.txt", "w")
    f.write(str(tasks))
    f.close()
    root.destroy()

### program starts ###

filesize = os.path.getsize("save_data.txt")

random_tasks = ["'Program Two Hours'", "'Wash the Dishes'", "'Take Out The Trash'", "'Drink Daily Tea'", "'Wait for Mother'", "'Eat Sweets'", "'Eat Veggies'"]

if filesize == 0:
    tasks = []
else:
    f = open("save_data.txt", "r")
    text = f.read()
    tasks = text.strip('][').split(', ')
    f.close()

root = Tk()
root.configure(bg="white")
root.title("My To-Do List")
root.geometry("360x520")

lb_tasks = Listbox(root)
lb_tasks.grid(row=15, column=4)

lbl_title = Label(root, text="To Do List", bg="white")
lbl_title.grid(row=1, column=4)

lbl_display = Label(root, text="", bg="white")
lbl_display.grid(row=2, column=4)

add_label = Label(root, text="Add A Task", bg="white")
add_label.grid(row=3, column=4)

txt_input = Entry(root, width=15)
txt_input.grid(row=4, column=4)

delete_label = Label(root, text="Delete A Task", bg="white")
delete_label.grid(row=5, column=4)

delete_input = Entry(root, width=15)
delete_input.grid(row=6, column=4)

button_add_task = Button(root, text="Add Task",fg="green", bg="white", command=add_task)
button_add_task.grid(row=7, column=4)

button_delete_all = Button(root, text="Delete All Tasks",fg="green", bg="white", command=delete_all)
button_delete_all.grid(row=8, column=4)

button_delete_one = Button(root, text="Delete",fg="green", bg="white", command=delete_task)
button_delete_one.grid(row=9, column=4)

button_sort_asc = Button(root, text="Sort List (ASC)",fg="green", bg="white", command=sort_asc)
button_sort_asc.grid(row=10, column=4)

button_sort_desc = Button(root, text="Sort List (DESC)",fg="green", bg="white", command=sort_desc)
button_sort_desc.grid(row=11, column=4)

button_choose_random = Button(root, text="Add Random Task",fg="green", bg="white", command=choose_random_task)
button_choose_random.grid(row=12, column=4)

button_number_of_tasks = Button(root, text="Number of Tasks",fg="green", bg="white", command=check_number_of_tasks)
button_number_of_tasks.grid(row=13, column=4)

button_exit = Button(root, text="Exit Program",fg="green", bg="white", command=exit)
button_exit.grid(row=14, column=4)

lb_tasks = Listbox(root)
lb_tasks.grid(row=15, column=4)
for item in range(len(tasks)):
    lb_tasks.insert(END, tasks[item])

root.mainloop()

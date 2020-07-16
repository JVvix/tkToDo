from tkinter import *
import random
import os
import json

location = 3

def makeNew(name):
    global location
    name2 = name
    name = exec("%s = %d" % (name, 2))
    name = Checkbutton(root, text=name2).grid(row=location, column=0)

def update_screen():
    global location
    for i in range(len(tasks)):
        if tasks[i] != "":
            location += 1
            makeNew(tasks[i])

def add_task():
    global tasks, location
    tasks.append(newTask.get())
    update_screen()

# def delete_all():
#     global tasks, location
    
#     location = 3

# def delete_task():
#     tasks = tasks[:-1]
#     update_screen()

def save():
    f = open("save_data.txt", "w")
    f.write(tasks)
    root.destroy()

# ### program starts ###

f = open("save_data.txt", "r")
text = f.read()

if len(text) == 0:
    tasks = []
else:
    tasks = text.strip('][').split(", ")
    for i in range(len(tasks)):
        tasks[i] = tasks[i].replace("'", "")
    f.close()

print(tasks)

root = Tk()
root.title("My To-Do List")
root.geometry("260x220")

lbl_title = Label(root, text="To Do List").grid(row=1, column=0)

placeholder = Label(root, text="").grid(row=2, column=0)

newTask = Entry(root)
newTask.grid(row=3, column=0)

add_button = Button(root, text="Add task", command=add_task).grid(row=3, column=5)
# delete_all_button = Button(root, text="Delete all tasks", command=delete_all).grid(row=4, column=5)
# delete_button = Button(root, text="Delete last task", command=delete_task).grid(row=5, column=5)
# exit_button = Button(root, text="Exit", command=save).grid(row=6, column=5)

root.protocol("WM_DELETE_WINDOW", save)
# root.after(2, update_screen)
root.mainloop()

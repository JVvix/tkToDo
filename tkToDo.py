from tkinter import *
import random
import os
import json

location = 5

def save_and_quit():
    f = open("save_data.txt", "w")
    f.write(str(tasks))
    f.close()
    root.destroy()

def save():
    f = open("save_data.txt", "w")
    f.write(str(tasks))
    f.close()

def add_task():
    global location
    taskName = newTask.get()
    tasks.append(taskName)
    word = Checkbutton(task_frame, text=str(taskName)).grid(row=location, column=0)
    location += 1

def add_saved_task(taskName):
    global location
    word = Checkbutton(task_frame, text=taskName).grid(row=location, column=0)
    location += 1

def delete_all():
    global tasks
    tasks = []
    task_frame.grid_forget()

### program starts ### 
root = Tk()
root.title("My To-Do List")
root.geometry("260x220")

task_frame = Frame(root)
task_frame.grid(row=4)
f = open("save_data.txt", "r")
text = f.read()

if len(text) == 0:
    tasks = []
else:
    tasks = text.strip('][').split(", ")
    for i in range(len(tasks)):
        tasks[i] = tasks[i].replace("'", "") 
    f.close()

for i in range(len(tasks)):
    add_saved_task(tasks[i])

lbl_title = Label(root, text="To Do List").grid(row=1, column=0)

placeholder = Label(root, text="").grid(row=2, column=0)

newTask = Entry(root)
newTask.grid(row=3, column=0)

add_button = Button(root, text="Add task", command=add_task).grid(row=3, column=5)
delete_all_button = Button(root, text="Delete all tasks", command=delete_all).grid(row=4, column=5)
save_button = Button(root, text="Save", command=save).grid(row=5, column=5)
save_and_quit_button = Button(root, text="Save and Exit", command=save_and_quit).grid(row=6, column=5)

root.protocol("WM_DELETE_WINDOW", save_and_quit)
root.mainloop()


from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import sqlite3

db="db.db"

root=Tk()
gavmed=Label(root, text="Gav-Med Solutions")
gavmed.pack()

def populate_list():
    db.(0, END)
    for row in db.fetch():
        db.insert(END, row)

def add_item():
    if name_text.get() ==''or parish_text.get() =='' or telephone_text.get() =='' or email_text.get() =='' or test_text.get() =='' or lab_text.get() =='' or user_text.get() =='' or id_text.get() =='' or date_text.get() =='' or time_text.get() =='':
        messagebox.showerror('Required Field', 'Please include all fields')
        return
    mylist.insert(name_text.get(), parish_text.get(), telephone_text.get(), email_text.get(), test_text.get(), lab_text.get(), user_text.get(), id_text.get(), date_text.get(), time_text.get())
    db.execute(name_text.get(), parish_text.get(), telephone_text.get(), email_text.get(), test_text.get(), lab_text.get(), user_text.get(), id_text.get(), date_text.get(), time_text.get())
    db.delete(0, END)
    db.execute(END, (name_text.get(), parish_text.get(), telephone_text.get(), email_text.get(), test_text.get(), lab_text.get(), user_text.get(), id_text.get(), date_text.get(), time_text.get()))
    clear_text()
    populate_list()
def select_item(event):
    try:
        global selected_item
        index=mylist.curselection()[0]
        selected_item= mylist.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_item[1])
        e2.delete(0, END)
        e2.insert(END, selected_item[2])
        e3.delete(0, END)
        e3.insert(END, selected_item[3])
        e4.delete(0, END)
        e4.insert(END, selected_item[4])
        e5.delete(0, END)
        e5.insert(END, selected_item[5])
        e6.delete(0, END)
        e6.insert(END, selected_item[6])
        e7.delete(0, END)
        e7.insert(END, selected_item[7])
        e8.delete(0, END)
        e8.insert(END, selected_item[8])
        e9.delete(0, END)
        e9.insert(END, selected_item[9])
        e10.delete(0, END)
        e10.insert(END, selected_item[10])
    except IndexError:
        pass
def remove_item():
    db.delete(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item,  name_text.get(), parish_text.get(), telephone_text.get(), email_text.get(), test_text.get(), lab_text.get(), user_text.get(), id_text.get(), date_text.get(), time_text.get())
    populate_list()

def clear_text():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)


def getExcel():
    global df
    filepath= filedialog.askopenfilename()
    container= tk.Listbox(root, selectmode="multiple")
    canvas= tk.Canvas(container)
    canvas.create_window((0,0), anchor="nw")
    canvas.pack()


myButton=Button(root, text="Medical Laboratory", bg="red", fg="white", command= getExcel)
myButton.pack()

root['bg']='lightblue'
w=Canvas(root, bg="white", height=250, width=300)
im=PhotoImage(file="C:\\Users\\diana\\desktop\\gavmed.png")
w=Label(root, image=im)
w.place(x=0, y=0, relwidth=1, relheight=1)
w.pack()
root.iconphoto(False, im)
menubar=Menu(root)
File=Menu(menubar)
File.add_command(label="Doctor", command= getExcel)
File.add_separator()
File.add_command(label="Patient", command= getExcel)
menubar.add_cascade(label="File",menu=File)
Edit=Menu(root)
Edit.add_command(label="Cut")
Edit.add_separator()
Edit.add_command(label="Paste")
menubar.add_cascade(label="Edit", menu=Edit)
View=Menu(root)
View.add_command(label="Online")
View.add_separator()
View.add_command(label="Offline")
menubar.add_cascade(label="View", menu=View)
root.config(menu=menubar)
mylist=Listbox(root, height=15, width=800, border=0)
mylist.place(x=0, y=400)
mylist.bind('<<ListboxSelect>>', select_item)
root.geometry("500x200+100+100")
name_text=StringVar()
l1=Label(root, text="Name", bg="blue", fg="white").place(x=75, y=80)
parish_text=StringVar()
l2=Label(root, text="Parish", bg="blue", fg="white").place(x=75, y=120)
telephone_text=StringVar()
l3=Label(root, text="Telephone", bg="blue", fg="white").place(x=75, y=160)
email_text=StringVar()
l4=Label(root, text="Email", bg="blue", fg="white").place(x=75, y=200)
test_text=StringVar()
l5=Label(root, text="Test", bg="blue", fg="white").place(x=75, y=240)
lab_text=StringVar()
l6=Label(root, text="Lab", bg="blue", fg="white").place(x=75, y=280)
e1=Entry(root, textvariable=name_text, bd=10).place(x=150, y=80)
e2=Entry(root, textvariable=parish_text, bd=10).place(x=150, y=120)
e3=Entry(root, textvariable=telephone_text, bd=10).place(x=150, y=160)
e4=Entry(root, textvariable=email_text, bd=10).place(x=150, y=200)
e5=Entry(root, textvariable=test_text, bd=10).place(x=150, y=240)
e6=Entry(root, textvariable=lab_text, bd=10).place(x=150, y=280)
user_text=StringVar()
l7=Label(root, text="USER", bg="blue", fg="white").place(x=1100,y=80)
id_text=StringVar()
l8=Label(root, text="ID", bg="blue", fg="white").place(x=1100, y=120)
date_text=StringVar()
l9=Label(root, text="DATE", bg="blue", fg="white").place(x=1100, y=160)
time_text=StringVar()
l10=Label(root, text="TIME", bg="blue", fg="white").place(x=1100, y=200)
e7=Entry(root, textvariable=user_text, bd=10).place(x=1150, y=80)
e8=Entry(root, textvariable=id_text, bd=10).place(x=1150, y=120)
e9=Entry(root, textvariable=date_text, bd=10).place(x=1150, y=160)
e10=Entry(root, textvariable=time_text, bd=10).place(x=1150, y=200)
add_b=Button(root, text="ADD", width=12, bg="red", fg="white", command=add_item).place(x=1150, y=240)
remove_b=Button(root, text="REMOVE", width=12, bg="red", fg="white", command=remove_item).place(x=1150, y=280)
update_b=Button(root, text="UPDATE", width=12, bg="red", fg="white", command=update_item).place(x=1150, y=320)
clear_b=Button(root, text="CLEAR", width=12, bg="red", fg="white", command=clear_text).place(x=1150, y=360)
root.title("Gavin Omar Dixon")
root.config(background="white")
populate_list()
root.mainloop()

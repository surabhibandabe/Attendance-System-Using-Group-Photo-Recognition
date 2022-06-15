from tkinter import ttk
import tkinter as tk
#import mysql.connector
import pymysql

#import main.py

# Creating tkinter window
def show(class_id) :
    window = tk.Tk()
    window.resizable(width = 50, height = 50)

    con=pymysql.connect(host='localhost',user='root',password='',database='attendance')
    cur=con.cursor()
    cur.execute("select * from student where class_id = %s ",(class_id))


    # Using treeview widget
    treev = ttk.Treeview(window, selectmode ='browse')

    # Calling pack method w.r.to treeview
    treev.pack(side ='top')

    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(window,
                            orient ="vertical",
                            command = treev.yview)

    # Calling pack method w.r.to vertical
    # scrollbar
    verscrlbar.pack(side ='right', fill ='x')

    # Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)

    # Defining number of columns
    treev["columns"] = ("1", "2", "3")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to the
    # respective columns
    treev.column("1", width = 400, anchor ='c')
    treev.column("2", width = 400, anchor ='c')
    treev.column("3", width = 400, anchor ='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text ="Sr.No")
    treev.heading("2", text ="ID")
    treev.heading("3", text ="Name")

    # Inserting the items and their features to the
    # columns built
    i=0
    for row in cur:
        treev.insert('',i,text=row[0],values=(i+1,row[0],row[1]))
        i=i+1

    treev.pack()


    # Calling mainloop

    window.mainloop()

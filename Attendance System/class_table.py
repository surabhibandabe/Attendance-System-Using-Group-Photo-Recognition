# Python program to illustrate the usage of
# treeview scrollbars using tkinter


from csv import excel
from tkinter import messagebox, ttk
from tkinter import *
import tkinter as tk
#import mysql.connector
import pymysql


#import main.py


window = Tk()

window.title('Mark Attendance')
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

frame=Frame(window, width=350, height=350, bg='white')
frame.place(x=280,y=70)


con=pymysql.connect(host='localhost',user='root',password='',database='attendance')
cur=con.cursor()
cur.execute("select * from class")


# Using treeview widget
treev = ttk.Treeview(window, selectmode ='browse')


# Calling pack method w.r.to treeview
# treev.pack(side ='top')
# treev.pack(side ='right')

# Constructing vertical scrollbar
# with treeview
verscrlbar =ttk.Scrollbar(frame,
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
treev.column("1", width = 200, anchor ='c')
treev.column("2", width = 200, anchor ='c')
treev.column("3", width = 200, anchor ='c')

# Assigning the heading names to the
# respective columns
treev.heading("1", text ="Sr.No")
treev.heading("2", text ="Class")
treev.heading("3", text ="Total Students")

# Inserting the items and their features to the
# columns built
id=''

i=0
cur1=con.cursor()
for row in cur:
    total_rows=  cur1.execute("select * from student where class_id = %s ",(row[0]))
    treev.insert('',i,text=row[0],values=(i+1,row[1],total_rows))
    i=i+1

treev.pack()
value=""
present_name=[]
def takeAttendance():
   # Get selected item to Edit
   selected_item = treev.focus()
   temp = treev.item(selected_item, 'values')
   value = temp[1]
   id=temp[0]
   
   #print(value)
   #window.destroy()
   from attendance import  find_target_face,render_image
#    try:
#        lis = find_target_face(value)
#    except Exception as es:
#        messagebox.showerror("Error",f'Error Due to: {str(es)}')
#    try:    
#        render_image()
#    except Exception as es:
#        messagebox.showerror("Error",f'Error Due to: {str(es)}')

       
   lis = find_target_face(value)
   render_image()
   for image in lis:
       cur.execute("select * from student where photo = %s ",(image))
       row=cur.fetchone()
       present_name.append(row[1])
   # for name in present_name:
   #              print(name)

   window.destroy()
   from excel import create_csv
   
   create_csv(id,present_name)
   
   
   
def viewDetails():
   # Get selected item to Edit
   selected_item = treev.focus()
   temp = treev.item(selected_item, 'values')
   value=temp[0]
   print(value)
   from view_details import show
   show(value)
  # treev.item(selected_item, text="", values=("foo", "bar"))
   
att_btn = Button(window,width=39,pady=7, bg='#57a1f8',fg='white',border=0, cursor='hand2', text="Take Attendance", command=takeAttendance).place(x=300,y=304)


view_btn = Button(window,width=39,pady=7, text="View Details", bg='#57a1f8',fg='white',border=0, cursor='hand2',command=viewDetails).place(x=300,y=374)

# Calling mainloop


window.mainloop()

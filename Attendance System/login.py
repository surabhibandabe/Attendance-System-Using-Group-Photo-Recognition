from cProfile import label
from tkinter import *
from tkinter import messagebox
from tkinter import font
from turtle import width
from unicodedata import name
#from django.forms import PasswordInput
import pymysql
from numpy import insert
from numpy.lib.function_base import place

root=Tk()

root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def signin():
    username=User.get()
    password=Password.get()
    
    if username=='Username' and password=='Password':
        messagebox.showerror("invalid",'All field are required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',database='attendance')
            cur=con.cursor()
            cur.execute("select * from teachers where Username=%s and Password=%s",(User.get(),Password.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("invalid",'Invalid Username and Password')
            else:
                messagebox.showinfo("Success","Logged in")
                root.destroy()
                con.close()
                import class_table
        
        except Exception as es:
            messagebox.showerror("Error",f'Error Due to: {str(es)}')
            

# img = PhotoImage(file='bg.png')
# Label(root,image=img,bg='white', height=925, width=).place(x=50,y=50)

frame=Frame(root, width=350, height=350, bg='white')
frame.place(x=280,y=70)

heading=Label(frame, text='sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#_________
def on_enter(e):
    User.delete(0,'end')

def on_leave(e):
    name=User.get()
    if name=='':
        User.insert(0,'Username')

#user details
User=Entry(frame,width=25, fg='black',border=0, bg="white",font=('Mocrosoft YaHei UI Light',11))
User.place(x=30,y=80)
User.insert(0,'Username')
User.bind('<FocusIn>', on_enter)
User.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25,y=107)

def on_enter(e):
    Password.delete(0,'end')
    Password.config(show='*')

def on_leave(e):
    name=Password.get()
    if name=='':
        Password.insert(0,'Password')
Password=Entry(frame,width=25, fg='black',border=0, bg="white", font=('Mocrosoft YaHei UI Light',11))
Password.place(x=30,y=150)
Password.insert(0,'Password')
Password.bind('<FocusIn>', on_enter)
Password.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0, cursor='hand2',command=signin).place(x=35,y=204)

                                                                
root.mainloop()
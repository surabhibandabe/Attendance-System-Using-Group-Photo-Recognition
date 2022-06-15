from tkinter import *
from tkinter import messagebox
from tkinter import font
import tkinter as tk
from tkinter import filedialog
from turtle import width
import datetime
from datetime import datetime
import csv
from unicodedata import name
from wsgiref import headers
from cv2 import CAP_OPENCV_MJPEG
import pandas as pd
import os
#from django.forms import PasswordInput
import pymysql
from numpy import NaN, insert
from numpy.lib.function_base import place



def openWindow():
    def save_file():
    
        path=folder_name
        file=filename.get()
        completeName = os.path.join(path, file +'.csv')
        print(completeName)
        f=open('attendance.csv',"r")
        df = pd.read_csv(f)
        file2 = open(completeName, "w")
        df.to_csv(file2, index=False)
        f.close()
        file2.close()
        messagebox.showinfo("Success","{file}CSV file craeted at location:{path}")
        window.destroy()
        
    def openlocation():
        global folder_name
        folder_name=filedialog.askdirectory()
        filename2.insert(0,folder_name)
        print(folder_name)
   
    window = Tk()
    window.title('Save File')
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)
    frame=Frame(window, width=350, height=350, bg='white')
    frame.place(x=280,y=70)
    filename=Entry(window,width=25, fg='black',border=0, bg="white",font=('Mocrosoft YaHei UI Light',11))
    filename.place(x=305,y=80)
    filename.insert(0,'Enter File Name')

    Frame(window, width=250, height=2, bg='black').place(x=305,y=100)

    filename2=Entry(window,width=30, fg='black',border=0, bg="white",font=('Mocrosoft YaHei UI Light',11))
    filename2.place(x=305,y=150)

    Button(window,width=39,pady=7,text='choose path',bg='#57a1f8',fg='white',border=0, cursor='hand2', command=openlocation).place(x=305,y=200)

    Button(window,width=39,pady=7,text='Create Csv',bg='#57a1f8',fg='white',border=0, cursor='hand2', command=save_file).place(x=305,y=300)
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
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
con=pymysql.connect(host='localhost',user='root',password='',database='attendance')
cur=con.cursor()

List=[]
ID=''



#print("excel")




def create_csv(class_id,present_name):
    cur.execute("select id,name from student where class_id = %s ",(class_id))
    
    headers=['Roll No','Name','status']
    
    
    with open('attendance.csv','w') as csvfile:
        writer=csv.writer(csvfile)
       
        writer.writerow(headers)
        
        writer.writerows(cur)
        
    df = pd.read_csv('attendance.csv') 
   
    for index, row in df.iterrows():
        for x in present_name:
            if  row['Name']==x:
                df.loc[index,['status']]='P'
                
    for index, row in df.iterrows():
        if row['status']!="P":
            df.loc[index, ['status']]='A'        
            
    print(df) 
    df.to_csv('attendance.csv', index=False)
    now = datetime.now()
    filename = now.strftime("%H:%M:%S")
    #os.rename('attendance.csv',filename+'.csv')

     
    
        
        
    
            
            # for x in present_name:
            #     if p['Name']==str(x):
            #         p['status']='P'
            #     else:
            #         p['status']='A'
        
#create_csv('1','rohit sharma')
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
    



def openlocation():
    global folder_name
    folder_name=filedialog.askdirectory()
    filename2.insert(0,folder_name)
    
    print(folder_name)
 

 
from save_file import openWindow
openWindow()








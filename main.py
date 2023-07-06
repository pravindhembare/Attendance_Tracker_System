from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_detector import Face_Detector
from attendance import Attendance
from tracking import Tracking
import os

class Attendance_Tracker:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1355x700+0+0") 
        self.root.title("attendance tracker")

        #Heading Image
        img=Image.open(r"D:\Programs\attendance_tracker\images\a.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img1=Image.open(r"D:\Programs\attendance_tracker\images\download (5).jpg")
        img1=img1.resize((855,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=855,height=130)

        #background image
        img2=Image.open(r"D:\Programs\attendance_tracker\images\images (8).jpg")
        img2=img2.resize((1355,570),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_img=Label(self.root,image=self.photoimg2)
        bg_img.place(x=0,y=130,width=1355,height=570)
        
        #Heading
        title_lbl=Label(bg_img,text="ATTENDANCE  TRACKER  SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1355,height=45)

        #Time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font= ('times new roman',14,'bold'),background='white',foreground='black')    
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #Date
        def current_date():
            now=datetime.now()
            cdate=now.date()
            lbl1.config(text=cdate)
        lbl1 = Label(title_lbl, font= ('times new roman',14,'bold'),background='white',foreground='black')    
        lbl1.place(x=1240,y=0,width=110,height=50)
        current_date()

        #Student Button
        img3=Image.open(r"D:\Programs\attendance_tracker\images\images (15).jpg")
        img3=img3.resize((200,150),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(bg_img,image=self.photoimg3,command=self.student_details,cursor="hand2")
        b1.place(x=70,y=200,width=200,height=150)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=70,y=350,width=200,height=40)

         #Train Face Button
        img5=Image.open(r"D:\Programs\attendance_tracker\images\images (13).jpg")
        img5=img5.resize((200,150),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,command=self.train_data,cursor="hand2")
        b2.place(x=320,y=200,width=200,height=150)

        b2_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b2_1.place(x=320,y=350,width=200,height=40)

         #Detect Face Button
        img6=Image.open(r"D:\Programs\attendance_tracker\images\b.webp")
        img6=img6.resize((200,150),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,command=self.face_detect,cursor="hand2")
        b3.place(x=570,y=200,width=200,height=150)

        b3_1=Button(bg_img,text="Take Attendance",command=self.face_detect,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b3_1.place(x=570,y=350,width=200,height=40)

        #Attendance Face Button
        att=Image.open(r"D:\Programs\attendance_tracker\images\attendace.jpg")
        att=att.resize((200,150),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(att)

        b4=Button(bg_img,image=self.photoimg7,command=self.attendance_data,cursor="hand2")
        b4.place(x=820,y=200,width=200,height=150)

        b4_1=Button(bg_img,text="Manage Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b4_1.place(x=820,y=350,width=200,height=40)

         #Tracing Button
        Email=Image.open(r"D:\Programs\attendance_tracker\images\a12.jpg")
        Email=Email.resize((200,150),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(Email)

        b5=Button(bg_img,image=self.photoimg8,command=self.tracing_data,cursor="hand2")
        b5.place(x=1070,y=200,width=200,height=150)

        b5_1=Button(bg_img,text="Trace Attendance",command=self.tracing_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b5_1.place(x=1070,y=350,width=200,height=40)

        #Exit
        b6=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="red")
        b6.place(x=570,y=450,width=200,height=40)

    def open_img(self):
        os.startfile("data")

    #Function
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_detect(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Detector(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def tracing_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Tracking(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Attendance_Tracker","Are you sure to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return 

if __name__ == "__main__":        
    root=Tk()
    obj=Attendance_Tracker(root)
    root.mainloop()
        
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
import os
import csv
from tkinter import filedialog
from tkcalendar import DateEntry
import re


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1355x700+0+0") 
        self.root.title("attendance tracker")

        cal=DateEntry(self.root,selectmode='day',year=2013,month=6,day=16)

        #variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        self.var_atten_date1=StringVar()
        self.var_search_type=StringVar()
        self.var_search_sid=StringVar()
        
        self.var_search_dep=StringVar()
        self.var_search_sem=StringVar()
        self.var_search_date=StringVar()
        self.var_search_id=StringVar()

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
        title_lbl=Label(bg_img,text="MANAGE  STUDENT  ATTENDANCE",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1355,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1345,height=500)       

        back_btn=Button(title_lbl,text="Back",command=self.return_main,width=10,font=("times new roman",12,"bold"),bg="black",fg="White")
        back_btn.place(x=0,y=0,width=110,height=50)

        # Left Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=710,height=480)

        # img_left=Image.open(r"D:\Programs\attendance_tracker\images\attendace.jpg")
        # img_left=img_left.resize((700,100),Image.Resampling.LANCZOS)
        # self.photoimg3=ImageTk.PhotoImage(img_left)

        # f_lbl2=Label(Left_frame,image=self.photoimg3)
        # f_lbl2.place(x=0,y=0,width=705,height=90)

        left_inside_frame=Frame(Left_frame,bd=0,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=0,width=705,height=455)

        #Search frame        
        Search_frame=LabelFrame(left_inside_frame,bd=0,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),bg="white")
        Search_frame.place(x=0,y=0,width=700,height=90)

        space=Label(Search_frame,text="",font=("times new roman",12,"bold"),bg="white",fg="white")
        space.grid(row=0,column=0,padx=100,pady=2,sticky=W)

        Search_Lable=Label(Search_frame,text="Search By :",font=("times new roman",12,"bold"),bg="red",fg="white")
        Search_Lable.grid(row=0,column=1,padx=10,pady=2,sticky=W)

        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_search_type,font=("times new roman",12,"bold"),state="readonly",width=10)
        search_combo["values"]=("Select ","Student Id","Roll No","Name","Phone No","Email")
        search_combo.current(0)
        search_combo.grid(row=0,column=2,padx=2,pady=2,sticky=W)

        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search_sid,width=13,font=("times new roamn",12,"bold"))
        search_entry.grid(row=0,column=3,padx=5,pady=20,sticky=W)

        search_btn=Button(left_inside_frame,text="Search",command=self.search_data,width=10,font=("times new roman",12,"bold"),bg="black",fg="White")
        search_btn.place(x=250,y=85,width=250,height=25)

        

        #Lables and entries Frame
        lbl_frame=LabelFrame(left_inside_frame,bd=0,relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"),bg="white")
        lbl_frame.place(x=0,y=125,width=700,height=220)
         #Attendance id
        attendanceId_Lable=Label(lbl_frame,text="Student ID :",font=("times new roman",12,"bold"),bg="white")
        attendanceId_Lable.grid(row=0,column=0,padx=10,pady=20,sticky=W)

        attendanceId_entry=Label(lbl_frame,width=20,textvariable=self.var_atten_id,font=("times new roamn",12,"bold"),bg="white")
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=20,sticky=W)

         #Roll
        roll_Lable=Label(lbl_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        roll_Lable.grid(row=0,column=2,padx=10,pady=20,sticky=W)

        atten_roll=Label(lbl_frame,width=20,textvariable=self.var_atten_roll,font=("times new roamn",12,"bold"),bg="white")
        atten_roll.grid(row=0,column=3,padx=10,pady=20,sticky=W)

         #Name
        name_Lable=Label(lbl_frame,text="Name :",font=("times new roman",12,"bold"),bg="white")
        name_Lable.grid(row=1,column=0,padx=10,pady=0,sticky=W)

        atten_name=Label(lbl_frame,width=20,textvariable=self.var_atten_name,font=("times new roamn",12,"bold"),bg="white")
        atten_name.grid(row=1,column=1,padx=10,pady=0,sticky=W)

        #Department
        dep_Lable=Label(lbl_frame,text="Department :",font=("times new roman",12,"bold"),bg="white")
        dep_Lable.grid(row=1,column=2,padx=10,pady=0,sticky=W)

        atten_dep=Label(lbl_frame,width=20,textvariable=self.var_atten_dep,font=("times new roamn",12,"bold"),bg="white")
        atten_dep.grid(row=1,column=3,padx=10,pady=0,sticky=W)

         #Time
        time_Lable=Label(lbl_frame,text="Time :",font=("times new roman",12,"bold"),bg="white")
        time_Lable.grid(row=2,column=0,padx=10,pady=20,sticky=W)

        atten_time=Label(lbl_frame,width=20,textvariable=self.var_atten_time,font=("times new roamn",12,"bold"),bg="white")
        atten_time.grid(row=2,column=1,padx=0,pady=20,sticky=W)

         #Date
        date_Lable=Label(lbl_frame,text="Date :",font=("times new roman",12,"bold"),bg="white")
        date_Lable.grid(row=2,column=2,padx=10,pady=20,sticky=W)

        atten_date=Label(lbl_frame,width=20,textvariable=self.var_atten_date,font=("times new roamn",12,"bold"),bg="white")
        atten_date.grid(row=2,column=3,padx=0,pady=20,sticky=W)

       #Calender
        date_Lable1=Label(lbl_frame,text="Date :",font=("times new roman",12,"bold"),bg="white")
        date_Lable1.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        cal=DateEntry(lbl_frame,selectmode='day',date_pattern="dd/mm/y",textvariable=self.var_atten_date1)
        cal.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        # sel.trace('w',self.my_upd)

        #attendance
        attendanceLable=Label(lbl_frame,text="Attendance Status :",bg="white",font="comicsansns 11 bold")
        attendanceLable.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(lbl_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        self.atten_status.current(0)

        # Database buttons frame
        btn_frame=Frame(left_inside_frame,bd=0,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=355,width=700,height=30)

        import_btn=Button(btn_frame,text="Add Attendance",command=self.add_attendance,width=19,font=("times new roman",12,"bold"),bg="black",fg="White")
        import_btn.grid(row=0,column=0)

        add_btn=Button(btn_frame,text="Update Attendance",command=self.update_attendance,width=18,font=("times new roman",12,"bold"),bg="black",fg="White")
        add_btn.grid(row=0,column=1)       

        update_btn=Button(btn_frame,text="Delete Attendance",command=self.delete_attendance,width=18,font=("times new roman",12,"bold"),bg="black",fg="White")
        update_btn.grid(row=0,column=2)

        delete_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="black",fg="White")
        delete_btn.grid(row=0,column=3)


        # csv buttons frame
        btn_frame=Frame(left_inside_frame,bd=0,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=400,width=700,height=30)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=38,font=("times new roman",12,"bold"),bg="black",fg="White")
        import_btn.grid(row=0,column=0)        

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=38,font=("times new roman",12,"bold"),bg="black",fg="White")
        export_btn.grid(row=0,column=1)


        # Right Frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),bg="white")
        Right_frame.place(x=730,y=10,width=600,height=480)

        # img_right=Image.open(r"D:\Programs\attendance_tracker\images\ab.jpg")
        # img_right=img_right.resize((500,100),Image.Resampling.LANCZOS)
        # self.photoimg4=ImageTk.PhotoImage(img_right)

        # r_lbl3=Label(Right_frame,image=self.photoimg4)
        # r_lbl3.place(x=0,y=0,width=597,height=90)

        # Right Search frame        
        Search_frame1=LabelFrame(Right_frame,bd=0,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),bg="white")
        Search_frame1.place(x=0,y=0,width=597,height=90)
        
        year=Label(Search_frame1,text="",font=("times new roman",12,"bold"),bg="white",fg="black")
        year.grid(row=0,column=0,padx=0,pady=0,sticky=W)

        year_combo=Label(Search_frame1,text="",font=("times new roman",12,"bold"),bg="white",fg="black",width=5)
        # year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")
        # year_combo.current(0)
        year_combo.grid(row=1,column=0,padx=1,pady=1,sticky=W)

        course=Label(Search_frame1,text="Department",font=("times new roman",12,"bold"),bg="white",fg="black")
        course.grid(row=0,column=1,padx=2,pady=1,sticky=W)

        dep_combo=ttk.Combobox(Search_frame1,textvariable=self.var_search_dep,font=("times new roman",12,"bold"),state="read only",width=16)
        dep_combo["values"]=("Select Department","MCA","MBA")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=1)

        sem=Label(Search_frame1,text="Semester",font=("times new roman",12,"bold"),bg="white",fg="black")
        sem.grid(row=0,column=2,padx=2,pady=1,sticky=W)

        sem_combo=ttk.Combobox(Search_frame1,textvariable=self.var_search_sem,font=("times new roman",12,"bold"),state="readonly",width=14)
        sem_combo["values"]=("Select Semester","Semester-1","Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=2,padx=2,pady=1,sticky=W)

        date=Label(Search_frame1,text="Date",font=("times new roman",12,"bold"),bg="white",fg="black")
        date.grid(row=0,column=3,padx=2,pady=1,sticky=W)        

        date_entry=DateEntry(Search_frame1,selectmode='day',date_pattern="dd/mm/y",textvariable=self.var_search_date,width=12)
        date_entry.grid(row=1,column=3,padx=2,pady=1,sticky=W)

        stuid=Label(Search_frame1,text="Std Id",font=("times new roman",12,"bold"),bg="white",fg="black")
        stuid.grid(row=0,column=4,padx=2,pady=1,sticky=W)        

        stuid_entry=ttk.Entry(Search_frame1,textvariable=self.var_search_id,width=12,font=("times new roamn",12,"bold"))
        stuid_entry.grid(row=1,column=4,padx=2,pady=1,sticky=W)

        # search_btn=Button(Search_frame1,text="Search",command=self.search_data,width=10,font=("times new roman",12,"bold"),bg="black",fg="White")
        # search_btn.grid(row=0,column=5,padx=0)
        search_btn1=Button(Right_frame,text="Search",command=self.search_data1,width=10,font=("times new roman",12,"bold"),bg="black",fg="White")
        search_btn1.place(x=180,y=90,width=250,height=25)

        #Scroling Frame
        table_frame=LabelFrame(Right_frame,bd=0,relief=RIDGE,bg="white")
        table_frame.place(x=2,y=135,width=587,height=320)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReport_table=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReport_table.xview)
        scroll_y.config(command=self.AttendanceReport_table.yview)

        self.AttendanceReport_table.heading("id",text="Student ID")
        self.AttendanceReport_table.heading("roll",text="Roll no.")
        self.AttendanceReport_table.heading("name",text="Name")
        self.AttendanceReport_table.heading("department",text="Department")
        self.AttendanceReport_table.heading("time",text="Time")
        self.AttendanceReport_table.heading("date",text="Date")
        self.AttendanceReport_table.heading("attendance",text="Attendance Status")
        self.AttendanceReport_table["show"]="headings"

        self.AttendanceReport_table.column("id",width=100)
        self.AttendanceReport_table.column("roll",width=100)
        self.AttendanceReport_table.column("name",width=100)
        self.AttendanceReport_table.column("department",width=100)        
        self.AttendanceReport_table.column("time",width=100)
        self.AttendanceReport_table.column("date",width=100)
        self.AttendanceReport_table.column("attendance",width=100)

        self.AttendanceReport_table.pack(fill=BOTH,expand=1)
        self.AttendanceReport_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # def my_upd(*args):
        # atten_date.config(Text=sel.get())


     # Data Search    
    def search_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
        my_cursor1=conn.cursor()  

        if self.var_search_type.get()=="Select ":
             messagebox.showerror("Error","All Please select any Search Type",parent=self.root)
        elif self.var_search_sid.get()=="":
             messagebox.showerror("Error","Please enter the value of search",parent=self.root)
        elif self.var_search_type.get()=="Student Id":
             query="select stud_id,roll,name,dep from student where stud_id=%s"
        elif self.var_search_type.get()=="Roll No":
             query="select stud_id,roll,name,dep from student where roll=%s"
        elif self.var_search_type.get()=="Phone No":
             query="select stud_id,roll,name,dep from student where phone=%s"
        elif self.var_search_type.get()=="Email":
             query="select stud_id,roll,name,dep from student where stud_email=%s"
        elif self.var_search_type.get()=="Name":
             query="select stud_id,roll,name,dep from student where name=%s"             
        else:
             messagebox.showerror("Error","Something went wrong",parent=self.root)
        try :
            value=(self.var_search_sid.get(),)
            my_cursor1.execute(query,value)                   
            data= my_cursor1.fetchall()
            
            if len(data)!=0:
                self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())
                for i in data:
                    self.AttendanceReport_table.insert("",END,values=i)
            else:
                messagebox.showerror("Error","Record not found",parent=self.root)
            conn.commit()
            conn.close() 
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)            


    # Data Showing
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
        my_cursor1=conn.cursor()
        my_cursor1.execute("select student.stud_id,student.roll,student.name,student.dep,attendance.time,attendance.date,attendance.status from attendancetracker.student inner join attendancetracker.attendance on attendance.stdid=student.stud_id")
        data= my_cursor1.fetchall()
        
        if len(data)!=0:
            self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())
            mydata.clear()
            for i in data:
                self.AttendanceReport_table.insert("",END,values=i)                
                mydata.append(i)
            conn.commit()
        conn.close()   

    #fetch data
    def fetchData(self,rows):
        self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())
        for i in rows:
            self.AttendanceReport_table.insert("",END,values=i)

    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Export CSV            
    def exportCsv(self):
        try:
            # if len(mydata)<1:
            #     messagebox.showerror("No Data","No data found to export",parent=self.root)
            #     return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Your data exported to "+os.path.basename(fln)+" successfully.",parent=self.root)

        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    
    # Cursor
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReport_table.focus()
        content=self.AttendanceReport_table.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    # Reset
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")
        self.var_search_dep.set("Select Department")
        self.var_search_sem.set("Select Semester")
        self.var_search_type.set("Select ")
        self.var_search_id.set("")
        self.var_search_sid.set("")
        self.fetch_data()

    # Add Attendance
    def add_attendance(self):
        if self.var_atten_id.get()=="" or self.var_atten_roll.get()=="" or self.var_atten_name.get()=="" or self.var_atten_dep.get()=="":
             messagebox.showerror("Error","Please firstly select student info..",parent=self.root)
        elif  self.var_atten_attendance.get()=="Status":
             messagebox.showerror("Error","Please select the attendance status",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
            my_cursor=conn.cursor()

            query="select date from attendance where stdid=%s"
            value=self.var_atten_id.get() 
            value1=(value,)     
            my_cursor.execute(query,value1)
            date=my_cursor.fetchall()       
            now=datetime.now()                
            dtString=now.strftime("%H:%M:%S") 
            count=0 
            date0=self.var_atten_date1.get()       
            for row in date:
                if row==(date0,):
                    count+=1
            if count==0: 
                sid1=self.var_atten_id.get()
                date1=self.var_atten_date1.get()
                status1=self.var_atten_attendance.get()        

                my_cursor.execute("insert into attendance (stdid,time,date,status) values(%s,%s,%s,%s)",(sid1,dtString,date1,status1))        
                with open("std_att.csv","r+",newline="\n") as f:
                    myDataList=f.readlines()
                    name_list=[]
                    for line in myDataList:
                        entry=line.split((","))
                        name_list.append(entry[0])
                    f.writelines(f"\n{self.var_atten_id.get()},{self.var_atten_roll.get()},{self.var_atten_name.get()},{self.var_atten_dep.get()},{dtString},{self.var_atten_date1.get()},{self.var_atten_attendance.get()}")                                                                    
                messagebox.showinfo("success","Student attendance has been added successfully",parent=self.root)
                self.fetch_data()
            else:
                messagebox.showerror("Alredy exist","This date attendance is already taken, You can update attendance status",parent=self.root)

            conn.commit() 
    
     # Update Attendance
    def update_attendance(self):
        if self.var_atten_id.get()=="" or self.var_atten_roll.get()=="" or self.var_atten_name.get()=="" or self.var_atten_dep.get()=="" or self.var_atten_time.get()=="" or self.var_atten_date.get()=="":
             messagebox.showerror("Error","Please firstly select student info..",parent=self.root)
        elif  self.var_atten_attendance.get()=="Status":
             messagebox.showerror("Error","Please select the attendance status",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
            my_cursor=conn.cursor()

            query="select date from attendance where stdid=%s and date=%s"
            value0=self.var_atten_id.get()
            value=self.var_atten_date.get() 
            value1=(value0,value)     
            my_cursor.execute(query,value1)
            date=my_cursor.fetchone()           
            count=0                  
            for row in date:            
                 count+=1
            if count==1: 
                status1=self.var_atten_attendance.get()        

                try :
                    Update=messagebox.askyesno("Update","You can update only attendance status",parent=self.root)
                    if Update>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
                        my_cursor2=conn.cursor()                       
                        my_cursor2.execute("update attendance set status=%s where stdid=%s and date=%s",(self.var_atten_attendance.get(),self.var_atten_id.get(),self.var_atten_date.get()))               
                                                                                                                                                                        
                    else:
                        if not Update:
                            return 
                    messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                    conn.commit()
                    self.search_data1()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)               
            #     with open("std_att.csv","r+",newline="\n") as f:
            #         myDataList=f.readlines()
            #         name_list=[]
            #         for line in myDataList:
            #             entry=line.split((","))
            #             name_list.append(entry[0])
            #         f.writelines(f"\n{self.var_atten_id.get()},{self.var_atten_roll.get()},{self.var_atten_name.get()},{self.var_atten_dep.get()},{dtString},{self.var_atten_date1.get()},{self.var_atten_attendance.get()}")                                                                    
            
    # Delete Attendace
    def delete_attendance(self):
        if self.var_atten_id.get()=="" or self.var_atten_roll.get()=="" or self.var_atten_name.get()=="" or self.var_atten_dep.get()=="" or self.var_atten_time.get()=="" or self.var_atten_date.get()=="":
             messagebox.showerror("Error","Please firstly select student info..",parent=self.root)        
        else:
            try :    
                    delete=messagebox.askyesno("Delete Attendance","Do you want to delete this student Attendance",parent=self.root)
                    if delete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
                        my_cursor2=conn.cursor() 
                        sql="delete from attendance where stdid=%s and date=%s"
                        val=(self.var_atten_id.get(),self.var_atten_date.get())
                        my_cursor2.execute(sql,val)
                    else:
                         if not delete:
                              return
                    conn.commit()                
                    self.search_data1()
                    conn.close()
                    messagebox.showinfo("Delete","Successfully delete student attendance")
            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   

     # Right Frame Data Search    
    def search_data1(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
        my_cursor1=conn.cursor()  

        new_id=self.var_search_id.get()
        pattern1=  r'^\d{1,6}$'
        match2=re.match(pattern1,new_id)        
       
        if self.var_search_dep.get()=="Select Department" and self.var_search_sem.get()=="Select Semester" and self.var_search_id.get()=="":
             query="select student.stud_id,student.roll,student.name,student.dep,attendance.time,attendance.date,attendance.status from attendancetracker.student inner join attendancetracker.attendance on attendance.stdid=student.stud_id where attendance.date=%s"
             value=(self.var_search_date.get(),)
        elif self.var_search_dep.get()!="Select Department" and self.var_search_sem.get()!="Select Semester" and self.var_search_id.get()!="":
             query="select student.stud_id,student.roll,student.name,student.dep,attendance.time,attendance.date,attendance.status from attendancetracker.student inner join attendancetracker.attendance on attendance.stdid=student.stud_id where attendance.date=%s and student.dep=%s and student.sem=%s and attendance.stdid=%s "
             value=(self.var_search_date.get(),self.var_search_dep.get(),self.var_search_sem.get(),self.var_search_id.get())
             if bool(match2)==FALSE:
                messagebox.showerror("Error","Student ID must be in number format",parent=self.root)
        elif self.var_search_dep.get()!="Select Department" and self.var_search_sem.get()=="Select Semester" and self.var_search_id.get()=="":
             query="select student.stud_id,student.roll,student.name,student.dep,attendance.time,attendance.date,attendance.status from attendancetracker.student inner join attendancetracker.attendance on attendance.stdid=student.stud_id where attendance.date=%s and student.dep=%s"
             value=(self.var_search_date.get(),self.var_search_dep.get())
        elif self.var_search_dep.get()=="Select Department" and self.var_search_sem.get()!="Select Semester" and self.var_search_id.get()=="":
             query="select student.stud_id,student.roll,student.name,student.dep,attendance.time,attendance.date,attendance.status from attendancetracker.student inner join attendancetracker.attendance on attendance.stdid=student.stud_id where attendance.date=%s and student.sem=%s"
             value=(self.var_search_date.get(),self.var_search_sem.get())
        elif self.var_search_dep.get()=="Select Department" and self.var_search_sem.get()=="Select Semester" and self.var_search_id.get()!="":
             query="select student.stud_id,student.roll,student.name,student.dep,attendance.time,attendance.date,attendance.status from attendancetracker.student inner join attendancetracker.attendance on attendance.stdid=student.stud_id where attendance.date=%s and attendance.stdid=%s"
             value=(self.var_search_date.get(),self.var_search_id.get())
             if bool(match2)==FALSE:
                messagebox.showerror("Error","Student ID must be in number format",parent=self.root)
        elif self.var_search_dep.get()!="Select Department" and self.var_search_sem.get()!="Select Semester" and self.var_search_id.get()=="":
             query="select student.stud_id,student.roll,student.name,student.dep,attendance.time,attendance.date,attendance.status from attendancetracker.student inner join attendancetracker.attendance on attendance.stdid=student.stud_id where attendance.date=%s and student.dep=%s and student.sem=%s"
             value=(self.var_search_date.get(),self.var_search_dep.get(),self.var_search_sem.get())
        elif self.var_search_dep.get()!="Select Department" and self.var_search_sem.get()=="Select Semester" and self.var_search_id.get()!="":
             query="select student.stud_id,student.roll,student.name,student.dep,attendance.time,attendance.date,attendance.status from attendancetracker.student inner join attendancetracker.attendance on attendance.stdid=student.stud_id where attendance.date=%s and student.dep=%s and attendance.stdid=%s"
             value=(self.var_search_date.get(),self.var_search_dep.get(),self.var_search_id.get())
             if bool(match2)==FALSE:
                messagebox.showerror("Error","Student ID must be in number format",parent=self.root)
        elif self.var_search_dep.get()=="Select Department" and self.var_search_sem.get()!="Select Semester" and self.var_search_id.get()!="":
             query="select student.stud_id,student.roll,student.name,student.dep,attendance.time,attendance.date,attendance.status from attendancetracker.student inner join attendancetracker.attendance on attendance.stdid=student.stud_id where attendance.date=%s and student.sem=%s and attendance.stdid=%s "
             value=(self.var_search_date.get(),self.var_search_sem.get(),self.var_search_id.get()) 
             if bool(match2)==FALSE:
                messagebox.showerror("Error","Student ID must be in number format",parent=self.root)                 
        else:
             messagebox.showerror("Error","Something went wrong",parent=self.root)
        try :            
            my_cursor1.execute(query,value)                   
            data= my_cursor1.fetchall()
            
            if len(data)!=0:
                self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())
                mydata.clear()
                for i in data:
                    self.AttendanceReport_table.insert("",END,values=i)
                    mydata.append(i)
            else:
                messagebox.showerror("Error","Record not found",parent=self.root)
            conn.commit()
            conn.close() 
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)  

    def return_main(self):
        self.root.destroy()


        

if __name__ == "__main__":        
    root=Tk()
    obj=Attendance(root)
    root.mainloop()        
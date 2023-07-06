from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import re



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1355x700+0+0") 
        self.root.title("attendance tracker")


    #Variables
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_stud_id=StringVar()
        self.var_stud_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_stud_email=StringVar()
        self.var_par_email=StringVar()
        self.var_search_type=StringVar()
        self.var_search_sid=StringVar()


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
        title_lbl=Label(bg_img,text="STUDENT  REGISTRATION",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1355,height=45)

        back_btn=Button(title_lbl,text="Back",command=self.return_main,width=10,font=("times new roman",12,"bold"),bg="black",fg="White")
        back_btn.place(x=0,y=0,width=110,height=50)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1345,height=500)

        # Left Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=710,height=480)

        img_left=Image.open(r"D:\Programs\attendance_tracker\images\attendace.jpg")
        img_left=img_left.resize((700,100),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img_left)

        f_lbl2=Label(Left_frame,image=self.photoimg3)
        f_lbl2.place(x=0,y=0,width=705,height=90)

        #Current Cource
        current_course=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course.place(x=5,y=90,width=695,height=80)

        #Department
        dep_lable=Label(current_course,text='Department :',font=("times new roman",12,"bold"),bg="white")
        dep_lable.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only",width=16)
        dep_combo["values"]=("Select Department","MCA","MBA")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #Year
        year_lable=Label(current_course,text='Year :',font=("times new roman",12,"bold"),bg="white")
        year_lable.grid(row=0,column=2,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=10)
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Semester
        sem_lable=Label(current_course,text='Semester :',font=("times new roman",12,"bold"),bg="white")
        sem_lable.grid(row=0,column=4,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=14)
        sem_combo["values"]=("Select Semester","Semester-1","Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=0,column=5,padx=2,pady=10,sticky=W)

        #Student Information
        stud_info=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        stud_info.place(x=5,y=175,width=695,height=283)

        #Student id
        StuId_Lable=Label(stud_info,text="Student ID :",font=("times new roman",12,"bold"),bg="white")
        StuId_Lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudId_entry=ttk.Entry(stud_info,textvariable=self.var_stud_id,width=20,font=("times new roamn",12,"bold"))
        StudId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

         #Student name
        StuName_Lable=Label(stud_info,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        StuName_Lable.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        StudName_entry=ttk.Entry(stud_info,textvariable=self.var_stud_name,width=20,font=("times new roamn",12,"bold"))
        StudName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         #Student Division
        StuDiv_Lable=Label(stud_info,text="Division :",font=("times new roman",12,"bold"),bg="white")
        StuDiv_Lable.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #StuDiv_entry=ttk.Entry(stud_info,textvariable=self.var_div,width=20,font=("times new roamn",12,"bold"))
        #StuDiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(stud_info,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=14)
        div_combo["values"]=("Select Division","A1","A2","B1","B2")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Student Roll no
        StuRollno_Lable=Label(stud_info,text="Roll No. :",font=("times new roman",12,"bold"),bg="white")
        StuRollno_Lable.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        StuRollno_entry=ttk.Entry(stud_info,textvariable=self.var_roll,width=20,font=("times new roamn",12,"bold"))
        StuRollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #Student Gender
        StuGender_Lable=Label(stud_info,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        StuGender_Lable.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #StuGender_entry=ttk.Entry(stud_info,textvariable=self.var_gender,width=20,font=("times new roamn",12,"bold"))
        #StuGender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(stud_info,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=14)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

         #Student DOB
        StuGender_Lable=Label(stud_info,text="DOB :",font=("times new roman",12,"bold"),bg="white")
        StuGender_Lable.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        StuGender_entry=ttk.Entry(stud_info,textvariable=self.var_dob,width=20,font=("times new roamn",12,"bold"))
        StuGender_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Student Phone No
        StuPhoneNO_Lable=Label(stud_info,text="Phone No. :",font=("times new roman",12,"bold"),bg="white")
        StuPhoneNO_Lable.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        StuPhoneNO_entry=ttk.Entry(stud_info,textvariable=self.var_phone,width=20,font=("times new roamn",12,"bold"))
        StuPhoneNO_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Student Address
        StuAddress_Lable=Label(stud_info,text="Address :",font=("times new roman",12,"bold"),bg="white")
        StuAddress_Lable.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        StuAddress_entry=ttk.Entry(stud_info,textvariable=self.var_address,width=20,font=("times new roamn",12,"bold"))
        StuAddress_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Student Email
        StuEmail_Lable=Label(stud_info,text="Student Email :",font=("times new roman",12,"bold"),bg="white")
        StuEmail_Lable.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        StuEmail_entry=ttk.Entry(stud_info,textvariable=self.var_stud_email,width=20,font=("times new roamn",12,"bold"))
        StuEmail_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Parent Email
        ParEmail_Lable=Label(stud_info,text="Parent Email :",font=("times new roman",12,"bold"),bg="white")
        ParEmail_Lable.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        ParEmail_entry=ttk.Entry(stud_info,textvariable=self.var_par_email,width=20,font=("times new roamn",12,"bold"))
        ParEmail_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(stud_info,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)        
        radiobtn2=ttk.Radiobutton(stud_info,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #buttons frame
        btn_frame=Frame(stud_info,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=690,height=30)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="black",fg="White")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="black",fg="White")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",12,"bold"),bg="black",fg="White")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="black",fg="White")
        reset_btn.grid(row=0,column=3)

         #buttons frame
        btn_frame1=Frame(stud_info,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=230,width=690,height=30)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=25,font=("times new roman",12,"bold"),bg="black",fg="White")
        take_photo_btn.grid(row=1,column=0,padx=50)

        update_photo_btn=Button(btn_frame1,command=self.update_dataset,text="Update Photo Sample",width=25,font=("times new roman",12,"bold"),bg="black",fg="White")
        update_photo_btn.grid(row=1,column=1,padx=50)


        # Right Frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="white")
        Right_frame.place(x=730,y=10,width=600,height=480)

        img_right=Image.open(r"D:\Programs\attendance_tracker\images\ab.jpg")
        img_right=img_right.resize((500,100),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img_right)

        r_lbl3=Label(Right_frame,image=self.photoimg4)
        r_lbl3.place(x=70,y=0,width=500,height=90)

         # Search System
        Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),bg="white")
        Search_frame.place(x=5,y=90,width=585,height=80)

        Search_Lable=Label(Search_frame,text="Search By :",font=("times new roman",12,"bold"),bg="red",fg="white")
        Search_Lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_search_type,font=("times new roman",12,"bold"),state="readonly",width=10)
        search_combo["values"]=("Select ","Student Id","Roll No","Name","Phone No","Email")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search_sid,width=13,font=("times new roamn",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",command=self.search_data,width=10,font=("times new roman",12,"bold"),bg="black",fg="White")
        search_btn.grid(row=0,column=23,padx=4)

        showAll_btn=Button(Search_frame,text="Show All",command=self.fetch_data,width=10,font=("times new roman",12,"bold"),bg="black",fg="White")
        showAll_btn.grid(row=0,column=4,padx=4)

         # Table Frame
        table_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=180,width=585,height=273)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","year","sem","id","name","div","roll","gender","dob","phone","address","stuemail","paremail","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll no.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("phone",text="Phone no.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("stuemail",text="Student Email")
        self.student_table.heading("paremail",text="Parent Email")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)        
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("stuemail",width=100)
        self.student_table.column("paremail",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #function declaration

    def add_data(self):
        sid=self.var_stud_id.get()
        sroll=self.var_roll.get()
        sphone=self.var_phone.get()
        semail=self.var_stud_email.get()
        pemail=self.var_par_email.get()
        pattern1=  r'^\d{1,6}$'
        pattern2=  r'^\d{1,6}$'
        pattern3= r'^\d{10}$'
        pattern4= r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$'
        match1=re.match(pattern1, sid)
        match2=re.match(pattern2, sroll)
        match3=re.match(pattern3, sphone)
        match4=re.match(pattern4, semail)
        match5=re.match(pattern4, pemail)
        if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year"  or self.var_sem.get()=="Select Semester" or self.var_stud_id.get()=="" or self.var_stud_name.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_stud_email.get()=="" or self.var_par_email.get()=="" or self.var_radio1.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif bool(match3)==FALSE:
            messagebox.showerror("Error","Phone No must be 10 digit number",parent=self.root)
        elif bool(match1)==FALSE:
            messagebox.showerror("Error","Student Id must be less than 7 digit number",parent=self.root)
        elif bool(match2)==FALSE:
            messagebox.showerror("Error","Roll No must be less than 7 digit number",parent=self.root)
        elif bool(match4)==FALSE:
            messagebox.showerror("Error","Please enter correct Student email address",parent=self.root)
        elif bool(match5)==FALSE:
            messagebox.showerror("Error","Please enter correct Parent email address",parent=self.root)        
        else :
            try :
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_dep.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_stud_id.get(),
                                                                                        self.var_stud_name.get(),
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_stud_email.get(),
                                                                                        self.var_par_email.get(),
                                                                                        self.var_radio1.get()
                                                                                    ))
                conn.commit() 
                self.fetch_data()                                                     
                conn.close()
                messagebox.showinfo("success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    

    # Data Search    
    def search_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
        my_cursor1=conn.cursor()  

        if self.var_search_type.get()=="Select ":
             messagebox.showerror("Error","All Please select any Search Type",parent=self.root)
        elif self.var_search_sid.get()=="":
             messagebox.showerror("Error","Please enter the value of search",parent=self.root)
        elif self.var_search_type.get()=="Student Id":
             query="select * from student where stud_id=%s"
        elif self.var_search_type.get()=="Roll No":
             query="select * from student where roll=%s"
        elif self.var_search_type.get()=="Phone No":
             query="select * from student where phone=%s"
        elif self.var_search_type.get()=="Email":
             query="select * from student where stud_email=%s"
        elif self.var_search_type.get()=="Name":
             query="select * from student where name=%s"             
        else:
             messagebox.showerror("Error","Something went wrong",parent=self.root)
        value=(self.var_search_sid.get(),)
        my_cursor1.execute(query,value)                   
        data= my_cursor1.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
        else:
                messagebox.showerror("Error","Record not found",parent=self.root)
        conn.commit()
        conn.close() 
       

    # Data Showing
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
        my_cursor1=conn.cursor()
        my_cursor1.execute("select * from student")
        data= my_cursor1.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
    
    #Data Retriving
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data1=content["values"]

        self.var_dep.set(data1[0])
        self.var_year.set(data1[1])
        self.var_sem.set(data1[2])
        self.var_stud_id.set(data1[3])
        self.var_stud_name.set(data1[4])
        self.var_div.set(data1[5])
        self.var_roll.set(data1[6])
        self.var_gender.set(data1[7])
        self.var_dob.set(data1[8])
        self.var_phone.set(data1[9])
        self.var_address.set(data1[10])
        self.var_stud_email.set(data1[11])
        self.var_par_email.set(data1[12])
        self.var_radio1.set(data1[13])        

# update function
    def update_data(self):
        sid=self.var_stud_id.get()
        sroll=self.var_roll.get()
        sphone=self.var_phone.get()
        semail=self.var_stud_email.get()
        pemail=self.var_par_email.get()
        pattern1=  r'^\d{1,6}$'
        pattern2=  r'^\d{1,6}$'
        pattern3= r'^\d{10}$'
        pattern4= r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$'
        match1=re.match(pattern1, sid)
        match2=re.match(pattern2, sroll)
        match3=re.match(pattern3, sphone)
        match4=re.match(pattern4, semail)
        match5=re.match(pattern4, pemail)
        if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year"  or self.var_sem.get()=="Select Semester" or self.var_stud_id.get()=="" or self.var_stud_name.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_stud_email.get()=="" or self.var_par_email.get()=="" or self.var_radio1.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif bool(match3)==FALSE:
            messagebox.showerror("Error","Phone No must be 10 digit number",parent=self.root)
        elif bool(match1)==FALSE:
            messagebox.showerror("Error","Student Id must be less than 7 digit number",parent=self.root)
        elif bool(match2)==FALSE:
            messagebox.showerror("Error","Roll No must be less than 7 digit number",parent=self.root)
        elif bool(match4)==FALSE:
            messagebox.showerror("Error","Please enter correct Student email address",parent=self.root)
        elif bool(match5)==FALSE:
            messagebox.showerror("Error","Please enter correct Parent email address",parent=self.root) 
        else :
                try :
                    Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                    if Update>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
                        my_cursor2=conn.cursor()                       
                        my_cursor2.execute("update student set dep=%s,year=%s,sem=%s,name=%s,roll=%s,gender=%s,dob=%s,phone=%s,address=%s,stud_email=%s,par_email=%s,photo=%s,division=%s where stud_id=%s",(self.var_dep.get(),self.var_year.get(),self.var_sem.get(),self.var_stud_name.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_phone.get(),self.var_address.get(),self.var_stud_email.get(),self.var_par_email.get(),self.var_radio1.get(),self.var_div.get(),self.var_stud_id.get()))               
                                                                                                                                                                        
                    else:
                        if not Update:
                            return 
                    messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# Delete function
    def delete_data(self):
        if self.var_stud_id.get()=="":
                messagebox.showerror("Error","Student id must be required",parent=self.root)
        else :
                try :    
                    delete=messagebox.askyesno("Delete Page","Do you want to delete this student record",parent=self.root)
                    if delete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
                        my_cursor2=conn.cursor() 
                        sql="delete from student where stud_id=%s"
                        val=(self.var_stud_id.get(),)
                        my_cursor2.execute(sql,val)
                    else:
                         if not delete:
                              return
                    conn.commit()                
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete","Successfully delete student record")
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                  

# Reset Function
    def reset_data(self):
         self.var_dep.set("Select Department")        
         self.var_year.set("Select Year")
         self.var_sem.set("Select Semester")
         self.var_stud_id.set("")
         self.var_stud_name.set("")
         self.var_div.set("Select Division")
         self.var_roll.set("") 
         self.var_gender.set("Select Gender")
         self.var_dob.set("")
         self.var_phone.set("")
         self.var_address.set("") 
         self.var_stud_email.set("") 
         self.var_par_email.set("")
         self.var_radio1.set("")

# Photo sample function
    def generate_dataset(self):
          if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year"  or self.var_sem.get()=="Select Semester" or self.var_stud_id.get()=="" or self.var_stud_name.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_stud_email.get()=="" or self.var_par_email.get()=="" or self.var_radio1.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
          else :
                try :
                    
                    # conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
                    # my_cursor2=conn.cursor() 
                    # my_cursor2.execute("select * from student")
                    # myresult=my_cursor2.fetchall()
                    # id=0
                    # for x in myresult:
                    #     id+=1
                    # my_cursor2.execute("update student set dep=%s,year=%s,sem=%s,name=%s,roll=%s,gender=%s,dob=%s,phone=%s,address=%s,stud_email=%s,par_email=%s,photo=%s,division=%s where stud_id=%s",(self.var_dep.get(),self.var_year.get(),self.var_sem.get(),self.var_stud_name.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_phone.get(),self.var_address.get(),self.var_stud_email.get(),self.var_par_email.get(),self.var_radio1.get(),self.var_div.get(),self.var_stud_id.get()==id+1))               

                    # conn.commit()
                    # self.fetch_data()
                    # self.reset_data()
                    # conn.close()

                    #load predefined data on face frontals from opencv
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                         faces=face_classifier.detectMultiScale(gray,1.3,5)

                         for (x,y,w,h) in faces:
                              face_cropped=img[y:y+h,x:x+w]
                              return face_cropped
                         
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                         ret,my_frame=cap.read()
                         if face_cropped(my_frame) is not None:
                              img_id+=1  
                              face=cv2.resize(face_cropped(my_frame),(450,450))                      
                              face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                              file_name_path="data/user."+str(self.var_stud_id.get())+"."+str(img_id)+".jpg"
                              cv2.imwrite(file_name_path,face)
                              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                              cv2.imshow("Cropped Face",face)

                         if cv2.waitKey(1)==13 or int(img_id)==100:
                              break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets completed..")
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                  


    def update_dataset(self):
          if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year"  or self.var_sem.get()=="Select Semester" or self.var_stud_id.get()=="" or self.var_stud_name.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_stud_email.get()=="" or self.var_par_email.get()=="" or self.var_radio1.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
          else :
                try :
                    
                    #conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
                    #my_cursor2=conn.cursor() 
                    #my_cursor2.execute("select * from student")
                    #myresult=my_cursor2.fetchall()
                    #id=0
                    #for x in myresult:
                    #    id+=1
                    #my_cursor2.execute("update student set dep=%s,year=%s,sem=%s,name=%s,roll=%s,gender=%s,dob=%s,phone=%s,address=%s,stud_email=%s,par_email=%s,photo=%s,division=%s where stud_id=%s",(self.var_dep.get(),self.var_year.get(),self.var_sem.get(),self.var_stud_name.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_phone.get(),self.var_address.get(),self.var_stud_email.get(),self.var_par_email.get(),self.var_radio1.get(),self.var_div.get(),self.var_stud_id.get()==id+1))               

                    #conn.commit()
                    #self.fetch_data()
                    #self.reset_data()
                    #conn.close()

                    #load predefined data on face frontals from opencv
                    id=self.var_stud_id.get()
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                         faces=face_classifier.detectMultiScale(gray,1.3,5)

                         for (x,y,w,h) in faces:
                              face_cropped=img[y:y+h,x:x+w]
                              return face_cropped
                         
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                         ret,my_frame=cap.read()
                         if face_cropped(my_frame) is not None:
                              img_id+=1  
                              face=cv2.resize(face_cropped(my_frame),(450,450))                      
                              face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                              file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                              cv2.imwrite(file_name_path,face)
                              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                              cv2.imshow("Cropped Face",face)

                         if cv2.waitKey(1)==13 or int(img_id)==100:
                              break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Updating data sets completed..")
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                            
    

    def return_main(self):
        self.root.destroy()                   
         

if __name__ == "__main__":        
    root=Tk()
    obj=Student(root)
    root.mainloop()
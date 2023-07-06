from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry
import re
import smtplib as s



mydata=[]
class Tracking:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1355x700+0+0") 
        self.root.title("attendance tracker")

        #Variables
        self.var_search_date=StringVar()
        self.var_search_date1=StringVar()
        self.var_search_id=StringVar()

        self.Var_total_clg_days=StringVar()

        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_tatal_pre_days=StringVar()
        self.var_percentage=StringVar()

        self.id=StringVar()
        self.roll=StringVar()
        self.present_days=StringVar()
        self.percentage=StringVar()

        self.greeting=StringVar()
        self.info=StringVar()

        self.var_std_email=StringVar()
        self.var_par_email=StringVar()        
        
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
        title_lbl=Label(bg_img,text="TRACE  STUDENT  ATTENDANCE",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1355,height=45)

        back_btn=Button(title_lbl,text="Back",command=self.return_main,width=10,font=("times new roman",12,"bold"),bg="black",fg="White")
        back_btn.place(x=0,y=0,width=110,height=50)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1345,height=500)

        heading=Label(main_frame,text="Search The Student Present Days For Specific Duration ",font=("times new roman",22,"bold"),bg="white",fg="black")
        heading.place(x=350,y=5) 
        
        # Search frame        
        Search_frame1=LabelFrame(main_frame,bd=0,relief=RIDGE,text="",font=("times new roman",12,"bold"),bg="white")
        Search_frame1.place(x=380,y=50,width=400,height=80)                

        date=Label(Search_frame1,text="   Date From",font=("times new roman",12,"bold"),bg="white",fg="black")
        date.grid(row=0,column=0,padx=10,pady=1,sticky=W) 

        cal=DateEntry(Search_frame1,selectmode='day',date_pattern="dd/mm/y",textvariable=self.var_search_date)
        cal.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        date=Label(Search_frame1,text="   Date To",font=("times new roman",12,"bold"),bg="white",fg="black")
        date.grid(row=0,column=1,padx=10,pady=1,sticky=W)                

        date_entry=DateEntry(Search_frame1,selectmode='day',date_pattern="dd/mm/y",textvariable=self.var_search_date1,width=12)
        date_entry.grid(row=1,column=1,padx=10,pady=1,sticky=W)

        stuid=Label(Search_frame1,text="     Std Id",font=("times new roman",12,"bold"),bg="white",fg="black")
        stuid.grid(row=0,column=2,padx=10,pady=1,sticky=W)        

        stuid_entry=ttk.Entry(Search_frame1,textvariable=self.var_search_id,width=12,font=("times new roamn",12,"bold"))
        stuid_entry.grid(row=1,column=2,padx=10,pady=1,sticky=W)
       
       #search Button
        search_btn1=Button(main_frame,text="Search",command=self.retrive_data,width=10,font=("times new roman",12,"bold"),bg="black",fg="White")
        search_btn1.place(x=750,y=80,width=250,height=25)

        #heading2
        heading1=Label(main_frame,text="Enter The Total College Days For Given Duration ",font=("times new roman",19,"bold"),bg="white",fg="black")
        heading1.place(x=420,y=120)

         # Calculate frame        
        Cal_frame1=LabelFrame(main_frame,bd=0,relief=RIDGE,text="",font=("times new roman",12,"bold"),bg="white")
        Cal_frame1.place(x=470,y=160,width=400,height=80)                

        total_days_entry=ttk.Entry(Cal_frame1,textvariable=self.Var_total_clg_days,width=20,font=("times new roamn",12,"bold"))
        total_days_entry.grid(row=0,column=0,padx=10,pady=1,sticky=W) 

        search_btn2=Button(Cal_frame1,text="Calculate Percentage",command=self.cal_percentage,width=20,height=0,font=("times new roman",12,"bold"),bg="black",fg="White")
        search_btn2.grid(row=0,column=1,padx=10,pady=1,sticky=W)

        #Lables and entries Frame
        lbl_frame=LabelFrame(main_frame,bd=0,relief=RIDGE,font=("times new roman",12,"bold"),bg="white")
        lbl_frame.place(x=480,y=240,width=400,height=70)
         #Attendance id
        Student_Lable=Label(lbl_frame,text="",textvariable=self.id,font=("times new roman",12,"bold"),bg="white")
        Student_Lable.grid(row=0,column=0,padx=0,pady=0,sticky=W)

        StudentId_entry=Label(lbl_frame,width=9,textvariable=self.var_id,font=("times new roamn",12,"bold"),bg="white",fg="red")
        StudentId_entry.grid(row=0,column=1,padx=0,pady=0,sticky=W)

         #Roll
        roll_Lable=Label(lbl_frame,text="",textvariable=self.roll,font=("times new roman",12,"bold"),bg="white")
        roll_Lable.grid(row=0,column=2,padx=0,pady=0,sticky=W)

        atten_roll=Label(lbl_frame,width=12,textvariable=self.var_roll,font=("times new roamn",12,"bold"),bg="white",fg="red")
        atten_roll.grid(row=0,column=3,padx=0,pady=0,sticky=W)

         #Present Days
        presenty_Lable=Label(lbl_frame,text="",textvariable=self.present_days,font=("times new roman",12,"bold"),bg="white")
        presenty_Lable.grid(row=1,column=0,padx=0,pady=5,sticky=W)

        presenty_entry=Label(lbl_frame,width=9,textvariable=self.var_tatal_pre_days,font=("times new roamn",12,"bold"),bg="white",fg="red")
        presenty_entry.grid(row=1,column=1,padx=0,pady=5,sticky=W)

         #Percentage
        per_Lable=Label(lbl_frame,text="",textvariable=self.percentage,font=("times new roman",12,"bold"),bg="white")
        per_Lable.grid(row=1,column=2,padx=0,pady=5,sticky=W)

        per_roll=Label(lbl_frame,width=12,textvariable=self.var_percentage,font=("times new roamn",12,"bold"),bg="white",fg="red")
        per_roll.grid(row=1,column=3,padx=0,pady=5,sticky=W)

        #name
        name=Label(main_frame,textvariable=self.var_name,font=("times new roamn",25,"bold"),fg="red",bg="white")
        name.place(x=570,y=200)

        #greeting
        greeting=Label(main_frame,textvariable=self.greeting,font=("times new roamn",35,"bold"),fg="green",bg="white")
        greeting.place(x=480,y=320)

        #info
        info=Label(main_frame,textvariable=self.info,font=("times new roamn",15,"bold"),fg="blue",bg="white")
        info.place(x=400,y=380)

        #radio buttons
        self.var_radio1=StringVar()        
        radiobtn1=ttk.Radiobutton(main_frame,variable=self.var_radio1,text="Student",value="1")
        radiobtn1.place(x=500,y=440)        
        radiobtn2=ttk.Radiobutton(main_frame,variable=self.var_radio1,text="Parent",value="2")
        radiobtn2.place(x=600,y=440)
        radiobtn3=ttk.Radiobutton(main_frame,variable=self.var_radio1,text="Both",value="3")
        radiobtn3.place(x=700,y=440)
        print(self.var_radio1.get())

        #send buttons         
        send_btn=Button(main_frame,text="Send Email",command=self.send_email,bd=0,font=("times new roman",12,"bold"),bg="White",fg="black")
        send_btn.place(x=800,y=437)

    def initialize(self):
        self.id.set("Student ID :")
        self.roll.set("Roll No.:")
        self.present_days.set("Present Days :")        
    
    #Search Data
    def retrive_data(self):
        new_id=self.var_search_id.get()
        pattern1=  r'^\d{1,6}$'
        match2=re.match(pattern1,new_id)
        if bool(match2)==TRUE:
            try:                
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
                my_cursor1=conn.cursor() 
                new_query="SELECT date FROM attendance WHERE date BETWEEN %s AND %s and stdid=%s and status=%s"
                new_value=(self.var_search_date.get(),self.var_search_date1.get(),self.var_search_id.get(),"Present")
                my_cursor1.execute(new_query,new_value)                   
                new_data= my_cursor1.fetchall()
                count=0
                for row in new_data:
                    count+=1
                if count!=0:
                    self.initialize()
                    self.var_id.set(self.var_search_id.get())
                    self.var_tatal_pre_days.set(count)
                    query="select name,roll,stud_email,par_email from student where stud_id=%s"
                    value=(self.var_search_id.get(),)
                    my_cursor1.execute(query,value)
                    data=my_cursor1.fetchone()
                    self.var_name.set(data[0])
                    self.var_roll.set(data[1])
                    self.var_std_email.set(data[2])
                    self.var_par_email.set(data[3])
                else:
                    messagebox.showerror("Error","Record Not Found",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        else:
            messagebox.showerror("Error","Please Enter ID in only number format",parent=self.root)

    def cal_percentage(self):
        new_days=self.Var_total_clg_days.get()
        pattern2=  r'^\d{1,6}$'
        match3=re.match(pattern2,new_days)
        if self.var_id.get()=="" or self.var_roll.get()=="" or self.var_name.get()=="" or self.var_tatal_pre_days.get()=="":
            messagebox.showerror("Error","Please firstly search the student attendance",parent=self.root)
        elif bool(match3)==TRUE:
            per=(int(self.var_tatal_pre_days.get())/int(self.Var_total_clg_days.get()))*100
            self.var_percentage.set(round(per,2))
            self.percentage.set("Percentage :")
            if round(per,2)>=70:
                self.greeting.set("..Congratulation..")
                self.info.set("You are eligible to take exam, Your attendance is more than 70"+"%")
                img10=Image.open(r"D:\Programs\attendance_tracker\images\c1.jpg")
                img10=img10.resize((300,350),Image.Resampling.LANCZOS)
                self.photoimg10=ImageTk.PhotoImage(img10)
                f_lbl10=Label(self.root,image=self.photoimg10)
                f_lbl10.place(x=10,y=335,width=300,height=350)
                img11=Image.open(r"D:\Programs\attendance_tracker\images\c2.jpg")
                img11=img11.resize((300,350),Image.Resampling.LANCZOS)
                self.photoimg11=ImageTk.PhotoImage(img11)
                f_lbl11=Label(self.root,image=self.photoimg11)
                f_lbl11.place(x=1050,y=335,width=300,height=350)
            else :
                self.greeting.set("     ..Sorry..")
                self.info.set("You are not eligible to take exam, due to less than 70"+"%"+" attendance..")
                img12=Image.open(r"D:\Programs\attendance_tracker\images\b1.jpg")
                img12=img12.resize((300,350),Image.Resampling.LANCZOS)
                self.photoimg12=ImageTk.PhotoImage(img12)
                f_lbl12=Label(self.root,image=self.photoimg12)
                f_lbl12.place(x=10,y=335,width=300,height=350)
                img13=Image.open(r"D:\Programs\attendance_tracker\images\b1.jpg")
                img13=img13.resize((300,350),Image.Resampling.LANCZOS)
                self.photoimg13=ImageTk.PhotoImage(img13)
                f_lbl13=Label(self.root,image=self.photoimg13)
                f_lbl13.place(x=1050,y=335,width=300,height=350)
        else:
           messagebox.showerror("Error","Please Enter College Days in only number format",parent=self.root)

    def send_email(self):
        if self.var_id.get()=="" or self.var_roll.get()=="" or self.var_name.get()=="" or self.var_tatal_pre_days.get()=="" or self.Var_total_clg_days.get()=="" or self.var_percentage.get()=="":
            messagebox.showerror("Error","Please firstly calculate the student attendance",parent=self.root) 
        else:               
            if self.var_radio1.get()=="1":
                self.std_msg="Dear Student   "+self.greeting.get() 
                self.std_name=self.var_name.get()           
                self.body="     "+self.info.get()
                self.body1="            From "+self.var_search_date.get()+" To "+self.var_search_date1.get()+" total college days are "+self.Var_total_clg_days.get()+", Out of these you are present "+self.var_tatal_pre_days.get()+" days. According to this your attendance is "+self.var_percentage.get()+" percentage"
                self.listOfAddress=[self.var_std_email.get()]
                self.send_email1()                      
            elif self.var_radio1.get()=="2":
                self.std_msg="Dear Parents   "+self.greeting.get() 
                self.std_name="Your child "+self.var_name.get()           
                self.body="     "+self.info.get()
                self.body1="            From "+self.var_search_date.get()+" To "+self.var_search_date1.get()+" total college days are "+self.Var_total_clg_days.get()+", Out of these your child was present "+self.var_tatal_pre_days.get()+" days. According to this your child attendance is "+self.var_percentage.get()+" percentage"            
                self.listOfAddress=[self.var_par_email.get()]
                self.send_email1()                      
            elif self.var_radio1.get()=="3":
                self.std_msg="Dear Student   "+self.greeting.get() 
                self.std_name=self.var_name.get()           
                self.body="     "+self.info.get()
                self.body1="            From "+self.var_search_date.get()+" To "+self.var_search_date1.get()+" total college days are "+self.Var_total_clg_days.get()+", Out of these you are present "+self.var_tatal_pre_days.get()+" days. According to this your attendance is "+self.var_percentage.get()+" percentage"
                self.listOfAddress=[self.var_std_email.get()]
                self.send_email1()

                self.std_msg="Dear Parents   "+self.greeting.get() 
                self.std_name="Your child "+self.var_name.get()           
                self.body="     "+self.info.get()
                self.body1="            From "+self.var_search_date.get()+" To "+self.var_search_date1.get()+" total college days are "+self.Var_total_clg_days.get()+", Out of these your child was present "+self.var_tatal_pre_days.get()+" days. According to this your child attendance is "+self.var_percentage.get()+" percentage"            
                self.listOfAddress=[self.var_par_email.get()]
                self.send_email1()             
            elif self.var_radio1.get()=="":
                messagebox.showerror("error","Please select Student or Parent or Both")
        
    def send_email1(self):
            try:
                ob=s.SMTP("smtp.gmail.com",587)
                ob.starttls()
                ob.login("pravindhembare85@gmail.com","anwwcsmbxxuhxrsb")
                subject="Exam Eligibility..."            
                msg="Subject:{}\n\n{}\n{}\n{}\n{}".format(subject,self.std_msg,self.std_name,self.body,self.body1)
                ob.sendmail("pravindhembare85@gmail.com",self.listOfAddress,msg)
                ob.quit()
                messagebox.showinfo("Success","Email send successfully..")
            except Exception as es:
                messagebox.showerror("error","Something went wrong... Email not send")
            
    def return_main(self):
        self.root.destroy()


if __name__ == "__main__":        
    root=Tk()
    obj=Tracking(root)
    root.mainloop()     
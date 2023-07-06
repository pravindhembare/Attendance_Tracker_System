from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Attendance_Tracker
import re

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1355x700+0+0")

        self.var_securityQ1=StringVar()
        self.var_securityA1=StringVar()
        self.var_pass1=StringVar()
        self.var_conpass1=StringVar()

        img=Image.open(r"D:\Programs\attendance_tracker\images\login.jpg")
        img=img.resize((1355,700),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1355,height=700)

        frame=Frame(self.root,bg="black")
        frame.place(x=530,y=150,width=340,height=450)

        img1=Image.open(r"D:\Programs\attendance_tracker\images\icon.png")
        img1=img1.resize((70,70),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl1=Label(self.root,image=self.photoimg1,bg="black",borderwidth=0)
        f_lbl1.place(x=660,y=155,width=70,height=70)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=90,y=100)

        #Labels
        username_lbl=Label(frame,text="Username :",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=25,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password_lbl=Label(frame,text="Password :",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=25,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #Login Button
        loginbtn=Button(frame,text="Login",command=self.signin,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

         #Register Button
        registerbtn=Button(frame,text="New User Register",command=self.rigister_window,font=("times new roman",12,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

         #Forgate Pass Button
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",12,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activebackground="black")
        registerbtn.place(x=7,y=370,width=160)

    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    #login function
    def signin(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required..",parent=self.root)                       
        else:             
             conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from admin where uname=%s and password=%s",(
                                                                self.txtuser.get(),
                                                                self.txtpass.get()
                                                        ))
             row=my_cursor.fetchone()
             if row==None:
                 messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
             else:
                 open_main=messagebox.askyesno("YesNo","Access only admin",parent=self.root)
                 if open_main>0:
                     self.new_window=Toplevel(self.root)
                     self.app=Attendance_Tracker(self.new_window)
                 else:
                     if not open_main:
                         return
             conn.commit()
             conn.close()

    def reset_password(self):
        password=bool(re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-={}|;:,.<>/?]).{8,}$',self.var_pass1.get()))
        conpassword=bool(re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-={}|;:,.<>/?]).{8,}$',self.var_conpass1.get()))
        if self.var_securityA1.get()=="Select Quetion" or self.var_conpass1.get()=="" or self.var_pass1.get()=="" or self.var_securityA1.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        elif password==FALSE or conpassword==FALSE:
            messagebox.showerror("Error","Password must contain at least one uppercase letter, at least one lowercase letter,at least one digit,at least one special character and have minimum length of 8 characters",parent=self.root2)
        elif self.var_pass1.get()!=self.var_conpass1.get():
            messagebox.showerror("Error","password and confirm password must be same",parent=self.root2)
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
             my_cursor=conn.cursor()
             query="select * from admin where uname=%s and securityQ=%s and securityA=%s"
             value=(self.txtuser.get(),self.var_securityQ1.get(),self.var_securityA1.get())
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             if row==None:
                 messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
             else:
                 query=("update admin set password=%s where uname=%s")
                 value=(self.var_conpass1.get(),self.txtuser.get())
                 my_cursor.execute(query,value)

                 conn.commit()
                 conn.close()
                 messagebox.showinfo("Success","Password reset successfully",parent=self.root2)
                 self.root2.destroy()


    def forgot_password_window(self)             :
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please inter the User Name to reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
            my_cursor=conn.cursor()
            query="select * from admin where uname=%s"
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x420+530+180")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_q1=Label(self.root2,text="Security Quetion",font=("times new roman",15,"bold"),bg="white")
                security_q1.place(x=90,y=70)

                security_que1=ttk.Combobox(self.root2,textvariable=self.var_securityQ1,font=("times new roman",12,"bold"),state="readonly",width=14)
                security_que1["values"]=("Select Quetion","Your Birth Place","Your School Name","Your Pet Name","Your Friend Name")
                security_que1.current(0)
                security_que1.place(x=70,y=100,width=200,height=30)

                security1=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security1.place(x=90,y=140)

                security_entry1=ttk.Entry(self.root2,textvariable=self.var_securityA1,font=("times new roman",15,"bold"))
                security_entry1.place(x=70,y=170,width=200)


                password1=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                password1.place(x=90,y=220)

                password_entry1=ttk.Entry(self.root2,textvariable=self.var_pass1,font=("times new roman",15,"bold"))
                password_entry1.place(x=70,y=250,width=200)

                cpassword1=Label(self.root2,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
                cpassword1.place(x=90,y=290)

                cpassword_entry1=ttk.Entry(self.root2,textvariable=self.var_conpass1,font=("times new roman",15,"bold"))
                cpassword_entry1.place(x=70,y=320,width=200)

                reset_btn=Button(self.root2,text="Reset Password",command=self.reset_password,width=18,font=("times new roman",13,"bold"),bg="green",fg="White")
                reset_btn.place(x=75,y=370)


    def main_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_Tracker(self.new_window)
                       

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1355x700+0+0")

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_uname=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_conpass=StringVar()
        self.var_check=IntVar()

        img=Image.open(r"D:\Programs\attendance_tracker\images\login.jpg")
        img=img.resize((1355,700),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1355,height=700)

        frame=Frame(self.root,bg="white")
        frame.place(x=390,y=150,width=650,height=450)

        register_lbl=Label(frame,text="REGISTER  HERE...",font=("times new roman",25,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=15)

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=70)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=100,width=200)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=350,y=70)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=350,y=100,width=200)


        phone=Label(frame,text="Phone No.",font=("times new roman",15,"bold"),bg="white")
        phone.place(x=50,y=140)

        phone_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        phone_entry.place(x=50,y=170,width=200)

        uname=Label(frame,text="User Name",font=("times new roman",15,"bold"),bg="white")
        uname.place(x=350,y=140)

        uname_entry=ttk.Entry(frame,textvariable=self.var_uname,font=("times new roman",15,"bold"))
        uname_entry.place(x=350,y=170,width=200)


        security_q=Label(frame,text="Security Quetion",font=("times new roman",15,"bold"),bg="white")
        security_q.place(x=50,y=210)

        security_que=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12,"bold"),state="readonly",width=14)
        security_que["values"]=("Select Quetion","Your Birth Place","Your School Name","Your Pet Name","Your Friend Name")
        security_que.current(0)
        security_que.place(x=50,y=240,width=200,height=30)
        
        security=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security.place(x=350,y=210)

        security_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        security_entry.place(x=350,y=240,width=200)


        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=50,y=280)

        password_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        password_entry.place(x=50,y=310,width=200)

        cpassword=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        cpassword.place(x=350,y=280)

        cpassword_entry=ttk.Entry(frame,textvariable=self.var_conpass,font=("times new roman",15,"bold"))
        cpassword_entry.place(x=350,y=310,width=200)

        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions.",font=("times new roman",12),onvalue=1,offvalue=0,bg="white")
        checkbtn.place(x=50,y=350)


        register_btn=Button(frame,text="Register Now",command=self.register_data,width=18,font=("times new roman",13,"bold"),bg="green",fg="White")
        register_btn.place(x=80,y=380)

        login_btn=Button(frame,text="Login Now",command=self.return_login,width=18,font=("times new roman",13,"bold"),bg="green",fg="White")
        login_btn.place(x=310,y=380)


    def register_data(self):
        phone=self.var_contact.get()
        pattern=r'^\d{10}$'
        match2=re.match(pattern, phone)
        fname=bool(re.match("^[a-zA-Z]+$",self.var_fname.get()))
        lname=bool(re.match("^[a-zA-Z]+$",self.var_lname.get()))
        password=bool(re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-={}|;:,.<>/?]).{8,}$',self.var_pass.get()))
        conpassword=bool(re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-={}|;:,.<>/?]).{8,}$',self.var_conpass.get()))
        if self.var_fname.get()==""  or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_pass.get()=="" or self.var_conpass.get()=="" or self.var_uname.get()=="" or self.var_securityQ.get()=="Select Quetion" or self.var_securityA.get()=="":
            messagebox.showerror("error","All fields are required")
        elif fname==FALSE or lname==FALSE:
            messagebox.showerror("Error"," First name and Last name contains only alphabetic characters.")
        elif  bool(match2)==FALSE:
            messagebox.showerror("Error","Phone No must be 10 digit number",parent=self.root)
        elif password==FALSE or conpassword==FALSE:
            messagebox.showerror("Error","Password must contain at least one uppercase letter, at least one lowercase letter,at least one digit,at least one special character and have minimum length of 8 characters")            
        elif self.var_pass.get()!=self.var_conpass.get():
            messagebox.showerror("error","password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("error",("Please agree our Terms and Conditions"))
        else:
            try :
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
                my_cursor=conn.cursor()
                query=("select * from admin where uname=%s")
                value=(self.var_uname.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist please try another user name")
                else:
                    my_cursor.execute("insert into admin values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_uname.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_conpass.get(),                                                                                       
                                                                                    ))
                conn.commit()                                                                     
                conn.close()
                messagebox.showinfo("success","Registration done successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def return_login(self):
        self.root.destroy()
            

if __name__ == "__main__":        
    main()        
from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
from datetime import datetime
import cv2



class Face_Detector:
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
        img2=Image.open(r"D:\Programs\attendance_tracker\images\download.jpg")
        img2=img2.resize((1355,570),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_img=Label(self.root,image=self.photoimg2)
        bg_img.place(x=0,y=130,width=1355,height=570)
        
        #Heading
        title_lbl=Label(self.root,text="TAKE  STUDENT ATTENDANCE",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=130,width=1355,height=45)

        back_btn=Button(title_lbl,text="Back",command=self.return_main,width=10,font=("times new roman",12,"bold"),bg="black",fg="White")
        back_btn.place(x=0,y=0,width=110,height=50)

        #Button
        btn=Button(bg_img,text="Take  Attendance",command=self.face_recog
                   ,cursor="hand2",font=("times new roman",25,"bold"),bg="black",fg="red")
        btn.place(x=100,y=260,width=350,height=50)

        #Attendance
    def mark_attendance(self,i,r,n,d):

        now=datetime.now()
        d1=now.strftime("%d/%m/%Y")
        dtString=now.strftime("%H:%M:%S")
         
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
        my_cursor=conn.cursor()

        query="select date from attendance where stdid=%s"
        value=(str(i),)      
        my_cursor.execute(query,value)
        date=my_cursor.fetchall()  
        count=0      
        for row in date:
            if row==(d1,):
                count+=1       
        
        if count==0:                    
            my_cursor.execute("insert into attendance(stdid,time,date,status) values(%s,%s,%s,%s)",(str(i),dtString,d1,"Present"))
            with open("std_att.csv","r+",newline="\n") as f:
                myDataList=f.readlines()
                name_list=[]
                for line in myDataList:
                    entry=line.split((","))
                    name_list.append(entry[0])
                #if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")                                                                    
        conn.commit() 
        




        


        #Face Recognition
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="attendancetracker")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where stud_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from student where stud_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from student where stud_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select stud_id from student where stud_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"Std Id :{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll :{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name :{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department :{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        vedio_cap=cv2.VideoCapture(0)

        while True:
            ret,img=vedio_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Wlecome TO face Recognition..",img)

            if cv2.waitKey(1)==13:
                break

        vedio_cap.release()
        cv2.destroyAllWindows()
        

    
    def return_main(self):
        self.root.destroy()



if __name__ == "__main__":        
    root=Tk()
    obj=Face_Detector(root)
    root.mainloop()

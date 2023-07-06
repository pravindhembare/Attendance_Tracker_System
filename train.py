from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:
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
        title_lbl=Label(self.root,text="TRAIN STUDENT DATA  SET",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=130,width=1355,height=45)

        back_btn=Button(title_lbl,text="Back",command=self.return_main,width=10,font=("times new roman",12,"bold"),bg="black",fg="White")
        back_btn.place(x=0,y=0,width=110,height=50)

        #Button
        btn=Button(bg_img,text="TRAIN  DATA",command=self.train_classifir,cursor="hand2",font=("times new roman",25,"bold"),bg="black",fg="red")
        btn.place(x=790,y=220,width=250,height=50)
       
    def train_classifir(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #Gray scale image
            iamageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(iamageNp)
            ids.append(id)
            cv2.imshow("Training",iamageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets completed...")

    def return_main(self):
        self.root.destroy()

if __name__ == "__main__":        
    root=Tk()
    obj=Train(root)
    root.mainloop()

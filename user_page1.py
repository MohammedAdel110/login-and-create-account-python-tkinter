from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import date


#Main page
userpage=Tk()
userpage.title('Userpage')
userpage.iconbitmap('C:/Users/121mo/OneDrive/Desktop/hospital/full project/iamge/hospital-building.ico')

Width=1920
Hight=1080

GetWidth=userpage.winfo_screenwidth()
GetHight=userpage.winfo_screenheight()

centerWidth=int((GetWidth-Width)/2)
centerHight=int((GetHight-Hight)/2)
userpage.geometry(f'{Width}x{Hight}+{centerWidth}+{centerHight}')

#Left Frame

sidebar = tk.Frame(userpage, width=400, bg='#ade8f4',relief=RAISED,highlightbackground="blue", highlightcolor="black")
sidebar.pack(side="left", fill="y")
#User Image
userimage_path=Image.open('C:/Users/121mo/OneDrive/Desktop/hospital/full project/iamge/user.png')
userImageTk=ImageTk.PhotoImage(userimage_path)

UsereImagelbl=Label(userpage,image=userImageTk,bg="#ade8f4")
UsereImagelbl.place(relx=0.02,rely=0.06)
#User name label
userNamelbl=Label(userpage,text='User name',font=('Arial',15,'bold'),bg='#ade8f4',fg='#0077b6')
userNamelbl.place(relx=0.06,rely=0.077)
#UserEmail label
UserEmail=Label(userpage,text='User@gmail.com',font=('Arial',8,'bold'),bg='#ade8f4',fg='#6c757d')
UserEmail.place(relx=0.06,rely=0.1)
#log out func
def logout():
    userpage.destroy()
    import login
    
#logoutbtn
logoutbtn=Button(userpage,text='Log out',font=('Arial',10,'bold'),width=30,fg='#0077b6',bg='#48cae4',relief='groove',command=logout)
logoutbtn.place(relx=0.023,rely=0.15)
#Date
today=date.today()
#Date lbl
Datelbl=Label(userpage,text=today,font=('Arial',13,'bold'),fg='#03045e')
Datelbl.place(relx=0.9,rely=0.03)
#Date image
DateImage_path=Image.open('C:/Users/121mo/OneDrive/Desktop/hospital/full project/iamge/calendar.png')
DateImageTk=ImageTk.PhotoImage(DateImage_path)
Datashow=Label(userpage,image=DateImageTk)
Datashow.place(relx=0.95,rely=0.01)
#Today Date lbl
Today_Date_lbl=Label(userpage,text="Today's Date",font=('Arial',10,'bold'),fg="#6c757d")
Today_Date_lbl.place(relx=0.9,rely=0.01)
#Book an appointment with the doctor
bookImage=Image.open('C:/Users/121mo/OneDrive/Desktop/hospital/full project/iamge/حجز.jpg')
bookImage.resize((400,600))
bookTk=ImageTk.PhotoImage(bookImage)

#book lbl
book_lbl=Label(userpage,image=bookTk)
book_lbl.place(relx=0.23,rely=0.15)
#book lbl text
bookText=Label(userpage,text="Book an appointment with the doctor?",font=('Arial',18,'bold'),fg="#0077b6")
bookText.place(relx=0.23,rely=0.12)
#book btn
book_btn=Button(userpage,text='Book now',font=('Arial',13,'bold'),width=39,bg='#48cae4',fg='white')
book_btn.place(relx=0.23,rely=0.63)
#Buy medicine
medicineImage_path=Image.open('C:/Users/121mo/OneDrive/Desktop/hospital/full project/iamge/medicin.jpg')
medicineImageTk=ImageTk.PhotoImage(medicineImage_path)
#medicin lbl
medicinlbl=Label(userpage,image=medicineImageTk)
medicinlbl.place(relx=0.6,rely=0.15)
#medicin text lbl
medicinTextlbl=Label(userpage,text='Buy medicine',font=('Arial',18,'bold'),fg="#0077b6")
medicinTextlbl.place(relx=0.6,rely=0.119)
#medicin btn
medicin_btn=Button(userpage,text='Buy now',font=('Arial',13,'bold'),width=39,bg='#48cae4',fg='white')
medicin_btn.place(relx=0.6,rely=0.63)




















userpage.mainloop()
from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# MAin page

main = Tk()
window_width = 500
window_height = 500

w=main.winfo_screenwidth()
h=main.winfo_screenheight()
center_x = int(w/2 - window_width/2)
center_y = int(h/2 - window_height/2)

main.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
main.title("Log-in")
main.resizable(False, False)
main.configure(bg='#cb997e')
main.iconbitmap('C:/Users/121mo/OneDrive/Desktop/hospital/iamge/hospital-building.ico')
#Image
img = Image.open('D:/imaaaaaaaage/2150896634.jpg')
imgTK = ImageTk.PhotoImage(img)


lbl = Label(main, image=imgTK)
lbl.place(relwidth=1, relheight=1.2)


# main lable
lbl1 = Label(main, text="Creating New Account", font=("Arial", 20, "bold"), fg='#3a0ca3', bg='#48cae4', pady=10, padx=10, relief="solid", bd=2)
lbl1.grid(row=0, column=0, columnspan=4, pady=20, sticky="nsew")

# Frame
frame = Frame(main, bg='')
frame.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=20)

# First Name
Fname = Label(frame, text='First Name', font=("Arial", 10, "bold"), bg='#48cae4', fg='#3a0ca3', pady=5, padx=5, relief="ridge", bd=2)
Fname.grid(row=1, column=0, pady=5, padx=5, sticky="w")


FnameVar=StringVar()
FnameEnt = Entry(frame,textvariable=FnameVar)
FnameEnt.grid(row=1, column=1, pady=5, padx=5)

# Last Name
Lname = Label(frame, text='Last Name', font=("Arial", 10, "bold"), bg='#48cae4', fg='#3a0ca3', pady=5, padx=5, relief="ridge", bd=2)
Lname.grid(row=1, column=2, pady=5, padx=5, sticky="w")
LnameEnt = Entry(frame)
LnameEnt.grid(row=1, column=3, pady=5, padx=5)

# Email
Email = Label(frame, text='Email', font=("Arial", 10, "bold"), bg='#48cae4', fg='#3a0ca3', pady=5, padx=5, relief="ridge", bd=2)
Email.grid(row=2, column=0, pady=5, padx=5, sticky="w")
EmailEnt = Entry(frame, width=40)
EmailEnt.grid(row=2, column=1, columnspan=3, pady=5, padx=5, sticky="ew")

# Password
Password = Label(frame, text="Password", font=("Arial", 10, "bold"), bg='#48cae4', fg='#3a0ca3', pady=5, padx=5, relief="ridge", bd=2)
Password.grid(row=3, column=0, pady=5, padx=5, sticky="w")

passvar=StringVar()

PassEnt = Entry(frame, show='*', width=20,textvariable=passvar)
PassEnt.grid(row=3, column=1, pady=5, padx=5, sticky="w")

# Confirmation
Confirm = Label(frame, text='Confirmation', font=("Arial", 10, "bold"), bg='#48cae4', fg='#3a0ca3', pady=5, padx=5, relief="ridge", bd=2)
Confirm.grid(row=3, column=2, pady=5, padx=5, sticky="w")

confirmvar=StringVar()
ConfirmEnt = Entry(frame, show='*', width=20,textvariable=confirmvar)
ConfirmEnt.grid(row=3, column=3, pady=5, padx=5, sticky="w")
#Check password
def Check_password():
    RealPass=passvar.get()
    Confirmpass=confirmvar.get()
    policy1=ChekckVar1.get()
    if policy1==False and RealPass==Confirmpass=='':
        messagebox.showerror('log in','Please enter your password and confirm the Plotical conditions.')
    elif policy1==True and RealPass=='' or Confirmpass=='' :
        messagebox.showerror('log in','Make sure to write the password or confirmation')
    elif policy1==True and RealPass!=Confirmpass:
       messagebox.showerror('log in','Password does not match')
    elif RealPass==Confirmpass and policy1==False:
        messagebox.showerror('log in','Please check the political terms.')
    elif RealPass!=Confirmpass and policy1==False:
        messagebox.showerror('log in','Check passwoer and political terms.')
    else:
        messagebox.showinfo('log in','The account was created successfully.')


# Gender
GenderVar=StringVar()
GenderVar.set('M')

Gender = Label(frame, text='Gender', font=("Arial", 10, "bold"), bg='#48cae4', fg='#3a0ca3', pady=5, padx=5, relief="ridge", bd=2)
Gender.grid(row=4, column=0, pady=5, padx=5, sticky="w")
Genderbtn1 = Radiobutton(frame, text='Male', font=("Arial", 8, "bold"), bg='#90e0ef', selectcolor='#f0efeb',value="M",variable=GenderVar)
Genderbtn1.grid(row=4, column=1, pady=5, padx=5, sticky="w")
Genderbtn2 = Radiobutton(frame, text="Female", font=("Arial", 8, "bold"), bg='#90e0ef', selectcolor='#f0efeb',value="F",variable=GenderVar)
Genderbtn2.grid(row=4, column=2, pady=5, padx=5, sticky="w")

# Pricing Plan
PricingVar=StringVar()
PricingVar.set('T')
Pricing_plan = Label(frame, text='Pricing Plan', font=("Arial", 10, "bold"), bg='#48cae4', fg='#3a0ca3', pady=5, padx=5, relief="ridge", bd=2)
Pricing_plan.grid(row=5, column=0, pady=5, padx=5, sticky="w")
Pricing_planbtn1 = Radiobutton(frame, text='Trial', font=("Arial", 8, "bold"), bg='#90e0ef', selectcolor='#f0efeb',variable=PricingVar,value='T')
Pricing_planbtn1.grid(row=5, column=1, pady=5, padx=5, sticky="w")
Pricing_planbtn2 = Radiobutton(frame, text='Silver', font=("Arial", 8, "bold"), bg='#90e0ef', selectcolor='#f0efeb',variable=PricingVar,value='S')
Pricing_planbtn2.grid(row=5, column=2, pady=5, padx=5, sticky="w")
Pricing_planbtn3 = Radiobutton(frame, text='Gold', font=("Arial", 8, "bold"), bg='#90e0ef', selectcolor='#f0efeb',variable=PricingVar,value='G')
Pricing_planbtn3.grid(row=5, column=3, pady=5, padx=5, sticky="w")

# Country
Country = Label(frame, text='Country', font=("Arial", 10, "bold"), bg='#48cae4', fg='#3a0ca3', pady=5, padx=5, relief="ridge", bd=2)
Country.grid(row=6, column=0, pady=5, padx=5, sticky="w")
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",
    "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the",
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
    "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France",
    "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
    "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South",
    "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
    "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
    "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar",
    "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway",
    "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland",
    "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
    "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria",
    "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
    "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu",
    "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

countryVar = StringVar()
countryVar.set('Afghanistan')
CountryComb = Combobox(frame, width=40, values=countries, textvariable=countryVar, state='readonly')
CountryComb.grid(row=6, column=1, columnspan=3, pady=5, padx=5, sticky="ew")

# Checkbuttons
ChekckVar1=BooleanVar()
check = Checkbutton(frame, text=" I would like to receive news by email", font=("Arial", 8, "bold"), bg='#48cae4')
check.grid(row=7, column=0, columnspan=4, pady=5, padx=5, sticky="w")

check2 = Checkbutton(frame, text="I agree to the privacy policy", font=("Arial", 8, "bold"), bg='#48cae4',variable=ChekckVar1)
check2.grid(row=8, column=0, columnspan=4, pady=5, padx=5, sticky="w")

# Create Account Button
CreateAcc = Button(main, text="Create Account", font=('Arial', 15, 'bold'), fg='#ffffff', bg='#00b4d8', width=20, height=2,command=Check_password)
CreateAcc.grid(row=9, column=0, columnspan=4, pady=20)

main.mainloop()

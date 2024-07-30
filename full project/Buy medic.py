from tkinter import *
from tkinter import messagebox 
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview

# Sample medicine data
medicines = [
    {"name": "Paracetamol", "category": "Pain Relief", "price": 5},
    {"name": "Aspirin", "category": "Pain Relief", "price": 8},
    {"name": "Amoxicillin", "category": "Antibiotic", "price": 12},
    {"name": "Ciprofloxacin", "category": "Antibiotic", "price": 15},
    {"name": "Loratadine", "category": "Antihistamine", "price": 10},
    {"name": "Cetirizine", "category": "Antihistamine", "price": 9},
    {"name": "Ibuprofen", "category": "Pain Relief", "price": 7},
    {"name": "Azithromycin", "category": "Antibiotic", "price": 18},
    {"name": "Paracetamol", "category": "Pain Relief", "price": 5},
    {"name": "Aspirin", "category": "Pain Relief", "price": 8},
    {"name": "Amoxicillin", "category": "Antibiotic", "price": 12},
    {"name": "Ciprofloxacin", "category": "Antibiotic", "price": 15},
    {"name": "Loratadine", "category": "Antihistamine", "price": 10},
    {"name": "Cetirizine", "category": "Antihistamine", "price": 9},
    {"name": "Ibuprofen", "category": "Pain Relief", "price": 7},
    {"name": "Azithromycin", "category": "Antibiotic", "price": 18}
]

# Filtered medicine data
filtered_medicines = medicines.copy()

# Function to update the treeview with filtered data
def update_treeview():
    for row in treeview.get_children():
        treeview.delete(row)
    for med in filtered_medicines:
        treeview.insert("", END, values=(med['name'], med['category'], med['price']))

# Function to filter medicines
def filter_medicines():
    global filtered_medicines
    category = category_var.get()
    name = name_var.get().lower()

    # Initialize the filtered_medicines list
    filtered_medicines = []

    # Loop through the medicines list and apply the filter conditions
    for med in medicines:
        if (category == "All" or category == med["category"]) and name in med["name"].lower():
            filtered_medicines.append(med)

    update_treeview()


# Main window

buy_med_window = Tk()
buy_med_window.title("Medicine Purchase")
width = 700
height = 467
get_height = buy_med_window.winfo_screenheight()
get_width = buy_med_window.winfo_screenwidth()

Center_height = int((get_height - height) / 2)
Center_width = int((get_width - width) / 2)

buy_med_window.geometry(f'{width}x{height}+{Center_width}+{Center_height}')
buy_med_window.iconbitmap("iamge/hospital-building.ico")

#image
imagee=Image.open('C:/Users/121mo/OneDrive/Desktop/hospital/full project/iamge/medicinnn.jpg')
imageTkk=ImageTk.PhotoImage(imagee)
lbl=Label(buy_med_window,image=imageTkk)
lbl.place(relx=0,rely=0)
#label
title_label = Label(buy_med_window, text="Buy Medicine", font=("Arial", 20, "bold"),background='#ade8f4' )
title_label.grid(row=0, column=0,columnspan=4)
# Filter 
filter_frame=Frame(buy_med_window,bg='')
filter_frame.grid(row=1, column=0,columnspan=4, pady=10)

category_lbl=Label(filter_frame, text="Category:",bg='#ade8f4')
category_lbl.grid(row=0, column=0, padx=5)
category_var = StringVar(value="All")
category_combobox = Combobox(filter_frame, textvariable=category_var, state="readonly")
category_combobox["values"] = ["All", "Pain Relief", "Antibiotic", "Antihistamine"]
category_combobox.grid(row=0, column=1, padx=5)

med_label=Label(filter_frame, text="Name:",bg='#ade8f4')
med_label.grid(row=1, column=0, padx=5)
name_var = StringVar()
name_entry = Entry(filter_frame, textvariable=name_var)
name_entry.grid(row=1, column=1, padx=5)

filter_button = Button(filter_frame, text="Filter",command=filter_medicines,bg='#48cae4')
filter_button.grid(row=2, column=0, columnspan=3, pady=5)

#treeview
treeview_frame = Frame(buy_med_window)
treeview_frame.grid(row=2, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

treeview = Treeview(treeview_frame, columns=("name", "category", "price"), show="headings")
treeview.column('name', width=50, anchor="center")
treeview.column('category', width=200, anchor="center")
treeview.column('price', width=100, anchor="center")
treeview.heading("name", text="Name")
treeview.heading("category", text="Category")
treeview.heading("price", text="Price")
treeview.grid(row=0, column=0, sticky="nsew")

scrollbar = Scrollbar(treeview_frame, orient=VERTICAL, command=treeview.yview)
treeview.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')
treeview_frame.grid_rowconfigure(0, weight=1)
treeview_frame.grid_columnconfigure(0, weight=1)

# Buy button
buy_button = Button(buy_med_window, text="Buy Medicine",bg='#48cae4')
buy_button.grid(row=3, column=0, columnspan=4, pady=10)

buy_med_window.grid_columnconfigure(0, weight=1)
buy_med_window.grid_columnconfigure(1, weight=1)
buy_med_window.grid_columnconfigure(2, weight=1)
buy_med_window.grid_rowconfigure(2, weight=1)
update_treeview()


buy_med_window.mainloop()
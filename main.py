import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accepted = accept_var.get()

    if (accepted)=="Accepted":
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        print("firstname: ", firstname, "Lastname: ", lastname)

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            print("title: ", title, "age: ", age, "nationality: ", nationality)
            
            registration_status = registered_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemsters_spinbox.get()
            print("Registration: ", registration_status, "Courses: ", numcourses, "Semesters: ", numsemesters)
            print("Terms accepted:", accepted)
        else:
            tkinter.messagebox.showwarning(title = "Error", message = "Please enter first and last name.")
            print("Error, no name entry")
            

    else:
        tkinter.messagebox.showwarning(title = "Error", message = "Please accept the terms.")
        print("Error, terms not accepted")

    print("--------------------------------------------------")
window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx = 20, pady = 20)

first_name_label = tkinter.Label(user_info_frame, text = "First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text = "First Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values = ["", "Mr.", "Ms."])
title_label.grid(row = 0, column = 2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row = 2, column = 0)
age_spinbox.grid(row = 3, column = 0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values = ["American", "Mexican", "Asian"])
nationality_label.grid(row = 2, column = 1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

##Saving course info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)


registered_label = tkinter.Label(courses_frame, text ="Registration Status")

registered_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text ="Currently Registered",
                                 variable=registered_var, onvalue="Registered", offvalue="Not registered")

registered_label.grid(row = 0, column = 0)
registered_check.grid(row=1, column=0)

numcources_label = tkinter.Label(courses_frame, text="Completed Course")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcources_label.grid(row = 0, column = 1)
numcourses_spinbox.grid(row=1, column=1)

numsemsters_label = tkinter.Label(courses_frame, text="Semesters")
numsemsters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numsemsters_label.grid(row = 0, column = 2)
numsemsters_spinbox.grid(row=1, column=2)


for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

##Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

accept_var = tkinter.StringVar(value = "Not accepted")
terms_check = tkinter.Checkbutton(terms_frame, text ="I accept",
                                  variable=accept_var, onvalue="Accepted", offvalue = "Not accepted")
terms_check.grid(row=0, column=0)

##button
button = tkinter.Button(frame,text="Enter data", command = enter_data)
button.grid(row=3, column = 0, sticky = "news", padx = 20, pady = 10)
window.mainloop()


# 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
import datetime
from tkinter import *
from PIL import ImageTk, Image
from database import *
import tksheet

welcomeLabel = None
login_button = None
register_button = None
label1 = None
label2 = None
label3 = None
label4 = None
submit_button = None
username_entry = None
password_entry = None
gender_entry, email_entry, userid_entry, postcode_entry, phonenumber_entry, address_entry = None, None, None, None, None, None


def reset():
    global welcomeLabel, login_button, register_button, label3, label4, label1, label2, submit_button, password_entry, username_entry
    global gender_entry, email_entry, userid_entry, postcode_entry, phonenumber_entry, address_entry
    all_variable = [welcomeLabel, login_button, register_button, label3, label4,
                    label1, label2, submit_button, address_entry, password_entry,
                    username_entry, gender_entry, email_entry, userid_entry,
                    phonenumber_entry, postcode_entry]
    for var in all_variable:
        if var is not None:
            var.destroy()


def register_user(*args, **kwargs):
    global main_screen, welcomeLabel, login_button, register_button, label3, label4, label1, label2, submit_button, password_entry, username_entry
    global gender_entry, email_entry, userid_entry, postcode_entry, phonenumber_entry, address_entry
    raw_password = password_entry.get()
    username = username_entry.get()
    gender = gender_entry.get()
    phonenumber = phonenumber_entry.get()
    email = email_entry.get()
    postalcode = postcode_entry.get()
    userid = userid_entry.get()
    address = address_entry.get()
    reset()
    sucess, msg = customer_db.add_user(name=username,
                                       gender=gender, phonenumber=phonenumber,
                                       email=email, address=address,
                                       postalcode=postalcode,
                                       userid=userid, password=raw_password)
    if sucess:
        msg = f'Customer ID is:- {msg}'
    label1 = Label(main_screen, text=msg, bg="black", fg="white", font=('Helvetica', 16, 'bold'))
    label1.place(relx=0.54, rely=0.26, anchor='ne')

    login_button = Button(text="Login", bg="black", fg='white', height="2", width="20", command=login)
    login_button.place(relx=0.33, rely=0.80, anchor='ne')

    # Label(text="")
    register_button = Button(text="Register", bg="black", fg='white', height="2", width="20", command=register)
    register_button.place(relx=0.73, rely=0.80, anchor='ne')


def register():
    global main_screen, welcomeLabel, login_button, register_button, label3, label4, label1, label2, submit_button, password_entry, username_entry
    global gender_entry, email_entry, userid_entry, postcode_entry, phonenumber_entry, address_entry
    reset()
    welcomeLabel = Label(text="Please Enter the information below", bg="black", fg="white",
                         font=('Helvetica', 18, 'bold'))
    welcomeLabel.place(relx=0.30, rely=0.05, anchor='nw')
    label1 = Label(main_screen, text="Username", bg="black", fg="white", font=('Helvetica', 10, 'bold'))
    label1.place(relx=0.34, rely=0.1, anchor='ne')

    username_entry = Entry(width=25, fg="black", font="bold", )
    username_entry.place(relx=0.68, rely=0.1, anchor='ne')
    username_entry.focus()

    label2 = Label(main_screen, text="Password", bg="black", fg="white", font=('Helvetica', 10, 'bold'))
    label2.place(relx=0.34, rely=0.2, anchor='ne')
    bullet = "\u2022"
    password_entry = Entry(width=25, fg="black", font="bold", show=bullet)
    password_entry.place(relx=0.68, rely=0.2, anchor='ne')

    label3= Label(main_screen, text="Gender", bg="black", fg="white", font=('Helvetica', 10, 'bold'))
    label3.place(relx=0.34, rely=0.3, anchor='ne')
    gender_entry = Entry(width=25, fg="black", font="bold")
    gender_entry.place(relx=0.68, rely=0.3, anchor='ne')

    label4 = Label(main_screen, text="Phone Number", bg="black", fg="white", font=('Helvetica', 10, 'bold'))
    label4.place(relx=0.34, rely=0.56, anchor='ne')
    phonenumber_entry = Entry(width=25, fg="black", font="bold")
    phonenumber_entry.place(relx=0.68, rely=0.55, anchor='ne')

    label5 = Label(main_screen, text="Postal Code", bg="black", fg="white", font=('Helvetica', 10, 'bold'))
    label5.place(relx=0.34, rely=0.56, anchor='ne')
    postcode_entry = Entry(width=25, fg="black", font="bold")
    postcode_entry.place(relx=0.68, rely=0.55, anchor='ne')

    label6 = Label(main_screen, text="User ID", bg="black", fg="white", font=('Helvetica', 10, 'bold'))
    label6.place(relx=0.34, rely=0.56, anchor='ne')
    userid_entry = Entry(width=25, fg="black", font="bold")
    userid_entry.place(relx=0.68, rely=0.55, anchor='ne')

    label7 = Label(main_screen, text="Address", bg="black", fg="white", font=('Helvetica', 10, 'bold'))
    label7.place(relx=0.34, rely=0.56, anchor='ne')
    address_entry = Entry(width=25, fg="black", font="bold")
    address_entry.place(relx=0.68, rely=0.55, anchor='ne')

    submit_button = Button(text="Register", bg="black", fg='white', font=('Helvetica', 8, 'bold'), width=20, height=1,
                           command=register_user)
    submit_button.place(relx=0.68, rely=0.75, anchor='nw')


def login_user(*args, **kwargs):
    global main_screen, welcomeLabel, login_button, register_button, label3, label4, label1, label2, submit_button, password_entry, username_entry
    name = username_entry.get()
    password = password_entry.get()
    if name == 'admin' and password == 'admin':
        main_screen.destroy()
        from admin import admin_screen

    sucess = customer_db.fetch_user(name, password)
    reset()
    if sucess:
        main_screen.destroy()
        from user import user_screen
    else:
        print('Wrong username or password')
        label1 = Label(main_screen, text=msg, bg="black", fg="white", font=('Helvetica', 16, 'bold'))
        label1.place(relx=0.54, rely=0.36, anchor='ne')
    
    login_button = Button(text="Login", bg="black", fg='white', height="2", width="30", command=login)
    login_button.place(relx=0.63, rely=0.35, anchor='ne')

    register_button = Button(text="Register", bg="black", fg='white', height="2", width="30", command=register)
    register_button.place(relx=0.63, rely=0.55, anchor='ne')

def login():
    global main_screen, welcomeLabel, login_button, register_button, label3, label4, label1, label2, submit_button, password_entry, username_entry
    reset()

    welcomeLabel = Label(text="Please Enter the information below", bg="black", fg="white",
                         font=('Helvetica', 18, 'bold'))
    welcomeLabel.place(relx=0.26, rely=0.3, anchor='nw')

    label1 = Label(main_screen, text="Name", bg="black", fg="white", font=('Helvetica', 10, 'bold'))
    label1.place(relx=0.34, rely=0.46, anchor='ne')

    username_entry = Entry(width=25, fg="black", font="bold", )
    username_entry.place(relx=0.68, rely=0.45, anchor='ne')

    label2 = Label(main_screen, text="Password", bg="black", fg="white", font=('Helvetica', 10, 'bold'))
    label2.place(relx=0.34, rely=0.56, anchor='ne')
    bullet = "\u2022"
    password_entry = Entry(width=25, fg="black", font="bold", show=bullet)
    password_entry.place(relx=0.68, rely=0.55, anchor='ne')

    submit_button = Button(text="Login", bg="black", fg='white', font=('Helvetica', 8, 'bold'), width=20, height=1,
                           command=login_user)
    submit_button.place(relx=0.68, rely=0.75, anchor='nw')


main_screen = Tk()
main_screen.title("Account Login")
main_screen.resizable(False, False)
main_screen.configure(bg='black')

canvas = Canvas(main_screen, width=900, height=550)
img = (Image.open("back2.jpg"))

# Resize the Image using resize method
resized_image = img.resize((900, 550), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

# Add image to the Canvas Items
canvas.create_image(0, 0, anchor=NW, image=new_image)
canvas.pack()

welcomeLabel = Label(text="Please Choose any one options", bg='white', fg="black",
                     font=('Helvetica', 16, 'bold'))
welcomeLabel.place(relx=0.31, rely=0.03, anchor='nw')

login_button = Button(text="Login", fg="black", bg='white', height="2", width="30", command=login)
login_button.place(relx=0.63, rely=0.35, anchor='ne')

register_button = Button(text="Register", fg="black", bg='white', height="2", width="30", command=register)
register_button.place(relx=0.63, rely=0.55, anchor='ne')
main_screen.mainloop()

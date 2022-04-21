from tkinter import *
from PIL import ImageTk, Image
import pdb
from database import *
import tksheet

label_one = None
label_two = None
label_three = None
label_four = None
input_1 = None
input_2 = None
input_3 = None
input_4 = None
listbox = None
button_ = None
label_five, input_5, label_six, input_6, label_seven, input_7 = None, None, None, None, None, None
add_dress_button, show_dress_button, show_booking_button, show_customer_button, remove_dress_button, cancle_booking_button = None, None, None, None, None, None

label_eight, input_8 = None, None


def reset_variable():
    global label_one, label_two, input_2, input_1, listbox, label_three, input_3, label_four, input_4, add_dress_button, add_dress_button, remove_dress_button
    global label_five, input_5, label_six, input_6, label_seven, input_7, show_dress_button, show_booking_button, show_customer_button, cancle_booking_button
    global label_eight, input_8, button_
    all_element = [label_one, label_two, input_2, input_1, listbox, label_three, input_3, label_four, input_4,
                   add_dress_button, show_dress_button, show_booking_button, show_customer_button, label_eight, input_8,
                   cancle_booking_button, remove_dress_button, button_]
    for single_element in all_element:
        if single_element is not None:
            single_element.destroy()


def add_dress_(*args, **kwargs):
    global input_8, input_2, input_1, input_3, input_4, input_5, input_6, input_7, button_, label_one
    category_id = int(input_1.get())
    size = input_2.get()
    storeid = int(input_3.get())
    Name = input_4.get()
    Ideal_For = input_5.get()
    Rental_Rate = float(input_6.get())
    Description = input_7.get()
    color = input_8.get()
    values = {"storeid": storeid,
              "categoryid": category_id,
              "Name": Name,
              "size": size,
              "color": color,
              "idealfor": Ideal_For,
              "Rental_Rate": Rental_Rate,
              "Description": Description}
    for key, value in values.items():
        if isinstance(value, tuple) or isinstance(value, list):
            values[key] = value
    sucess, msg = dress_db.add_dress(**values)
    reset_variable()
    if sucess:
        msg = f'Dress id is {msg}'
    label_one = Label(admin_screen, text=msg, bg="black", fg="white", font=('Helvetica', 16, 'bold'))
    label_one.place(relx=0.54, rely=0.36, anchor='ne')
    button_ = Button(text="Back", bg="white", font=('Helvetica', 8, 'bold'), width=30, height=3,
                     command=run_admin_screen)
    button_.place(relx=0.68, rely=0.90, anchor='nw')


def add_dress():
    global label_one, label_two, input_2, input_1, label_three, input_3, input_4, label_four, admin_screen
    global label_five, input_5, label_six, input_6, label_seven, input_7, label_eight, input_8
    reset_variable()
    ##
    label_one = Label(admin_screen, text="CategoryID", bg="white", fg="violet red", font=('Helvetica', 12, 'bold'))
    label_one.place(relx=0.34, rely=0.16, anchor='ne')

    input_1 = Entry(width=25, fg="black", font="bold", )
    input_1.place(relx=0.68, rely=0.15, anchor='ne')
    input_1.focus_set()

    ##
    label_two = Label(admin_screen, text="Size", bg="white", fg="violet red",
                      font=('Helvetica', 12, 'bold'))
    label_two.place(relx=0.34, rely=0.26, anchor='ne')

    input_2 = Entry(width=25, fg="black", font="bold", )
    input_2.place(relx=0.68, rely=0.25, anchor='ne')
    ##
    label_three = Label(admin_screen, text="StoreID", bg="white", fg="violet red", font=('Helvetica', 12, 'bold'))
    label_three.place(relx=0.34, rely=0.36, anchor='ne')

    input_3 = Entry(width=25, fg="black", font="bold", )
    input_3.place(relx=0.68, rely=0.35, anchor='ne')
    ##
    label_four = Label(admin_screen, text="Name", bg="white", fg="violet red", font=('Helvetica', 12, 'bold'))
    label_four.place(relx=0.34, rely=0.46, anchor='ne')

    input_4 = Entry(width=25, fg="black", font="bold", )
    input_4.place(relx=0.68, rely=0.45, anchor='ne')
    ##
    label_five = Label(admin_screen, text="Ideal_For", bg="white", fg="violet red", font=('Helvetica', 12, 'bold'))
    label_five.place(relx=0.34, rely=0.56, anchor='ne')

    input_5 = Entry(width=25, fg="black", font="bold", )
    input_5.place(relx=0.68, rely=0.55, anchor='ne')
    ##
    label_six = Label(admin_screen, text="Rental_Rate", bg="white", fg="violet red", font=('Helvetica', 12, 'bold'))
    label_six.place(relx=0.34, rely=0.66, anchor='ne')

    input_6 = Entry(width=25, fg="black", font="bold", )
    input_6.place(relx=0.68, rely=0.65, anchor='ne')
    ##
    label_seven = Label(admin_screen, text="Description", bg="white", fg="violet red", font=('Helvetica', 12, 'bold'))
    label_seven.place(relx=0.34, rely=0.76, anchor='ne')

    input_7 = Entry(width=25, fg="black", font="bold", )
    input_7.place(relx=0.68, rely=0.75, anchor='ne')

    label_eight = Label(admin_screen, text="Color", bg="white", fg="violet red", font=('Helvetica', 12, 'bold'))
    label_eight.place(relx=0.34, rely=0.86, anchor='ne')

    input_8 = Entry(width=25, fg="black", font="bold", )
    input_8.place(relx=0.68, rely=0.85, anchor='ne')

    button_ = Button(text="Submit", bg="white", font=('Helvetica', 8, 'bold'), width=30, height=3,
                     command=add_dress_)
    button_.place(relx=0.68, rely=0.90, anchor='nw')
    # pdb.set_trace()
    admin_screen.bind('<Return>', add_dress_)


def remove_dress_(*args, **kwargs):
    global input_1, label_one, button_
    bookingid = input_1.get()
    reset_variable()
    sucesss = dress_db.delete_dress(bookingid)
    if sucesss:
        msg = "Deleted the dress"
    else:
        msg = 'Cannot delete the dress. Contact Developer'
    label_one = Label(admin_screen, text=msg, bg="black", fg="white", font=('Helvetica', 16, 'bold'))
    label_one.place(relx=0.54, rely=0.36, anchor='ne')
    button_ = Button(text="Back", bg="white", font=('Helvetica', 8, 'bold'), width=30, height=3,
                     command=run_admin_screen)
    button_.place(relx=0.68, rely=0.90, anchor='nw')


def remove_dress():
    global label_one, label_two, input_2, input_1, label_three, input_3, button_
    reset_variable()
    ##
    label_one = Label(admin_screen, text="DressId", bg="white", fg="violet red", font=('Helvetica', 12, 'bold'))
    label_one.place(relx=0.34, rely=0.16, anchor='ne')

    input_1 = Entry(width=25, fg="black", font="bold", )
    input_1.place(relx=0.68, rely=0.15, anchor='ne')
    button_ = Button(text="Delete", bg="white", font=('Helvetica', 8, 'bold'), width=30, height=3,
                     command=remove_dress_)
    button_.place(relx=0.68, rely=0.85, anchor='nw')
    admin_screen.bind('<Return>', remove_dress_)


def cancel_booking_(*args, **kwargs):
    global input_1, label_one, button_
    bookingid = input_1.get()
    reset_variable()
    sucesss = book_db.delete_booking(bookingid)
    if sucesss:
        msg = "Booking is Cancel"
    else:
        msg = 'Cannot Cancel the booking. Contact Developer'
    label_one = Label(admin_screen, text=msg, bg="black", fg="white", font=('Helvetica', 16, 'bold'))
    label_one.place(relx=0.54, rely=0.36, anchor='ne')
    button_ = Button(text="Back", bg="white", font=('Helvetica', 8, 'bold'), width=30, height=3,
                     command=run_admin_screen)
    button_.place(relx=0.68, rely=0.90, anchor='nw')


def cancle_booking():
    global label_one, input_1, button_
    reset_variable()
    ##
    label_one = Label(admin_screen, text="BookingID", bg="white", fg="violet red", font=('Helvetica', 12, 'bold'))
    label_one.place(relx=0.34, rely=0.16, anchor='ne')

    input_1 = Entry(width=25, fg="black", font="bold", )
    input_1.place(relx=0.68, rely=0.15, anchor='ne')
    button_ = Button(text="Cancle", bg="white", font=('Helvetica', 8, 'bold'), width=30, height=3,
                     command=cancel_booking_)
    button_.place(relx=0.68, rely=0.85, anchor='nw')
    admin_screen.bind('<Return>', cancel_booking_)


def table_creating(result):
    new_screen = Tk()
    height = min(len(result) * 30, 1200)
    new_screen.geometry(f"800x{height}")
    new_screen.title("Store")
    sheet = tksheet.Sheet(new_screen, width=1200, height=height, headers=result[0])
    sheet.grid()
    sheet.set_sheet_data(result[1:])


def fetch_dress():
    global label_one
    result = dress_db.fetch_dress()
    if len(result) > 0:
        result.insert(0, (
        "DressId", "StoreID", "CategoryID", "Name", "size", "color", "Ideal_For", "Rental_Rate", "Description"))
        table_creating(result)
    else:
        msg = 'No Dress Found'
        label_one = Label(admin_screen, text=msg, bg="black", fg="white", font=('Helvetica', 16, 'bold'))
        label_one.place(relx=0.54, rely=0.36, anchor='ne')


def fetch_booking():
    global label_one
    result = book_db.fetch_booking()
    if len(result) > 0:
        result.insert(0, ("BookingID", "CustomerID", "DressID", "Booking_Date", "Total_Amount", "Description"))
        table_creating(result)
    else:
        msg = 'No Booking Found'
        label_one = Label(admin_screen, text=msg, bg="black", fg="white", font=('Helvetica', 16, 'bold'))
        label_one.place(relx=0.54, rely=0.36, anchor='ne')


def fetch_customer():
    global label_one
    result = customer_db.fetch_all_user()
    if len(result) > 0:
        result.insert(0, (
        "CustomerID", "Name", "Gender", "PhoneNumber", "Email", "Address", "Postal_Code", "User_ID", "Password"))
        table_creating(result)
    else:
        msg = 'No Customer Found'

        label_one = Label(admin_screen, text=msg, bg="black", fg="white", font=('Helvetica', 16, 'bold'))
        label_one.place(relx=0.54, rely=0.36, anchor='ne')


def run_admin_screen():
    global show_dress_button, show_booking_button, show_customer_button, cancle_booking_button, add_dress_button, add_dress_button, remove_dress_button, admin_screen
    reset_variable()
    welcomeLabel = Label(text="WELCOME To Admin Panel", bg="white", fg="black", font=('Helvetica', 20, 'bold'))
    welcomeLabel.place(relx=0.28, rely=0.03, anchor='nw')
    # Dress
    add_dress_button = Button(text="Add Dress", bg="white", font=('Helvetica', 8, 'bold'), width=20, height=3,
                              command=add_dress)
    add_dress_button.place(relx=0.18, rely=0.50, anchor='nw')

    show_dress_button = Button(text="Show Dress", bg="white", font=('Helvetica', 8, 'bold'), width=20, height=3,
                               command=fetch_dress)
    show_dress_button.place(relx=0.43, rely=0.50, anchor='nw')

    remove_dress_button = Button(text="Remove Dress", bg="white", font=('Helvetica', 8, 'bold'), width=20, height=3,
                                 command=remove_dress)
    remove_dress_button.place(relx=0.68, rely=0.50, anchor='nw')

    # Booking
    show_booking_button = Button(text="Show Booking", bg="white", font=('Helvetica', 8, 'bold'), width=20, height=3,
                                 command=fetch_booking)
    show_booking_button.place(relx=0.18, rely=0.65, anchor='nw')

    cancle_booking_button = Button(text="Cancle Booking", bg="white", font=('Helvetica', 8, 'bold'), width=20, height=3,
                                   command=cancle_booking)
    cancle_booking_button.place(relx=0.43, rely=0.65, anchor='nw')

    # Customer
    show_customer_button = Button(text="Show Customer", bg="white", font=('Helvetica', 8, 'bold'), width=20, height=3,
                                  command=fetch_customer)
    show_customer_button.place(relx=0.68, rely=0.65, anchor='nw')


admin_screen = None


def run_screen():
    global admin_screen
    admin_screen = Tk()
    admin_screen.title("Admin Panel")

    canvas = Canvas(admin_screen, width=900, height=550)
    img = (Image.open("back3.jpg"))

    # Resize the Image using resize method
    resized_image = img.resize((900, 550), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)

    # Add image to the Canvas Items
    canvas.create_image(0, 0, anchor=NW, image=new_image)
    canvas.pack()

    admin_screen.resizable(False, False)
    admin_screen.configure(bg='black')
    run_admin_screen()
    admin_screen.mainloop()
    return admin_screen


admin_screen = run_screen()

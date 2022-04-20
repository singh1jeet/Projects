import datetime
from tkinter import *
from PIL import ImageTk, Image
from database import *
import tksheet
            
def table_creating(result):
    new_screen = Tk()
    new_screen.title("Store")
    sheet = tksheet.Sheet(new_screen)
    sheet.grid()
    sheet.set_sheet_data(result)

def get_customer():
    f = open('username.txt')
    customer_id = f.readline()[0]
    customer_id = int(customer_id)

    return customer_id

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
show_dress_button, book_dress_button, show_booking_button, user_screen = None,None,None,None


def reset_variable():
    global label_one, label_two, input_2, input_1, listbox, label_three, input_3, label_four, input_4, button_
    global show_dress_button, book_dress_button, show_booking_button
    all_element = [button_, label_one, label_two, input_2, input_1, listbox, label_three, input_3, label_four, input_4, show_dress_button, book_dress_button, show_booking_button]
    for single_element in all_element:
        if single_element is not None:
            single_element.destroy()

def book_dress_():
    global label_one, label_two, input_2, input_1, label_three, input_3, user_screen, button_
    customer_id = get_customer()
    dress_id = input_1.get()
    booking_date = str(datetime.date.today())
    total_amount = 1000
    Description = input_2.get()
    sucess, msg = book_db.book_dress(
        customerid=customer_id,
        dressid=dress_id,
        booking_date=booking_date,
        amount=total_amount,
        des=Description)
    reset_variable()
    if sucess:
        msg = 'Booking id is :' + msg
    print(msg)
    button_ = Button(text="Back", bg="white", font=('Helvetica', 8, 'bold'), width=30, height=3,
                     command=run_user_screen)
    button_.place(relx=0.68, rely=0.90, anchor='nw')


def book_dress():
    global label_one, label_two, input_2, input_1, label_three, input_3, button_
    reset_variable()
    label_one = Label(user_screen, text="DressId", bg="white", fg="violet red", font=('Helvetica', 12, 'bold'))
    label_one.place(relx=0.34, rely=0.16, anchor='ne')
    input_1 = Entry(width=25, fg="black", font="bold", )
    input_1.place(relx=0.68, rely=0.15, anchor='ne')
    input_1.focus_set()
    ##
    label_two = Label(user_screen, text="Description", bg="white", fg="violet red",
                      font=('Helvetica', 12, 'bold'))
    label_two.place(relx=0.34, rely=0.26, anchor='ne')

    input_2 = Entry(width=25, fg="black", font="bold", )
    input_2.place(relx=0.68, rely=0.25, anchor='ne')

    button_ = Button(text="Submit", bg="white", font=('Helvetica', 8, 'bold'), width=30, height=3,
                     command=book_dress_)
    button_.place(relx=0.68, rely=0.90, anchor='nw')
    # pdb.set_trace()
    user_screen.bind('<Return>', book_dress_)


def show_dress():
    global button_
    reset_variable()
    result = dress_db.fetch_dress()
    result.insert(0, ("DressId", "StoreID", "CategoryID","Name", "size", "color", "Ideal_For", "Rental_Rate", "Description"))
    table_creating(result)
    button_ = Button(text="Back", bg="white", font=('Helvetica', 8, 'bold'), width=30, height=3,
                     command=run_user_screen)
    button_.place(relx=0.68, rely=0.90, anchor='nw')


def show_booking():
    global button_
    reset_variable()
    customer_id = get_customer()
    result = book_db.fetch_customer_booking(customer_id)
    result.insert(0, ("BookingID", "CustomerID", "DressID","Booking_Date", "Total_Amount", "Description"))
    table_creating(result)
    button_ = Button(text="Back", bg="white", font=('Helvetica', 8, 'bold'), width=30, height=3,
                     command=run_user_screen)
    button_.place(relx=0.68, rely=0.90, anchor='nw')


def run_user_screen():
    global show_dress_button, book_dress_button, show_booking_button, user_screen, button_
    # Dress
    reset_variable()
    show_dress_button = Button(text="Show Dress", bg="white", font=('Helvetica', 8, 'bold'), width=20, height=3,
                               command=show_dress)
    show_dress_button.place(relx=0.18, rely=0.50, anchor='nw')

    book_dress_button = Button(text="Book Dress", bg="white", font=('Helvetica', 8, 'bold'), width=20, height=3,
                               command=book_dress)
    book_dress_button.place(relx=0.43, rely=0.50, anchor='nw')

    show_booking_button = Button(text="Show Booking", bg="white", font=('Helvetica', 8, 'bold'), width=20, height=3,
                                 command=show_booking)
    show_booking_button.place(relx=0.68, rely=0.50, anchor='nw')


def run_screen():
    user_screen = Tk()
    user_screen.title("Store")
    
    canvas = Canvas(user_screen, width=900, height=550)
    img = (Image.open("back1.jpg"))
    
    # Resize the Image using resize method
    resized_image = img.resize((900, 550), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    
    # Add image to the Canvas Items
    canvas.create_image(0, 0, anchor=NW, image=new_image)
    canvas.pack()
    
    user_screen.resizable(False, False)
    user_screen.configure(bg='black')
    run_user_screen()
    user_screen.mainloop()
    return user_screen

user_screen = run_screen()
    
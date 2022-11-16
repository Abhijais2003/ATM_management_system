from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import time
import sqlite3


with sqlite3.connect("options.db") as db:
    cursor = db.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS options(id INTEGER PRIMARY KEY AUTOINCREMENT, current_balance interger, Deposit_amount interger); """)


def Balance_Inquiry():
    global img1, entry
    Bal = Toplevel()
    Bal.title("Balance Inquiry")
    Bal.geometry("600x500")
    p1 = PhotoImage(file="Options/images/logo_python.png")
    Bal.iconphoto(False, p1)

    img1 = ImageTk.PhotoImage(Image.open("Options/images/money.jpeg"))
    Balance_label = Label(Bal, image=img1)
    Balance_label.place(x=0, y=0)

    Avaiable_balance = Label(
        Bal, text="Available Balance:- ", font=("Open Sans", 22), bg="pink")
    Avaiable_balance.place(x=10, y=100)

    entry = Entry(Bal, width=30)
    entry.focus_set()
    entry.place(x=300, y=105)

    button_bal = Button(Bal, text="Exit", relief="groove", height=2, width=20,
                        bg="pink", fg="Yellow", activeforeground="pink", activebackground="red", border="3", command=Bal.quit, font=("Helvetica", 12))
    button_bal.pack(pady=230)


def Deposit():

    global img1, entry_dop
    Dep = Toplevel()
    Dep.title("Balance Inquiry")
    Dep.geometry("600x500")

    p1 = PhotoImage(file="Options/images/logo_python.png")
    Dep.iconphoto(False, p1)

    Address = Image.open("Options/images/Deposit.jpeg")
    resize_img = Address.resize((600, 500))
    img1 = ImageTk.PhotoImage(resize_img)

    Balance_label = Label(Dep, image=img1)
    Balance_label.place(x=0, y=0)

    txt = Label(Dep, text="INPUT:-", font=("Sarif", 12), bg="#C29D66")
    txt.place(x=120, y=100)

    input_label = Label(Dep, text="", font=("Courier 30 bold", 15))
    input_label.place(x=0, y=0, height=50)

    entry_dop = Entry(Dep, width=30)
    entry_dop.focus_set()
    entry_dop.place(x=220, y=105)

    entry_dop.insert(0, "Enter the Amount in Rupees")

    button_ok = Button(Dep, text="Proceed", relief="groove", height=2, width=10,
                       bg="Blue", fg="Black", activeforeground="pink", activebackground="red", border="3", command=messageDeposit, font=("Helvetica", 8))
    button_ok.place(x=250, y=150)

    button_bal = Button(Dep, text="Exit", relief="groove", height=2, width=20,
                        bg="pink", fg="Yellow", activeforeground="pink", activebackground="red", border="3", command=Dep.quit, font=("Helvetica", 12))
    button_bal.place(x=200, y=400)


def Withdrawal():

    global img1, entry_with
    With = Toplevel()
    With.title("Balance Inquiry")
    With.geometry("600x500")

    p1 = PhotoImage(file="Options/images/logo_python.png")
    With.iconphoto(False, p1)

    Address = Image.open("Options/images/withdrawal.jpeg")
    resize_img = Address.resize((600, 500))
    img1 = ImageTk.PhotoImage(resize_img)
    Balance_label = Label(With, image=img1)
    Balance_label.place(x=0, y=0)

    txt = Label(With, text="INPUT:-", font=("Sarif", 12), bg="#C29D66")
    txt.place(x=120, y=100)

    input_label = Label(With, text="", font=("Courier 30 bold", 15))
    input_label.place(x=0, y=0, height=50)

    entry_with = Entry(With, width=30)
    entry_with.focus_set()
    entry_with.place(x=220, y=105)

    entry_with.insert(0, "Enter the Amount in Rupees")

    button_ok = Button(With, text="Proceed", relief="groove", height=2, width=10,
                       bg="Blue", fg="Black", activeforeground="pink", activebackground="red", border="3", command=message, font=("Helvetica", 8))
    button_ok.place(x=250, y=150)

    button_bal = Button(With, text="Exit", relief="groove", height=2, width=20,
                        bg="pink", fg="Yellow", activeforeground="pink", activebackground="red", border="3", command=With.quit, font=("Helvetica", 12))
    button_bal.place(x=200, y=400)


def message():
    messagebox.showinfo("CONGRATULATIONS !!!!!.",
                        "Withdrawling Money.......!!!!")


def messageDeposit():
    messagebox.showinfo("Wait !!!", "Depositing money !!!!!!!")


def PinChange():
    pass


def info():
    pass


def help():

    root = Toplevel()
    root.title("How to use it......")
    root.geometry("500x400")

    label1 = Label(
        root, text="This is just a simple ATM Management system created by ABhishek Jaiswal in this GUI you can sign-up through the main page and than login to use the ATM , and if i talk about the options module in the ATM where you can deposit, check your account balanced , withdrawal your money, there is one more module from where you can change the ATM pin..", font=("Arial", 10))
    label1.place(x=0, y=0)


def calculate():

    cal1 = entry_with.get()
    cal2 = entry_dop.get()
    cal3 = entry.get()

    cursor.execute(
        "SELECT COUNT(*) from options WHERE Deposit_amount= '" + cal2 + "' ")
    result = cursor.fetchone()

    cursor.execute("INSERT INTO current_balance Values")


window = Tk()
window.title("ATM")

window.geometry("600x500")

my_menu = Menu(window)
window.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="How to use", command=help)
file_menu.add_separator()
file_menu.add_command(label="Info", command=info)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

localtime = time.asctime(time.localtime(time.time()))

p1 = PhotoImage(file="Options/images/logo_python.png")
window.iconphoto(False, p1)


image = Image.open("Options/images/ATM.jpeg")
resize_img = image.resize((600, 500))
bg = ImageTk.PhotoImage(resize_img)


label1 = Label(window, image=bg)
label1.place(x=0, y=0)

label2 = Label(window,  text=localtime, fg="Powder Blue",
               background="black", bd=10, anchor="w", font=(
                   "Helvetica", 18))
label2.pack(pady=20)

label2 = Label(window,  text="Options", font=(
    "Helvetica", 22), foreground="black", bg="#BCAD9A")
label2.pack(pady=0)


# Button 1 "Balance_Inquiry"

button1 = Button(window, relief="groove",
                 text="Balance Inquiry", height=2, width=20, bg="Brown", fg="Yellow", activeforeground="pink", activebackground="red", border="3", command=Balance_Inquiry, font=(
                     "Helvetica", 12))
button1.pack(pady=20)
button1.place(x=30, y=300)


# Button 2 "Deposit"
button2 = Button(window, text="Deposit", relief="groove", height=2, width=20,
                 bg="Brown", fg="Yellow", activeforeground="pink", activebackground="red", border="3", command=Deposit, font=(
                     "Helvetica", 12))
button2.pack(pady=20)
button2.place(x=30, y=400)


# Button 3 "Withdrawal"
button3 = Button(window, text="Withdrawal",
                 relief="groove", height=2, width=20, bg="Brown", fg="Yellow", activeforeground="pink", activebackground="red", border="3", command=Withdrawal, font=(
                     "Helvetica", 12))
button3.pack(pady=20)
button3.place(x=380, y=400)

# Button 4 "PinChange"
button4 = Button(window, text="PinChange", relief="groove", height=2, width=20,
                 bg="Brown", fg="Yellow", activeforeground="pink", activebackground="red", border="3", command=PinChange, font=(
                     "Helvetica", 12))
button4.pack(pady=20)
button4.place(x=380, y=300)


# Database
# connect = sqlite3.connect("ATM.db")
# c = connect.cursor()
# c.execute("CREATE TABLE ATM  (Name TEXT, age INT, gen TEXT , money INT)")
# connect.commit()
# connect.close()

window.mainloop()

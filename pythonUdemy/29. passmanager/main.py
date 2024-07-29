from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
password_list = password_letters + password_numbers + password_symbols

def generatepassword():
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    passinput.delete(0,END)
    passinput.insert(END,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def saveinfo():
    info = [websiteinput.get(),userinp.get(),passinput.get()]

    if len(info[0]) < 2 or  len(info[1]) < 2 or len(info[2]) < 2:
        messagebox.showinfo(title="Entry empty",message=f"Please enter correct details")
    else:
        isok = messagebox.askokcancel(title=info[0], message=f"these are the details entered:\nEmail: {info[1]}\nPassword: {info[2]}\nIs it ok to save?")
        if isok:
            with open("passwordData.txt","a") as file:
                file.write(f"{info[0]} | {info[1]} | {info[2]}\n")
                websiteinput.delete(0,END)
                passinput.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
info = {}

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1, row=0)

websitelabel = Label(text="Website")
websitelabel.grid(row=1, column=0)

websiteinput = Entry(width=35)
websiteinput.grid(row=1, column=1, columnspan=2)
websiteinput.focus()

usernamelabel = Label(text="Email/Username")
usernamelabel.grid(row=2, column=0)

userinp = Entry(width=35,highlightthickness=0)
userinp.grid(row=2, column=1, columnspan=2)
userinp.insert(END,"gillolahemavardhanreddy@gmail.com")

passlabel = Label(text="Password:")
passlabel.grid(row=3, column=0)

passinput = Entry(width=21,highlightthickness=0)
passinput.grid(row=3, column=1)

generatebtn = Button(text="Generate Passsword",highlightthickness=0,bd=0,command=generatepassword)
generatebtn.grid(row=3, column=2)

addbtn = Button(text="Add",width=36,highlightthickness=0,bd=0,command=saveinfo)
addbtn.grid(row=4, column=1, columnspan=2)

window.mainloop()
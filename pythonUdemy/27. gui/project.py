from tkinter import *

def mtok():
    miles = float(inp.get())
    km = miles * 1.609
    kmresult.config(text=f"{km}")

window = Tk()
window.title("Miles To kilometer Converter")
window.config(padx=20, pady=20)

# row 1
inp = Entry(width=7)
inp.grid(column=1, row=0)

label = Label(text="Miles")
label.grid(column=2, row=0)

isequal = Label(text="is equal to")
isequal.grid(column=0, row=1)

kmresult = Label(text="0")
kmresult.grid(column=1, row=1)

kmlabel = Label(text="Km")
kmlabel.grid(column=2, row=1)

calbtn =  Button(text="Calculate",command=mtok)
calbtn.grid(column=1, row=2)


window.mainloop()
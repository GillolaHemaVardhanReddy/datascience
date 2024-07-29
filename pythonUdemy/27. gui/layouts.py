from tkinter import *
"""
    pack() : all pack does is to pack every widget next to each other by default pack starts from
            start os window and places other widgets below them
            position is changes using side parameter => side=left/right/bottom
            if side = left then it start every widget from left of the window placing all next to each other
            we cannot place widgets in particular position
    place(x=n,y=m) : we can place any widget in perfet position using x and y values
            this becomes a problem to place each and every widget using place so we use grid
    grid(column=n,row=m) : this grid when we place widget in particular row col 
            if we are placing widget in row 3 col 2 then if there no widgets in col 2 totally then it automatically
            places widget in row 3 col 0

    ** cannot use pack and grid at a time
"""



window = Tk()
window.title("Layouts in tkinter")
window.minsize(width=500,height=500)

# challenge
label = Label(text="Label")
label.grid(column=0,row=0)

btn1 = Button(text="button")
btn1.grid(column=2,row=0)

btn = Button(text="new button")
btn.grid(column=1,row=1)


entry = Entry()
entry.insert(END,"Entry")
entry.grid(row=2,column=3)


window.mainloop()
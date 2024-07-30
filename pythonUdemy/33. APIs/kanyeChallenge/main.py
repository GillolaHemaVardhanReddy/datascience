# --------------------------------------------- IMPORTS ----------------------------------------------- #
import requests as req
from tkinter import *

# --------------------------------------------- API DATA ----------------------------------------------- #
api = "https://api.kanye.rest"
def getquote():
    response = req.get(api)
    data = response.json()
    canvas.itemconfig(quote_text,text=data["quote"], font=("Arial", 20, "bold"))

# --------------------------------------------- GUI ----------------------------------------------- #

window = Tk()
window.title("Quotes by Kanye!")
window.config(padx=50, pady=50)

# --------------------------------------------- CANVAS ----------------------------------------------- #
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=getquote)
kanye_button.grid(row=1, column=0)

# --------------------------------------------- RUN WIDGET ----------------------------------------------- #
window.mainloop()
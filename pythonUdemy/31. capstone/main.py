# ------------------------------------ IMPORTS ----------------------------------- #
from tkinter import *
import pandas as pd
import random as rd
import time 

# ------------------------------------ CONSTANTS ----------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
IMAGE_WIDTH = 800
IMAGE_HEIGHT = 526
FLIP_TIME = 3000

# ------------------------------------ GUI ---------------------------------------- #

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ------------------------------------ csv ---------------------------------------- #
try:
    file = pd.read_csv("./data/learn.csv")
except FileNotFoundError as errmsg:
    file = pd.read_csv("./data/data.csv")
finally:
    tolearn = file.to_dict(orient="records")
curcard = {}

def flipcard():
    card.itemconfig(cardimage, image=card_back)
    card.itemconfig(cardtitle,text="English", fill="white")
    card.itemconfig(cardtext,text=curcard["English"], fill="white")

def nextcard():
    global curcard, fliptimer
    window.after_cancel(fliptimer)
    curcard = rd.choice(tolearn)
    card.itemconfig(cardtitle,text="French", fill="black")
    card.itemconfig(cardtext,text=curcard["French"], fill="black")
    card.itemconfig(cardimage, image=card_front)
    fliptimer = window.after(FLIP_TIME, func=flipcard)

def knowcard():
    tolearn.remove(curcard)
    df = pd.DataFrame(tolearn)
    df.to_csv("./data/learn.csv", index=False)
    nextcard()

# ------------------------------------ IMAGES ---------------------------------------- #
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

# ------------------------------------ CANVAS ---------------------------------------- #
card = Canvas(width=IMAGE_WIDTH, height=IMAGE_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
cardimage = card.create_image(IMAGE_WIDTH//2, 263, image=card_front)
cardtitle = card.create_text(IMAGE_WIDTH//2, 150, text="French", font=("Ariel", 40, "italic"))
cardtext = card.create_text(IMAGE_WIDTH//2, 263, text="Esparaso", font=("Ariel", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)
fliptimer = window.after(FLIP_TIME, func=flipcard)

# ------------------------------------ BUTTONS ----------------------------------------------- #
unknownbtn = Button(image=wrong, bg=BACKGROUND_COLOR, highlightthickness=0, command=nextcard)
unknownbtn.grid(row=1, column=0)

knownbtn = Button(image=right, bg=BACKGROUND_COLOR, highlightthickness=0, command=knowcard)
knownbtn.grid(row=1, column=1)

# ------------------------------------ START APPLICATION ----------------------------------- #
nextcard()
window.mainloop()
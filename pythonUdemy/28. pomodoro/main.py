from tkinter import *
import math 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def resettimer():
    window.after_cancel(timer)
    counter(0)
    label2.config(text="")
    label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    global reps 
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps&1 :
        label.config(text="Work",fg=GREEN)
        counter(WORK_MIN*60)
    elif reps==8:
        label.config(text="BREAK",fg=RED)
        counter(LONG_BREAK_MIN*60)
    else: 
        label.config(text="BREAK",fg=PINK)
        counter(SHORT_BREAK_MIN*60)
    reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def dynamictype(var):
    if var == 0 :
        var = "00"
    elif var < 10 :
        var = f"0{var}"
    else:
        var = f"{var}"
    return var
def counter(n):
    mini = math.floor(n / 60)
    sec = n % 60
    canvas.itemconfig(timer_text,text=f"{dynamictype(mini)}:{dynamictype(sec)}")
    if n>0:
        global timer
        timer = window.after(1000,counter,n-1)
    else:
        start_timer()
        checkmark = ""
        wsession = math.floor(reps/2)
        for _ in range(wsession):
            checkmark += "✔"
        label2.config(text=checkmark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

label = Label(text="Timer",bg=YELLOW,font=(FONT_NAME,50))
label.config(fg=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,32,"bold"))
canvas.grid(column=1, row=1)

startbtn = Button(text="Start", highlightthickness=0, bd=0,command=start_timer)
startbtn.grid(column=0, row=2)
resetbtn = Button(text="Reset", highlightthickness=0, bd=0,command=resettimer)
resetbtn.grid(column=2, row=2)

label2 = Label(text="",fg=GREEN,bg=YELLOW,font=("Areal",14))
label2.grid(column=1, row=3)

window.mainloop()
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz : QuizBrain ):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scorelabel = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.scorelabel.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.questiontext = self.canvas.create_text(150, 125, width=280, text="some question text", fill=THEME_COLOR, font=("Arial",12,"italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        trueimage = PhotoImage(file="images/true.png")
        self.truebutton = Button(image=trueimage, highlightthickness=0, command=self.answerTrue)
        self.truebutton.grid(row=2, column=0)

        falseimage = PhotoImage(file="images/false.png")
        self.falsebutton = Button(image=falseimage, highlightthickness=0, command=self.answerFalse)
        self.falsebutton.grid(row=2, column=1)

        self.changequestion()
        self.window.mainloop()

    def answerTrue(self):
        self.feedback(self.quiz.check_answer("True"))
    
    def answerFalse(self):
        self.feedback(self.quiz.check_answer("False"))
    
    def feedback(self, fb):
        if fb : self.canvas.config(bg="green")
        else: self.canvas.config(bg="red")  
        self.window.after(1000,self.changequestion)

    def changequestion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scorelabel.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questiontext, text=q_text)
        else:
            self.scorelabel.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.questiontext, text=f"You've reached the end of the quiz. score : {self.quiz.score}/{self.quiz.question_number}")
            self.truebutton.config(state="disabled")
            self.falsebutton.config(state="disabled")
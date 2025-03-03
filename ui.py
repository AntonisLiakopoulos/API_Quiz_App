THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import*
from main_window import OriginalWindow



class Interface(OriginalWindow):
    def __init__(self,quiz_brain: QuizBrain):
        super().__init__()
        self.window.withdraw()
        self.quiz = quiz_brain
        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text( 150,
            125,
            width=280,
            text="Welcome to Quizmania!",
            font=("Arial", 20),
            fill=THEME_COLOR)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.score_label = Label(text="score: 0",bg=THEME_COLOR,fg="white")
        self.score_label.grid(column=1,row=0,sticky="E")

        self.true_button_photo = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_photo,command=self.is_true)
        self.true_button.grid(column=0,row=2)

        self.false_button_photo = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_photo,command=self.is_false)
        self.false_button.grid(column=1,row=2)

        self.get_next_question()

        #self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="The quiz is finished")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def is_true(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)



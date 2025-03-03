from tkinter.ttk import Combobox

THEME_COLOR = "#375362"
from tkinter import*
from quiz_brain import QuizBrain
from question_model import Question
from data import get_data
from ui import Interface
from main_window import OriginalWindow

class WelcomePage(OriginalWindow):
    def __init__(self):
        super().__init__()
        self.difficulty = 0
        self.question_num = 0
        self.canvas = Canvas(bg="white", width=300, height=300)
        self.logo_image = PhotoImage(file="images/logo_2.png")
        self.canvas.create_image(150,150,image=self.logo_image)
        self.canvas.grid(column=1, row=0, pady=50)
        self.question_data = {}

        self.num_of_questions_options = (5,10,20,30,40)
        self.first_value =StringVar(value= "Choose number of questions")
        self.num_of_questions = Combobox(values= self.num_of_questions_options, textvariable=self.first_value, state="readonly")
        self.num_of_questions.grid(column=0,row=1,columnspan=2,sticky="EW",pady=10)
        self.num_of_questions.bind("<<ComboboxSelected>>", self.get_questions_number)


        self.difficulty_options = ("easy", "medium", "hard")
        self.selected_value = StringVar(value="Choose difficulty")
        self.difficulty_box = Combobox( values=self.difficulty_options, textvariable=self.selected_value, state="readonly")
        self.difficulty_box.grid(column=0,row=2,columnspan=2,sticky="EW",pady=10)
        self.difficulty_box.bind("<<ComboboxSelected>>", self.difficulty_selected)


        self.start_button = Button(text="Start_Quiz",command=self.begin_game)
        self.start_button.grid(column=1,row=3)

        self.window.mainloop()


    def difficulty_selected(self,event):
        self.difficulty = self.difficulty_box.get()
        return self.difficulty

    def get_questions_number(self,event):
        self.question_num = int(self.num_of_questions.get())
        self.question_data = get_data(self.question_num,self.difficulty)
        return self.question_data

    def begin_game(self):
        question_bank = []
        for question in self.question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        for widget in self.window.winfo_children():
            widget.destroy()
        quiz = QuizBrain(question_bank)
        ui = Interface(quiz)


WelcomePage()





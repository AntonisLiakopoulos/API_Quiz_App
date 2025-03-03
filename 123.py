self.easy = Radiobutton(text="Easy", value=1, variable=self.radio_state, bg=THEME_COLOR, fg="white", command=self.radio_used)
        self.medium = Radiobutton(text="Medium", value=2, variable=self.radio_state, bg=THEME_COLOR, fg="white", command=self.radio_used)
        self.hard = Radiobutton(text="Hard", value=3, variable=self.radio_state, bg=THEME_COLOR, fg="white", command=self.radio_used)

        # Position radio buttons
        self.easy.grid(column=0, row=2, pady=10)
        self.medium.grid(column=1, row=2, pady=10)
        self.hard.grid(column=2, row=2, pady=10)

        # Start button
        self.start_button = Button(text="Start Quiz", command=self.begin_game)
        self.start_button.grid(column=1, row=3)

        self.window.mainloop()

    def radio_used(self):
        """Called when a radio button is clicked."""
        print(f"Selected Difficulty: {self.radio_state.get()}")  # Debugging print

    def get_questions_number(self):
        """Retrieve selected difficulty and number of questions."""
        difficulty = self.radio_state.get()  # Get the selected value (1, 2, or 3)
        question_num = self.num_of_questions.get()  # Assuming `self.num_of_questions` is an Entry field

        # Pass both values to your data retrieval function
        self.question_data = get_data(question_num, difficulty)
        return self.question_data

    def begin_game(self):
        """Start the quiz by getting the selected values."""
        difficulty = self.radio_state.get()  # Get selected difficulty
        print(f"Starting quiz with difficulty: {difficulty}")  # Debugging print
        self.get_questions_number()  # Call your function
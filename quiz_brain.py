class QuizBrain:
    def __init__(self, question_list):
        # Initialize the quiz with the list of questions
        self.question_number = 0  # Keeps track of the current question number
        self.question_list = question_list  # Stores the list of questions
        self.score = 0  # Track the user's score

    def has_more_questions(self):
        # Check if there are more questions to ask
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Get the current question and ask the user for an answer
        current_question = self.question_list[self.question_number]  # Get the current question object
        self.question_number += 1  # Move to the next question
        user_answer = input(
            f"Q. {self.question_number}: {current_question.question} (True/False): ")  # Ask the user for their answer
        self.check_answer(user_answer, current_question.answer)  # Check if the user's answer is correct

    def check_answer(self, user_answer, correct_answer):
        # Check the user's answer and update the score accordingly
        if user_answer.lower() == correct_answer.lower():  # Compare both answers in lowercase for consistency
            self.score += 1  # Increase the score if the answer is correct
            print("You got it right!")
        else:
            print("That's wrong.")

        # Display the correct answer and the user's current score
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

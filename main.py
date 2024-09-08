from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create the question bank
# Loop through each question in question_data (list of dictionaries)
# Create a Question object for each question and add it to question_bank
question_bank = []
for question in question_data:
    question_text = question["text"]   # Extract the question text
    question_answer = question["answer"]   # Extract the corresponding answer
    new_question = Question(question_text, question_answer)   # Create a new Question object
    question_bank.append(new_question)   # Add the new Question object to question_bank

# Initialize the QuizBrain with the list of questions (question_bank)
quiz = QuizBrain(question_bank)

# Run the quiz until all questions are answered
while quiz.has_more_questions():
    quiz.next_question()   # Ask the next question and process the user's answer

# After the quiz is completed, display the user's final score and total questions answered
print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")



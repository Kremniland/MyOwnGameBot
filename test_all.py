from data_base.manager import GuessedQuestionManager, QuestionManager

def get_random_question(user_tg_id, category):
    guessed_questions = GuessedQuestionManager().get_guessed_question(user_tg_id)
    # result = QuestionManager().get_random_question(guessed_questions, category)
    return guessed_questions


data = GuessedQuestionManager().get_guessed_question(111)
print(data)
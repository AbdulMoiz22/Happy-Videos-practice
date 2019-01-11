question_prompts= [
    'What colors are apples?\n(a) Red (b) Purple (c) blue\naa',
    'What colors are berries?\n(a) Red (b) Purple (c) blue',
    'What colors are baingan?\n(a) Red (b) Purple (c) blue'

]
class Question:
    def __init__(self,prompt,answer):
        self.prompt= prompt
        self.answer= answer
questions = [
    Question(question_prompts[0],'a'),
    Question(question_prompts[1],'b'),
    Question(question_prompts[2],'c'),
]
def run_test(questions):
    score= 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print('You got '+str(score) + '/' + str(len(questions)))
run_test(questions)

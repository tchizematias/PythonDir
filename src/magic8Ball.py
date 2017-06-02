#!/usr/bin/python3

# Randomly getting a and Answer everytime the program runs.
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'Its the decidely so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook no so good'
    elif answerNumber == 9:
        return 'This is the of line'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
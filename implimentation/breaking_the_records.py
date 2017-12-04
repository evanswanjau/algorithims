'''
A program that shows the number of time a person has broken the highest record
and lowest record decresed
'''

games = int(input('Enter number of games played: '))
scores = input('Enter scores (seperate by space) ')

def low_and_high(games, scores):

    scores = scores.split(' ') # Take out the space and set into a list
    scores = [int(i) for i in scores] # convert the string to integers
    score_length = len(scores)

    high = 0
    low = 0

    highest_record = scores[0]
    lowest_record = scores[0]
    for i in scores[1:]:
        if i > highest_record:
            highest_record = i
            high += 1
        elif i < lowest_record:
            lowest_record = i
            low += 1

    print("highest records broken: ", high)
    print("Lowest record: ", low)

low_and_high(games, scores)

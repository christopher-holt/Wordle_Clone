#!/usr/bin/env python

import sys
import random
import pandas as pd
import pathlib
from datetime import date

def Guess():
    guess = str(input("Please enter a guess: "))
    return guess

def isRightAnswer(guess, target):

    """
    This function will check to see if the guess string is equal to the target string. If so, return True
    """

    if guess == target:
        return True

def compare_guess_to_target(guess, target):
    """
    This function will compare the guess to the target and return the following information in list form:
        If the character in the guess is in the target and in the same location, it will be capitalised
        If the character in the guess is in the target but a different location, it will be lowercase
        If the character in the guess is NOT in the target, there will be a '-' next to it in the list
    """
    guess_char = list(guess)
    target_char = list(target)

    match_list = list()
    final_list = list()
    ## This checks to see if the letter is in the word in any spot
    for char in guess:
        if char in target:
            match_list.append(char)

    for i in range(len(guess_char)):
        ## If the letters are in the same spot, make it upper
        if guess_char[i] == target_char[i]:
            guess_char[i] = guess_char[i].upper()

        ## If the letters are not in the match list, remove them
        elif guess_char[i].lower() not in match_list:
            guess_char[i] = guess_char[i] + '-'
        
    for i in range(len(guess_char)):
        final_list.append(guess_char[i])

    return final_list

def outOfGuesses(guess_number, max_guesses):

    """
    This function checks to see if the user has reached the max number of guesses
    """

    if guess_number == max_guesses:
        return True

def getAllAnswers():
    """
    This function will read in the file containing the five letter words and return them as a list
    """
    with open("five_letter_words.txt", "r") as answers:
        lines = answers.readlines()
        targets = []
        for line in lines:
            targets.append(str(line).replace("\n", ""))
    return(targets)

def pickAnswer():
    """
    This function will pick a random answer from the list of fiver letter words and return the random answer
    """
    targets = getAllAnswers()
    return random.choice(targets)




def isGuessAWord(guess):
    """
    This function will determine if the guess is in the list of possible answers
    """
    list_of_answers = getAllAnswers()
    inAnswers = False
    while not inAnswers:
        if guess in list_of_answers:
            inAnswers = True
        else:
            print('Guess must be a a five letter word')
            guess = Guess()
    
    return guess

def read_records(new_record):
    """
    This function will read in the records file if it exists. If it doesn't it will create one
    """

    path = pathlib.Path("records.csv")
    if path.is_file():
        records = pd.read_csv("records.csv")
    else:
        new_record = True
        data = {'day':['0'],
        'word':['0']}
        columns = ["day", "word"]
        #data = [['0','0']]
        records = pd.DataFrame(data)
    
    return records, new_record
    

def hasTodayBeenPlayed(current_day,target, records, new_record):
    """
    This is a function that will check if wordle has been played already in the day and if it has, repeat the word
    """
    ## Current day and covert it to string, then a dictionary with the target
    date_to_input = current_day.strftime("%Y-%m-%d")
    day_and_word = {'day':[date_to_input], 'word':[target]}
    day_and_word = pd.DataFrame(day_and_word, columns = ['day', 'word'])
    ## has this date been played before
    isTodayPlayed = records.loc[records['day'].str.contains(date_to_input)]
    ## If it hasn't, start the record with today's data
    if isTodayPlayed.empty:
        print('You have not played Wordle today!')
        if new_record:
            records = pd.DataFrame(data = day_and_word)
        else:
            records = pd.concat([records, day_and_word])
        alreadyPlayed = False
    else:
        ## If it has, set the answer to the same answer
        print('You have already played Wordle today!')
        target = isTodayPlayed.values[0][-1]
        alreadyPlayed = True
    
    return records, alreadyPlayed, target



def main():

    ## Define the length of the word (preset to five), preset answer, max number of guesses
    max_guesses = 6
    guess_number = 1

    new_record = False
    records, new_record = read_records(new_record)
    target = pickAnswer()
    
    current_day = date.today()
    records, alreadyPlayed, target = hasTodayBeenPlayed(current_day, target, records, new_record)


    ## Pick a random answer from the file
    ## Have user enter in their guess via input
    guess = Guess()

    ## list of all the previous answers to print out
    all_answers = list()
    ## While guess does not match target
    match_target = False

    ## Convert target so it is easy to compare to the list
    target_formatted = target.upper()
    target_list = list(target_formatted)

    ## Make sure guess is a real, five letter word
    guess = isGuessAWord(guess)

    while not match_target:
        ## Check is guess is the right answer
        if isRightAnswer(guess, target):
            ## Format Guess for easy printing
            guess = guess.upper()
            answer_list = list(guess)
            if guess_number == 1:
                print (answer_list, '\nRight Answer in %s guess!' % (guess_number))
            else:
                all_answers.append(answer_list)
                print('\n'.join(map(str, all_answers)), ' ', guess_number)
                print ('Right Answer in %s guesses!' % (guess_number))
            match_target = True
            if alreadyPlayed == False:
                records.to_csv("records.csv", index = False)
            sys.exit(0)
        ## If guess is not the right answer, use formatting to find the letters and locations that match
        else:        
            ## Compare guess to target and see what letters line up
            guess_list = compare_guess_to_target(guess, target)

            ## Add guess to list of all previous answers
            all_answers.append(guess_list)
            print('\n'.join(map(str, all_answers)), ' ', guess_number)
            ## Check to see if user has exceeded number of allotted guesses
            if outOfGuesses(guess_number, max_guesses):
                print('Out of guesses: the correct answer is:\n', target_list)
                match_target = True
                if alreadyPlayed == False:
                    records.to_csv("records.csv", index = False)

                sys.exit(0)
            
            guess_number = guess_number + 1

            guess = Guess()
            guess = isGuessAWord(guess)



if __name__=='__main__':
    main()

#!usr/bin/python3
#Noel Glamann
#4 November 2019

""" Word Jumble Game 

Disply a word with mixed up letters. Let the user continue to guess until 
they figure out the correct word. 
Present the number of tries it took.
"""

#-----IMPORTS
import random as rd

#-----CONSTANTS

#-----FUNCTION DEFS
def welcome():
    '''welcomes user to play game'''
    print("    Let's Play Breakfast Word Jumble!")
    print("  -------------------------------------")
    print(" ")
    print("Here's your word: ")
    print(" ")
    
def selection(lst):
    '''selects which word from the list will be jumbled up and used for the game'''
    return rd.choice(lst)
    
def jumble(choice):
    '''jumbles up the word so the letters are in a random arrangement'''
    mix = list(choice)
    rd.shuffle(mix)
    
    return ''.join(mix)

def evaluation(word, correct):
    if word == correct:
        return True
    else:
        return False

    
#-----MAIN SECTION
if __name__ == "__main__":
    
    #Variables
    
    '''All the variables needed to run the program.'''
    word_bank = ["pancakes", "waffles", "syrup", "butter", "strudle", "eggs", "nutella", "toast", "coffee", "cereal", "granola", "yogurt", "croissant", "bacon", "sausage", "ham", "omlet", "muffin", "fruit", "milk", "early", "morning", "bagel", "cream", "donut", "cinnamon roll", "smoothie", "juice", "bread"]
    select_word = ""
    mixed_word = ""
    guess = ""
    attempts = 0
    response = False
    play_again = ""
    playing = True
    

    #Program
    while playing == True:
        welcome()
    
        select_word = selection(word_bank)
        mixed_word = jumble(select_word)
        print(mixed_word)
    
        while response == False:
            guess = input("Your guess? ")
            response = evaluation(guess, select_word)
            if response == False:
                attempts += 1
                print("Yeah... no that's not it.")
                print(" ")
            else: 
                attempts += 1
                print("Good job! You figured it out!")
                print("That only took you", attempts, "tries!")
                print(" ")
                
        play_again = input("Would you like to play again - y/n? ")
        if play_again == "n":
            playing = False
            print("Okay :(")
                  
        else:
            playing = True
            print("Yay!")
        
    

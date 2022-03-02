"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random
from statistics import mean
from statistics import median
from statistics import mode
from statistics import StatisticsError




def check_input():
    incorrect_input = True
    valid_guess = 1

    while incorrect_input:

        try:
            guess = int(input("Enter your guess: "))
            if(guess < 1 or guess > 100 ):
                print("Not a valid number.")
            else:
                valid_guess = guess
                break 
        except ValueError:
            print ("Not a number")
        continue

    return valid_guess


def start_game():
    
    ##. Display an intro/welcome message to the player.
    print("welcome, to the number guessing game!")
    #2. Store a random number as the answer/solution.
    number = random.randint(1, 100)
    number_guesses = 0
    overal_statistics =[]
    print("Guess a number between 1 and 100 ")
    print()
    #3. Continuously prompt the player for a guess.
    while True:
        
        guess = check_input()
        number_guesses += 1
        #a. If the guess greater than the solution, display to the player "It's lower".
        if guess  > number:
            print("It's lower")
        #b. If the guess is less than the solution, display to the player "It's higher".
        elif guess < number:
            print("It's higher")
        elif guess == number:
            
    
            overal_statistics.append(number_guesses)
            overal_statistics.sort()

            print()
            print("Got it")
            print("you had {} guesses. " .format(number_guesses))

            print()
            
            print("overall Statistics")
            print("the mean was {} . " .format(mean(overal_statistics)))
            print("the median was {} . " .format(median(overal_statistics)))
            
            try:
                print("the mode was {} . " .format(mode(overal_statistics))) # neads a sorted list
            except StatisticsError:
                print ("No unique mode found")
                print()
            again = input("Do you want to play again?: yes or no: ")
            if again == "yes":
                number_guesses = 0
                number = random.randint(1, 100)
                continue
            elif again == "no":
                print ("Good Bye thanks for playing")
                return
      
    
   # 4. Once the guess is correct, stop looping, inform the user they "Got it"
        # and show how many attempts it took them to get the correct number.
    #5. Let the player know the game is ending, or something that indicates the game is over.
    
  

# Kick off the program by calling the start_game function.
start_game()



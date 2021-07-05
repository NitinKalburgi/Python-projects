'''
A guessing game where we try to guess an number which computer has generated. 
To generate an random number we use an randint function from python libraries,
To use it we have to first import random.
'''
import random
def Guess(x): #Create an function Guess

    random_number = random.randint(1,x) # This generates an random number between 1 and x
    guess = 0 # To make sure the guess is not equal to the random number which is between 1-x we set guess = 0
    #Now we have to keep asking for the user input until they guess it right once the guess is equal to random number we stop executing.
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 and {x} : '))

        if guess < random_number:
            print("Too low, Try again and guess!!")
        
        if guess > random_number:
            print('Too high, Try again and guess!!')

        if guess == random_number:
            print('Huray! you have guessed a number corectly!!')

Guess(100)



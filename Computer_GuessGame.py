'''
This is a simple guess game whwere we choose a number and let the computer guess our number.
To let computer guess our number between some range we use the built in function 'randint'.
To use that function first we need to import random.
'''
import random
# Defining a function ComputerGuess..
def ComputerGuess(num):
    lower = 1
    higher = num
    
    '''
    To let computer take a feedback from us regarding the number it as guessed, we will create
    an empty string so we can tell it wheather the guessed number is Too high, Too low or Coreect.
    '''
    
    reply = ''
    while reply != 'C':
        # We will keep on executing this while loop until the number guessed is correct!!
        # If lower is same as higher then there is no need to guess the number, as there is only one
        if lower != higher:
            # The below line generates an random number between lower and higher which will be guessed by computer!
            guess = random.randint(lower, higher)
        
        else:
            guess = higher  #or lower as lower == higher
        '''
        We will give feedback to the computer wheather its guessed number is Too low, Too high or Coreect.
        If its coreect. Then we will exit thee while loop.
        '''

        reply = input(f'Is {guess} too high (H)\nToo low (L) \nCorrect (C)??\n').upper()

        '''
        Sometimes user doesn't enter what we want them to. S0. to prevent it from generating error i'm gonna check
        if the user has enterd anything else and if they have we'll throw an message and will execute the loops once again
        using 'continue' statement..
        '''

        if reply != 'C' or reply != 'H' or reply != 'L':
            print('PLEASE ENTER AN VALID REPLY AND TRY AGAIN!!')
            continue

        # If the guess is too high we will narrow down our search between 'lower' and 'guessed number'
        if reply == 'h':
            higher = guess - 1 # -1 is used as there is no need to include the guessed number
        
        # If the guess is too low we will narrow down our search between 'gueesed number' and 'higher'
        elif reply == 'l':
            lower = guess + 1
    
    # Finally when the gussed number is correct we print the following message!
    print(f'Hurray! I have guessed your number {guess}, correctly!')


ComputerGuess(10)





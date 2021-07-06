'''This is a small program where we can play rock paper scissors with copmputer.
To let computer make an random selection we'll import random function and later let the player choose
between rock, paper and scissors and tell who won!'''

# Import the random function
import random 

# Defining an function called 'Game' 
def Game():

    # Taking the input from the pllayer and converting it to lower case which will help to compare easily!
    input_rps = input("Enter your option Rock (r), paper (p) or Scissors (s) : ").lower()
    
    '''If the user enters something else other than what we want they to, it will throw an error. So, to avoid 
    that will check wheather the input is something else. If it is we'll return an error message!!'''
    if input_rps not in "rps":
        return 'Please enter an valid option!'

    # To let computer select somthing randomly  we'll use random.choice 
    computer_selection = random.choice(['r','p','s'])
    
    # if the player input_rps and computer_slection is same then its an tie!
    if input_rps == computer_selection:
        return "Cheers! Both of you won!!"
    
    # Else we'll return player won if the following condition satisfies
    # r > s, p > r, s > p
    elif  (input_rps == 'r' and computer_selection == 's') or (input_rps == 's' and computer_selection == 'p') \
        or (input_rps == 'p' and computer_selection == 'r'):
        return "Hurayy! YOU WON!!"

    return "Better luck next time! COMPUTER WINS!"

print(Game())
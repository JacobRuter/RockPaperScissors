import random;
play = True;
over = False;
choices = ['rock', 'paper', 'scissors'];

Userchoice = input() #Variable to take in user input
print ("My choice is ", Userchoice)

Computerchoice = choices[random.randint(0, 2)]
print ("The computer choose ", Computerchoice)

while (play == True):
if Userchoice == 'rock' :
    if Computerchoice == 'rock' :
        print('You have Tied')
    elif Computerchoice == 'paper' :
        print('You lose')
    elif Computerchoice == 'scissors' :
        print('You Win')
    
if Userchoice == 'paper' :
    if Computerchoice == 'paper' :
        print('You have Tied')
    elif Computerchoice == 'scissors' :
        print('You lose')
    elif Computerchoice == 'rock' :
        print('You Win')
    
if Userchoice == 'scissors' :
    if Computerchoice == 'scissors' :
        print('You have Tied')
    elif Computerchoice == 'rock' :
        print('You lose')
    elif Computerchoice == 'paper' :
        print('You Win')
    
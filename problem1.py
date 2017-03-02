guess = int(raw_input("Hello, please insert a random number between 1 and 1000"'>'))

from random import randrange

secret= randrange(1, 1000)

while(guess != secret):

    if(guess > secret):
	    print("Your guess is to high, the answer is lower") 
	    guess=int(raw_input("Insert another number"'>')) 
    if(guess < secret):
	    print("Your gues is to low, the answer is higher")
	    guess=int(raw_input("Insert another number"'>')) 
    if(guess == secret):
    	print("You are correct!")
    print(guess)
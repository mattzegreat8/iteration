print("Hello we are going to play a game where you type a number and the computer tries to guess it.")
from random import randrange

low=1

high=1000

hol= " "

int(raw_input("Please insert a number between 1 and 1000"'>'))
print("When the number the computer guesses is correct, type 'right'")
print("When the number the computer guesses is too high, type 'high'")
print("When the number the computer guesses is too low, type 'low'")

numberguess=randrange(1,1000)

while(hol!="right"):
	hol=raw_input("the computer guessed {}, is this the correct number?"'>'.format(numberguess))
	if(hol=="high"):
		high= numberguess-1
		numberguess=randrange(low,high)
	elif(hol=="low"):
		low= numberguess +1
		numberguess= randrange(low, high)

print("game over. The comp guessed it {}".format(numberguess))

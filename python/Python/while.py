#!/usr/bin/python
# Filename: while.py


#guess=intdd(raw_input('Guess a number:'))
def Guess(x,number=23):
	'''A small game.
       	           
	Guess a number.'''
	if x == number:
		print 'You are right!'
		running=False
		y=1
	elif x < number:
		print 'Lower than it!'
		y=0
	else:
		print 'Larger than it!'
		y=0
	return y
	print 'Done'
running = True

while running:
	x=int(raw_input('Guess a number:'))
#	Guess(x,23)
	y=Guess(x,23)
	if y == 1:
		running = False
	else:
		print 'Keep guessing'
		
print Guess.__doc__
	

#Guessing number - Computer
import random

def computer_guess(x):
  low=0
  high=x
  count=0
  feedback=' '

  while feedback!='c':

    if low!=high:
      guess=random.randint(low,high)

    else:
      guess=low

    feedback=input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
    count += 1

    if feedback =='h':
      high =guess-1

    elif feedback =='l':
      low=guess +1

  print(f'The computer guessed your number, {guess}, correctly in  {count} tries')


computer_guess(600)#x value
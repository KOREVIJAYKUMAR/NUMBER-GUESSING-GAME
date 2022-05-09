import random

n = random. randint(0,9)


chances = 5





guess = input

while chances > 0 :
  guess=int(input('Guess a number(between 0 to 9):')) 
  if guess == n :
    print('Congratulation You Won !')
    break
  else:
    if guess < n:
      print('enter a big number')
    else:
      print('enter a small number')  
  chances=chances-1
  

  

if  chances == 0:
    print('You Lose ! The number is', n)
    


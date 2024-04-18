import sys
import random

age = int(input("   Enter age\n"))
if age < 9 or age > 80:
    sys.exit('ACCESS DENIED')
elif age >= 9 or age <= 80:
    print('ACCESS GRANTED')
else:
    sys.exit('WRONG INPUT') 
print(" ")
print("ROCK".ljust(14, ".") + " 🪨")
print("PAPER".ljust(14, ".") + " 📃")
print("SCISSORS".ljust(14, ".") + " ✂️") 

p1 =input("   \n                            Enter... PLAY OF CHOICE \nROCK\nPAPER\nSCISSORS\n\n").upper() 

playables = ['ROCK','PAPER','SCISSORS']
com1 = random.choice(playables)

print("YOU CHOOSE:   " + p1)
print("PYTHON CHOOSE:   " + com1)
print(" ")
#assignments
message = 'error in game'

if p1== 'ROCK' and com1 == 'SCISSORS':
     print('😎 YOU WIN 🎉')
elif p1== 'PAPER' and com1 == 'ROCK':
     print(' 😎 YOU WIN 🎉')
elif p1 == 'SCISSORS' and com1 == 'PAPER':
     print('😎 YOU WIN 🎉')
elif p1 == 'ROCK' and com1 == 'PAPER':
     print('🐍 PYTHON WINS')
elif p1 == 'PAPER' and com1 == 'SCISSORS':
    print('🐍 PYTHON WINS')
elif p1 == 'SCISSORS' and com1 == 'ROCK':
    print('🐍 PYTHON WINS')
elif p1 == com1:
    print("🤔 TIE GAME")
else:
    print(message)
     
     
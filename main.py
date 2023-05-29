#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
EndGame = False
import random
print(""" / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
""") 

print("Welcome to the Number Guessing Game!")
numberlist = list(range(1,101))

#def game():
print("I'm thinking of a number between 1 and 100.")
Answer = random.choice(numberlist)
print(f"Pssst, the correct answer is {Answer}")
Difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if Difficulty == 'easy':
  guesses = 10
else:
  guesses = 5
while EndGame == False:
  

  print(f"You have {guesses} attempts remaining to guess the number.")
  UserGuess = int(input("Make a guess: "))
  if guesses > 0:
    if UserGuess <  Answer:
      print("Too low")
      print("Guess again")
      guesses-=1
    elif UserGuess >  Answer:
      print("Too high")
      print("Guess again")
      guesses-=1
      
    else:
      print(f"You got it! The answer was {Answer}.")
      EndGame = True
      
  else:
    print("You've run out of guesses, you lose.")
    EndGame = True

    
  
  
  
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
## Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode)

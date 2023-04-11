import random

easy_level_turns = 10
hard_level_turns = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too High.")
    return turns - 1
  elif guess < answer:
    print("Too Low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy_level_turns
  else:
    return hard_level_turns
    
def game():
  print("Welcome to The Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1,100)
  
  turns = set_difficulty()
  
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess Again.")

game()

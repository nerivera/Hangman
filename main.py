# mode -> True: random word from the tuple words will be selected without repeats until all have been used, when it repeats
# mode -> False: user will be prompted for word
mode = False

# A tuple of words to guess from
# They can only contain letters and spaces
# Not case-sensitive
words = (
  "Hello There",
  "How are you doing",
  "United States of America",
  "Supercalifragilisticexpialidocious",
  "Programming Language"
)

from art import states
from os import system
from random import randint

chosenWords = []
def randWord():
  """
  Generates a new random word from words, resetting after they have all been used
  """
  global chosenWords
  if len(chosenWords) == len(words):
    chosenWords = [chosenWords[-1]]
  x = list(set(words) - set(chosenWords))[randint(0, len(words) - len(chosenWords) - 1)]
  chosenWords.append(x)
  return x.upper()

def isAllowed(text, spaces):
  """
  Returns True if text is made up of only letters (and spaces is spaces if True)
  """
  for x in text:
    if x.lower() == x.upper() and (not spaces or x != " "):
      return False
  return True

def display(w, d):
  """
  Generates the display for the blanks and the previous guesses
  """
  f = []
  for letter in w:
    f.append(" " if letter == " " else letter if letter in d else "_")
  return " ".join(f) + "\n\nGuesses: " + ", ".join(d)

# Hopefully the rest of the code speaks for itself

playAgain = "Y"
while(playAgain == "Y"):
  system("clear")
  if mode:
    word = randWord()
  else:
    word = input("Word to guess: ").upper()
    while(not isAllowed(word, True)):
      system("clear")
      word = input("Word to guess: ").upper()
  wrong = 0
  guesses = []
  won = 0
  while wrong < 6:
    system("clear")
    print(states[wrong], display(word, guesses))
    guess = input("Enter a guess: ").upper()
    if guess == word:
      won = 2
      break
    if len(guess) == len(word):
      won = 0
      break
    if guess in guesses or len(guess) != 1 or not isAllowed(guess, False):
      continue
    guesses.append(guess)
    if not (guess in word):
      wrong += 1
    if not ("_" in display(word, guesses)):
      won = 1
      break
  playAgain = ""
  while not playAgain == "Y" and not playAgain == "N":
    system("clear")
    print(states[wrong if won > 0 else 6], display(word, guesses))
    print("Nice! You guessed the whole thing!" if won == 2 else "Congratulations: You won!" if won == 1 else "You lost. The word was " + word + "\nBetter luck next time!")
    playAgain = input("Would you like to play again (y/n)? ").upper()

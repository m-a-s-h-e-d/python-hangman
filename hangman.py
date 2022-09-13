import random

# ===========================================================================

game_result = False # True = Win, False = Lose
max_lives = 5 # Total number of wrong guesses
current_lives = 0 # Total number of wrong guesses
selected_word = "" # Selected word for hangman
required_characters = set() # Required characters
guessed_characters = set() # Set of guessed characters

# ===========================================================================

def validateChar(guess):
  return guess.isalpha() and guess == len(guess) * guess[0]

# ===========================================================================

def pick_random_word():
  with open('words.txt', 'r') as file:
    data = file.read()
    word = list(map(str, data.split()))
    selected = random.choice(word)
    
  return selected


# ===========================================================================

def set_required_characters(selected):
  required_characters = set()
  
  for character in selected:
    required_characters.add(character)

  return required_characters

# ===========================================================================
  
def get_selected_formatted():
  word_formatted = ''
  append_character = '_'
  
  for character in selected_word:
    if (character in required_characters):
      append_character = '_'
    else:
      append_character = character
    word_formatted += (append_character + ' ')
  return word_formatted

# ===========================================================================
  
def setupGame():
  global selected_word, required_characters, current_lives, max_lives, game_result
  selected_word = pick_random_word()
  required_characters = set_required_characters(selected_word)
  current_lives = max_lives
  game_result = False

# ===========================================================================
  
def game():
  global current_lives, required_characters, game_result
  
  while (current_lives > 0 and len(required_characters) > 0):
    print('===============================================\n')
    print(f'Current word: {get_selected_formatted()}')
    print(f'Current lives: {current_lives}')
    guess = input('Enter your guess: ')
    print('\n')
    if (not validateChar(guess)):
      print(f'\"{guess}\" is an invalid input. Your input must be a character\n')
      continue

    if (guess in guessed_characters):
      print(f'You have already guessed: \"{guess}\"\n')
      continue

    guessed_characters.add(guess)
    if guess in required_characters:
      required_characters.remove(guess)
    else:
      current_lives -= 1
    if len(required_characters) == 0:
      game_result = True

  print('===============================================\n')

# ===========================================================================
      
def main():
  global game_result
  setupGame()
  game()
  print(f'You win, the word was: {selected_word}' if game_result
    else f'You lose, the word was: {selected_word}')

# ===========================================================================

main()

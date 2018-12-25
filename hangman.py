# '_____'
# '|   |'
# '|   @'
# '|  /|\\'
# '|   |'
# '|  / \\'
# '|'
# '======'

from random import choice
from os import system, name
from time import sleep

# Clears the terminal. Stolen from Stack Exchange
def clear():
# for windows
    if name == 'nt':
        _ = system('cls')
# for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# These are the ascii hang men
mans = ['_____\n|   |\n|\n|\n|\n|\n|\n======\n',\
        '_____\n|   |\n|   @\n|\n|\n|\n|\n======\n',\
        '_____\n|   |\n|   @\n|   |\n|\n|\n|\n======\n',\
        '_____\n|   |\n|   @\n|  /|\n|\n|\n|\n======\n',\
        '_____\n|   |\n|   @\n|  /|\\\n|\n|\n|\n======\n',\
        '_____\n|   |\n|   @\n|  /|\\\n|   |\n|\n|\n======\n',\
        '_____\n|   |\n|   @\n|  /|\\\n|   |\n|  /\n|\n======\n',\
        '_____\n|   |\n|   @\n|  /|\\\n|   |\n|  / \\\n|\n======\n']

# Replace an underscore with a letter in the word progress
def update_string(word_prog, i, guess):
    s = list(word_prog)
    s[i] = guess
    return "".join(s)

# List of words. Currently a word file is being used instead
#word_list = ['potatoes', 'extreme', 'portent', 'strange', 'handsome', 'school',\
#        'global', 'artichoke', 'capybara', 'orchid', 'coordinate', 'family',\
#        'opossum', 'burrito', 'horse', 'quilt', 'garbage', 'raccoon', 'hat']

# Wipe the screen, introduce the game. Sleeps are for the arcade aesthetic
clear()
print '_____\n|   |\n|\n|\n|\n|\n|\n======\n'
print 'Welcome to Hangman.'
sleep(0.5)
print 'You can guess one letter at a time,'
sleep(0.5)
print 'or if you think you know the word,'
sleep(0.5)
print 'you can try to guess the full word.'
sleep(0.5)
print 'be warned: if you guess three wrong words'
sleep(0.5)
print '(any guess longer than one letter is a word),'
sleep(0.5)
print 'you lose. Good luck.'
sleep(0.5)

# Set up word and variables
filename = "word_list.txt"
with open(filename, "r") as f:
    lines = f.readlines()
    word = choice(lines)

#word_stat = word_list[randint(0, len(word_list))] # Picks a random word from the list above
word_stat = word.strip() # For "word static" - the word being guessed
word_prog = '_' * len(word_stat) # For "word progress" - correct guesses
letters = '' # Empty string for wrong letter guesses
wrong = 0 # Wrong guess counter. Less system heavy than len(letters) every time
full_guess = 0 # Full word guess counter

# This loop should never run out. Should always exit at win or loss
while wrong < 7:
# Get guess from player, make all input lowercase
    guess = raw_input('Make a guess: ')
    guess = guess.lower()

# Guess full word
    if len(guess) > 1 and guess.isalpha() == True:
        if guess == word_stat:
            print 'Nice work, that\'s the word. You win.'
            exit()
        else:
            full_guess += 1
# Lose if three wrong words are guessed
    if full_guess == 3:
        print 'That was your last guess. Game over.\nThe word was: ' + word_stat
        exit()

# Check guess
    if len(guess) == 1 and guess.isalpha() == True:
        i = 0
        found = False
# Check guess against word. If a match is found, fill in letter(s) over blanks
        for i in range(0, len(word_stat)):
            if guess == word_stat[i]:
                word_prog = update_string(word_prog, i, guess)
                found = True
            i += 1
        if found == True:
            print 'Good guess'
# If the letter is not in the word
        if found == False:
            if guess in  letters:
                print 'You guessed that already'
            else:
                letters += guess
                wrong += 1
                print 'Not that one'
# If the guess is not a single letter
    elif guess.isalpha() == False:
        print 'That\'s not a letter'
    else:
        print 'That\'s not the word'

    sleep(1)
    clear()

# Respond
    print mans[wrong] + 'Guessed: ' + letters + '_' * (7 - wrong)
    print 'Progress: ' + word_prog
    if wrong == 7:
        print 'He\'s dead, Jim.\nThe word was: ' + word_stat
        exit()

# Win condition
    if word_prog == word_stat:
        print 'You guessed the word, the man goes free.'
        exit()

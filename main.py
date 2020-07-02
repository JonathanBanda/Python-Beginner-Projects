# Overall objective
# We want to get user input
# Check each letter with the actual word
# Decide if the user got the entry correct or incorrect
# Apply the rules of Hangman



# First we want to  get random words

def get_data():
    import pandas as pd
    URL = 'https://raw.githubusercontent.com/JonathanBanda/Python-Beginner-Projects/master/randomWords.txt'
    random_words = pd.read_csv(URL)

    return random_words


# using this to check the length of our randomwords.txt file
#print(random_words.info())
# we have 50 rows

# Generate a Random word
# create a function to call a new random word

def call_random_word(data):
    ''' Function to get a random word from the .txt file '''
    import random

    randomWord = data.at[random.randint(0,49),'RANDOM WORDS']

    return randomWord

def displayUpdate(letter, word, wordtray):
    for i in range(len(word)):
        if letter == word[i]:
            wordtray[i] = letter








def check_input(user_input):
    ''' Code here'''

# main section of code

wrong_counter = 0
wordtray = []

userResponse = input('Welcome to Hangman!!\nTo begin enter [y/n]: ').lower()

if userResponse == 'y':
    print('Great lets play Hangman!\n\n')
    data = get_data()
    #print(call_random_word(data))
    random_Word_To_Guess = call_random_word(data)

    for x in range(len(random_Word_To_Guess)):
        wordtray.append('_')

    print("Your word to guess is " + random_Word_To_Guess)

    for letter in random_Word_To_Guess:
        print('_', end=" ")

    for i in range(len(random_Word_To_Guess)):
        ''' code here'''
        users_guess = input('\n\n\nEnter your guess: ').lower()

        decision = displayUpdate(users_guess, random_Word_To_Guess, wordtray)

        for x in wordtray:
            print(x, end= ' ')

    print('Congradulations you win !!')




else:
    print('Awe maybe next time')














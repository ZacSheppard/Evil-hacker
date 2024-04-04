import random


lives = 3
correct_guesses = 0
grid = [                  # creates 4x4 grid.
    ["word", "word", "word", "word"],
    ["word", "word", "word", "word"],
    ["word", "word", "word", "word"],
    ["word", "word", "word", "word"],
]

connections = [  # makes library's of words called connections, each connection has 4 words and a linking word/phrase

    {"linking_word": "evil words/things",  # the phrase that links all the 4 words
     "words": ["devious", "evil", "Zac", "naughty"]},  # the words included in the list

    {"linking_word": "types of males",
     "words": ["sigma", "beta", "alpha", "yogurt"]},

    {"linking_word": "common things you see while on too much benadryl",
     "words": ["spiders", "shadow people", "the hat man", "demons "]},

    {"linking_word": "ben and jerrys flavors ",
     "words": ["gimme-smore", "vanilla", "coffee-coffee-buzz-buzz-buzz", "chunky-monkey"]},

    {"linking_word": "medieval helmets",
     "words": ["frogmouth", "kettle-hat", "hounskull", "sallet"]},

    {"linking_word": "test",
     "words": ["i", "i", "i", "i"]},

]

selected_connections = random.sample(connections, 4)

connection1, connection2, connection3, connection4 = selected_connections

correctly_guessed_words = []

all_words = []

def fill_grid():
    global all_words
    # Flatten the list of shuffled words
    shuffled_words = []  #creates list of shuffled words
    for connection in selected_connections: #for loop to gather the single connection inside the full list of connections
        for word in connection["words"]: #refers to each word inside of the inside of the connection
            shuffled_words.append(word) #adds each word to the shuffled words list
    # Shuffle the flattened list of words
    
    random.shuffle(shuffled_words) #uses shuffle to shuffle the word inside the shuffled words list
    
    # Distribute the shuffled words across the grid   
    for l in range(4):  #refers to the length of the list because its four things long
        for w in range(4): #same thing but this time its width
            if shuffled_words:  #checks if there are still words in the shuffled words list 
                grid[l][w] = shuffled_words.pop(0)  #adds word into spots inside of the grid ensuring each word is only used once
                all_words.append(grid[l][w]) #adds words that are being added to the gird to the all_words variable
    print_grid(grid) #prints the grid
    return grid

def print_grid(grid):
    for l in range(len(grid)):
        for w in range(len(grid[l])):
            word = grid[l][w]
            if word in correctly_guessed_words:
                word = "\033[93m" + word + "\033[0m"  # Change the color to gold
            print(word, end=" | ")
        print()  # Move to the next line
        print("-" * (len(grid[0]) * 10 + 3))  # Add horizontal line between rows

def player_guess():
    global guesses  #makes the variable global
    guesses = []
    guess_number = 1
    while guess_number <= 4:  # Loop until 4 guesses are made
        guess = input("Guess #{}: ".format(guess_number))  # Ask the player for their guess
        if guess in all_words:   #checks if guess is in all words list
            guesses.append(guess)  #adds the guess to list of guesses
            guess_number += 1  # Increment guess number only if the guess is correct
        else:
            print("invalid guess, Try again.")
    print (guesses)
    return guesses

def check_if_guess_correct():
    global lives
    global grid               #makes all these variables global
    global correct_guesses
    for connection in selected_connections:         #loopsn through all the selected connections
        if set(guesses) == set(connection["words"]):  #checks if the guess is in the words in the selected connections
            print(f"Correct! The connection was: {connection['linking_word']}")   #if its in correct its prints a statement saying what the category was
            for word in connection["words"]:
                correctly_guessed_words.append(word)   # Append each word from the connection to correctly_guessed_words
            correct_guesses += 1  
            return

    print("Incorrect")
    lives -= 1
    print(f"remaining live = {lives} ")
    
def game_reset():
    global lives, correct_guesses, grid, selected_connections, correctly_guessed_words, all_words
    lives = 3
    correct_guesses = 0
    grid = [
        ["word", "word", "word", "word"],
        ["word", "word", "word", "word"],
        ["word", "word", "word", "word"],
        ["word", "word", "word", "word"],
    ]
    connections = [
        {"linking_word": "evil words/things", "words": ["devious", "evil", "Zac", "naughty"]},
        {"linking_word": "types of males", "words": ["sigma", "beta", "alpha", "yogurt"]},
        {"linking_word": "common things you see while on too much benadryl", "words": ["spiders", "shadow people", "the hat man", "demons "]},
        {"linking_word": "ben and jerrys flavors", "words": ["gimme-smore", "vanilla", "coffee-coffee-buzz-buzz-buzz", "chunky-monkey"]},
        {"linking_word": "medieval helmets", "words": ["frogmouth", "kettle-hat", "hounskull", "sallet"]},
        {"linking_word": "test", "words": ["i", "i", "i", "i"]},
    ]
    selected_connections = random.sample(connections, 4)
    correctly_guessed_words = []
    all_words = []

def main():
    while lives > 0:           #if lives goes below zero it prints you lose
        while correct_guesses < 4:   #if you get more than 4 correct guesses you win
            fill_grid()
            player_guess()
            check_if_guess_correct()
            if lives < 0:
        print("you win!")
        reset = input("would you like to play again? ('yes' or 'no')")
        if reset == ("yes"):
            game_reset()
            main()
        else:
            print("game over")
    reset = input("would you like to play again? ('yes' or 'no')")
    if reset == ("yes"):
        game_reset()
        main()
    else:
        print("game over")        
            

    print("you lose :(")

main()

    
    
    


    


   
    














import random

lives = 3

grid = [                  # creates 4x4 grid.
    ["word", "word", "word", "word"],
    ["word", "word", "word", "word"],
    ["word", "word", "word", "word"],
    ["word", "word", "word", "word"],
]

connections = [  # makes library's of words called connections, each connection has 4 words and a linking word/phrase

    {"linking_word": "evil words/things",  # the phrase that links all the 4 words
     "words": ["devious", "evil", "Zac", "naughty"]},  # the words included in the list

    {"linking_word": "places you can find spiders",
     "words": ["haunted-house", "web", "backyard", "haloween"]},

    {"linking_word": "common things you see while on too much benadryl",
     "words": ["spiders", "shadow people", "the hat man", "demons "]},

    {"linking_word": "ben and jerrys flavors ",
     "words": ["gimme-smore", "vanilla", "coffee-coffee-buzz-buzz-buzz", "chunky-monkey"]},

    {"linking_word": "medieval helmets",
     "words": ["frogmouth", "kettle-hat", "hounskull", "sallet"]},

]

selected_connections = random.sample(connections, 4)

connection1, connection2, connection3, connection4 = selected_connections

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
                all_words.append(grid[l][w])
    print_grid(grid)
    return grid

def print_grid(grid):
    for row in grid:
        print(" | ".join(row))  # Add separator between words
        print("-" * (len(row) * 10 + 3))  # Add horizontal line between rows

fill_grid()

print(all_words)
print(connection1)
#please can you type in your four words
def player_guess():
    global guesses
    guesses = []
    guess_number = 1
    while guess_number <= 4:  # Loop until 4 guesses are made
        guess = input("Guess #{}: ".format(guess_number))  # Ask the player for their guess
        if guess in all_words:
            guesses.append(guess)
            guess_number += 1  # Increment guess number only if the guess is correct
        else:
            print("Incorrect guess, Try again.")
    print (guesses)
    return guesses
player_guess()


def check_if_guess_correct():
    global lives
    for connection in selected_connections:
        if set(guesses) == set(connection["words"]):
            print(f"Correct! the connection was:  {connection['linking_word']}")
            return
    print("Incorrect")
    lives -= 1

    
check_if_guess_correct()





    


   
    














import random #lets me use random

#mr fongs twitter is @pitawater

grid = [                  #creates 4x4 grid.
    ["word","word","word","word"],
    ["word","word","word","word"],
    ["word","word","word","word"],
    ["word","word","word","word"],
]

connections = [  #makes library's of words called connections, each connection has 4 words and a linking word/phrase
    
    {"linking_word" : "evil words/things",               #the phrase that links all the 4 words          
    "words" : ["devious", "evil", "Zac", "naughty"]},  # the words included in the list
   
    {"linking_word" : "places you can find spiders",
    "words" : ["haunted house", "web", "backyard", "haloween"]},
    
    {"linking_word" : "common things you see while on too much benadryl",
    "words" : ["spiders", "shadow people", "the hat man", "demons "]},
    
    {"linking_word" : "ben and jerrys flavors ",
    "words" : ["gimme smore", "vanilla", "coffee coffee buzz buzz buzz", "chunky monkey"]},
   
    {"linking_word" : "medieval helmets",
    "words" : ["frogmouth", "kettle hat", "hounskull", "sallet"]},
    
]

selected_connections = random.sample(connections, 4)

 
for connection in selected_connections:
    row = 0 
    col = 0  # Reset column for each connection
    for word in connection["words"]:
        grid[row][col] = word
        col += 1
        if col == 4:  # If column reaches 4, move to the next row
            row += 1
            col = 0

print(grid)

#please can you type in your four words
def player_guess():
    guess = input("please guess your four words") 
    while guess.isdigit():
        guess = input("make sure your guess matches with the words in the grid")
        print(grid)
    return guess





    


   
    














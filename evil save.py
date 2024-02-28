def print_words_from_categories(word_categories): #function that allows me to access words from their category
    for category in print_words_from_categories:  #selects the individual category's from the whole group
        for word in category['words']:  #selects the words from each category
            print(word)

def setup_word_categories():  #holds all the words for later use
    word_categories = []
    category1 = {
    "linking_word" : "evil words/things",                        #adds words to library
    "words" : ["devious", "evil", "Zac", "naughty"]  
    }
    category2 = {
    "linking_word" : "places you can find spiders",
    "words" : ["haunted house", "web", "backyard", "haloween"]
    }
    category3 = {
    "linking_word" : "common things you see while on too much benadryl",
    "words" : ["spiders", "shadow people", "the hat man", "demons "]
    }
    category4 = {
    "linking_word" : "ben and jerrys flavors ",
    "words" : ["gimme smore", "vanilla", "coffee coffee buzz buzz buzz", "chunky monkey"]
    }
    category5 = {
    "linking_word" : "medieval helmets",
    "words" : ["frogmouth", "kettle hat", "hounskull", "sallet"]  
    }
    word_categories.append(category1)
    word_categories.append(category2)
    word_categories.append(category3)             #adds all the words into the one category
    word_categories.append(category4)
    word_categories.append(category5)

    return word_categories

def make_evil_word_grid():
    grid_size = 4
    word_grid = []
    
    for _ in range(grid_size):
        row =  []
        for _ in range(grid_size):
            row.append('word')
        word_grid.append(row)

grid = [
    ["word","word","word","word"],
    ["word","word","word","word"],
    ["word","word","word","word"],
    ["word","word","word","word"],
]

connections = [
    
    {"linking_word" : "evil words/things",                        #adds words to library
    "words" : ["devious", "evil", "Zac", "naughty"]},
   
    {"linking_word" : "places you can find spiders",
    "words" : ["haunted house", "web", "backyard", "haloween"]},
    
    {"linking_word" : "common things you see while on too much benadryl",
    "words" : ["spiders", "shadow people", "the hat man", "demons "]},
    
    {"linking_word" : "ben and jerrys flavors ",
    "words" : ["gimme smore", "vanilla", "coffee coffee buzz buzz buzz", "chunky monkey"]},
   
    {"linking_word" : "medieval helmets",
    "words" : ["frogmouth", "kettle hat", "hounskull", "sallet"]},
    
]


row = 0
col = 0
for connection in connections:
    for word in connection["words"]:
        grid[row][col] = word
        col = col + 1
    row = row + 1
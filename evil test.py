import random

connections = [  
    {"linking_word": "evil words/things", 
     "words": ["devious", "evil", "Zac", "naughty"]},  

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

print(selected_connections)

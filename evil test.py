def test_1():
    category1 = {
    "linking_word" : "evil words/things",
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
    for word in category1['words']:
        print(word)

    print(category3["words"])
    print(category3["linking_word"])
    
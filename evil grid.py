import random # imports the evil random integer

words = ["word1", 
         "word2", 
         "word3", 
         "word4", 
         "word5",
         "word6", 
         "word7", 
         "word8", 
         "word9", 
         "word10",
         "word11", 
         "word12", 
         "word13", 
         "word14", 
         "word15", 
         "word16"]


grid = []
word_index = 0

for row in range(0,4):
    row = []
    for col in range(0,4):
        row.append(words[word_index])
        word_index += 1
    grid.append(row)

print(grid)

#evil random

print(random.randint(0,14))

for i in range(100000):
    print(random.randint(1,100))



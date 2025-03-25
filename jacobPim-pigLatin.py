# Jacob Pim
# Pig Latin

vowels = ["a", "e", "i", "o", "u"]

# Step 1) Open files
poem = open("Jabberwocky.txt", "r")
text = poem.read()
poem.close()

# splitting lines
lines = text.split("\n")

wordLine = []
wordSum = 0

""""
# remove empty lines
for line in lines:
    if len(line) == 0:
        lines.remove(line)
"""


# split into words
for line in lines:
    if len(line) != 0:
        print(line.split(" "))
        wordLine.append(line.split(" "))
    else:
        wordLine.append(line)

# pigify the words
for line in range (len(wordLine)):
    if len(wordLine[line]) != 0:
        for word in range(len(wordLine[line])):
            thing = wordLine[line][word]
            firstLetter = thing[0]
            wordLine[line][word] = thing[1:] + firstLetter + "ay"

# scrap attempt
for line in wordLine:
    if len(line) != 0:
        currentLine = " ".join(line)
        print(currentLine)
    else:
        print(line)

# print(wordLine)
        

# Step 4) Creating Pig Latin lines

    # Step 4a) Instantiating each Pig Latin line
    
    # Step 4b) Turning each word into Pig Latin

    # Step 4c) Appending each Pig Latin line


# Step 5) Writing the file

# Step 5a) Opening the new file

# Step 5b) Writing and formatting

# Step 5c) Closing the file
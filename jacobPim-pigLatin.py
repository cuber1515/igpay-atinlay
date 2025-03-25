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

pigLatin = open("Abberwockyjay.txt", "w")

# scrap attempt
for line in wordLine:
    if len(line) != 0:
        currentLine = " ".join(line)
        print(currentLine)
        pigLatin.write(f"{currentLine} \n")

    else:
        print(line)
        pigLatin.write("\n")

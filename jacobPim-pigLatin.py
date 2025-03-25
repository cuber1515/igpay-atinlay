# Jacob Pim
# Pig Latin


vowels = ["a", "e", "i", "o", "u"]

# Open files
poem = open("Jabberwocky.txt", "r")
text = poem.read()
poem.close()

# Splitting lines
lines = text.split("\n")

# List of words
wordLine = []

# Adding the words to the list
for line in lines:
    if len(line) != 0:
        # print(line.split(" "))
        wordLine.append(line.split(" "))
    else:
        wordLine.append(line)

# Pigify the words
for line in range (len(wordLine)):
    if len(wordLine[line]) != 0:
        for word in range(len(wordLine[line])):
            thing = wordLine[line][word]

            # Finding first vowel
            firstVowel = 1
            for i in range (len(thing)):
                if thing[i] in vowels:
                    firstVowel = i
                    break
            
            # If starts with vowel
            if firstVowel == 0:
                wordLine[line][word] = thing + "ay"
            
            # If not
            else:
                firstLetters = thing[0:firstVowel]
                wordStart = firstVowel
                wordLine[line][word] = thing[wordStart:] + firstLetters + "ay"

# Open new file
pigLatin = open("Abberwockyjay.txt", "w")

# Print pig latin poem to new file
for line in wordLine:
    if len(line) != 0:
        currentLine = " ".join(line)
        # print(currentLine)
        pigLatin.write(f"{currentLine} \n")

    else:
        # print(line)
        pigLatin.write("\n")

pigLatin.close()
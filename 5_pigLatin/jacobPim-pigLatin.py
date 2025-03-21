# Jacob Pim
# Pig Latin

vowels = ["a", "e", "i", "o", "u"]

# Step 1) Open files
poem = open("Jabberwocky.txt", "r")
text = poem.read()
poem.close()

# Step 2) Splitting the line into files
lines = text.split("\n")
realLines = lines

# Step 3) Splitting the lines into words
wordLine = []
wordSum = 0

for line in lines:
    if len(line) == 0:
        lines.remove(line)

for line in lines:
    print(line.split(" "))
    wordLine.append(line.split(" "))

for line in wordLine:
    for thing in line:
        firstLetter = thing[0]
        thing = thing[1:] + firstLetter + "ay"
        print(thing)

print(wordLine)
        

# Step 4) Creating Pig Latin lines

    # Step 4a) Instantiating each Pig Latin line
    
    # Step 4b) Turning each word into Pig Latin

    # Step 4c) Appending each Pig Latin line


# Step 5) Writing the file

# Step 5a) Opening the new file

# Step 5b) Writing and formatting

# Step 5c) Closing the file
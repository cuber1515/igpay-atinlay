import os

name = input("What is your full name?\n")
name = name.split(" ")

lowerFirstName = name[0][0].lower() + name[0][1:]
regularLastName = name[1]
prefix = lowerFirstName + regularLastName
fileName = prefix + "-pigLatin.py"

if not os.path.exists(fileName):
    print("FILE NOT FOUND: Make sure the formatting on your file\'s title is correct.")
    print("The format should be : ' + lowerFirstLetterName + '-pigLatin.py")
    raise SystemExit

file = open(fileName,"r")
text = file.read()
lines = text.split("\n")
file.close()

numOpen = 0
numClose = 0
numRead = 0
numWrite = 0
for line in lines:
    if "open" in line:
        numOpen += 1
    if "close()" in line:
        numClose += 1
    if "read()" in line:
        numRead += 1
    if "write" in line:
        numWrite += 1

issueCount = 0
if numOpen < 2:
    print("NOT ENOUGH OPENED FILES:  There are less than 2 open statements in your code.")
    print("                          You need to open the input file for your code and the output file.")
    issueCount += 1

if numClose == 0:
    print("NOT ENOUGH CLOSED FILES:  There are less than 2 close statments in your code.")
    print("                          You should have opened at least 2 files, so we need you to close at least 2 files.")
    issueCount += 1

if numRead == 0:
    print("NO FILES READ:  There are no read statements in your code.")
    print("                You cannot perform string manipulations without reading the input.")
    issueCount += 1

if numWrite == 0:
    print("NO FILES WRITTEN:  You have no write statements in your code.")
    print("                   You need to write an output file for grading.")
    issueCount += 1

if issueCount > 0:
    raise SystemExit

if os.path.exists("Abberwockyjay.txt"):
    os.remove("Abberwockyjay.txt")

exec(text)

solution = """wastay rilligbay ndaay hetay lithysay ovestay 
idday yregay ndaay imblegay niay hetay abeway 
llaay imsymay ereway hetay orogovesbay 
ndaay hetay omemay athsray utgrabeoay 

ewarebay hetay abberwockjay ymay onsay 
hetay awsjay hattay itebay hetay lawscay hattay atchcay 
ewarebay hetay ubjubjay irdbay ndaay hunsay 
hetay rumiousfay andersnatchbay 

ehay ooktay ishay orpalvay wordsay niay andhay 
onglay imetay hetay anxomemay oefay ehay oughtsay 
osay estedray ehay ybay hetay umtumtay reetay 
ndaay toodsay whileaay niay houghttay 

ndaay saay niay ffishuay houghttay ehay toodsay 
hetay abberwockjay ithway yeseay foay lamefay 
amecay hifflingway hroughtay hetay ulgeytay oodway 
ndaay urbledbay saay tiay amecay 

neoay wotay neoay wotay ndaay hroughtay ndaay hroughtay 
hetay orpalvay ladebay entway nickersay nacksay 
ehay eftlay tiay eadday ndaay ithway tsiay eadhay 
ehay entway alumphinggay ackbay 

ndaay asthay houtay lainsay hetay abberwockjay 
omecay otay ymay rmsaay ymay eamishbay oybay 
oay rabjousfay ayday alloohcay allaycay 
ehay hortledcay niay ishay oyjay 

wastay rilligbay ndaay hetay lithysay ovestay 
idday yregay ndaay imblegay niay hetay abeway 
llaay imsymay ereway hetay orogovesbay 
ndaay hetay omemay athsray utgrabeoay 
"""
try:
    file = open("Abberwockyjay.txt","r")
except:
    print("FILE NOT FOUND:  The output file \"Abberwockyjay.txt\" was not able to be opened.")

answer = file.read()
file.close()
file = open("testLog.txt","w")
file.write("OUTPUT FROM YOUR CODE\n")
file.write("==============================================\n")
file.write(answer)
file.write("==============================================\n")
file.write("OUTPUT THAT IS EXPECTED\n")
file.write("==============================================\n")
file.write(solution)
file.write("==============================================\n")
if answer == solution:
    file.write("PASS")
else:
    file.write("FAIL")
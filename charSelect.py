import csv
f = open("AllLinks.csv","r")
dataIn = f.read()
list1 = dataIn.split("\n")

d = open("feat.csv","r")
csv_d = csv.reader(d)
allchar =[]
feat = []
line_count = 0
for row in csv_d:
    if line_count>0:
        feat.append(row)
        allchar.append(row)
    line_count = line_count + 1
s = open("suppChar.csv","r")
csv_s = csv.reader(s)
supp = []
line_count = 0
for row in csv_s:
    if line_count>0:
        supp.append(row)
        allchar.append(row)
    line_count = line_count + 1
o = open("otherChar.csv","r")
csv_o = csv.reader(o)
other = []
line_count = 0
for row in csv_o:
    if line_count>0:
        other.append(row)
        allchar.append(row)
    line_count = line_count + 1
a = open("antagChar.csv","r")
csv_a = csv.reader(a)
antag = []
line_count = 0
for row in csv_a:
    if line_count>0:
        antag.append(row)
        allchar.append(row)
    line_count = line_count + 1

onlychar = []
for i in range(len(allchar)):
    onlychar.append(allchar[i][1])
    
noDup = list(dict.fromkeys(onlychar))

#print("How many characters are you looking for?")
#charNum = int(input())

allChar = []

#for k in range(charNum):
print("what character do you want to read? ")
#char = str(input())
char = "kinney"
posChar =[]
for i in range(len(noDup)):
    if char in noDup[i] or char.lower() in noDup[i].lower():
        posChar.append(noDup[i])

topFive = []
top = 0
topChar = "temp"
p = 0
cnt = True
while cnt == True:
    for j in range(5):
        l = len(posChar)-j
        top = 0
        for i in range(l):
            if onlychar.count(posChar[i]) > top:
                topChar = posChar[i]
                top = onlychar.count(posChar[i])
        topFive.append(topChar)
        posChar.remove(topChar)

    print("all characters that match your input")
    for i in range(len(topFive)):
        print("[" + str(i+1) + "] " + topFive[i])
    print("[6] More")
    
    chosNum = int(input("choose which character you were referenceing\n"))
    if chosNum != 6:
        cnt = False
        chosChar = topFive[chosNum-1]
        
        
print(chosChar)
import csv
f = open("webpages.csv","r")
dataIn = f.read()
list1 = dataIn.split(",")

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

print("How many characters are you looking for?")
charNum = int(input())

allChar = []

for k in range(charNum):
    print("what character do you want to read?  ["+str(k+1)+"]")
    char = str(input())

    posChar =[]
    for i in range(len(noDup)):
        if char in noDup[i] or char.lower() in noDup[i].lower():
            posChar.append(noDup[i])

    print("all characters that match your input")
    for i in range(len(posChar)):
        print("[" + str(i+1) + "] " + posChar[i])
    
    chosNum = int(input("choose which character you were referenceing\n"))
    chosChar = posChar[chosNum-1]

    print("In what way do you want them to appear")
    print("[1] Featured Character \n[2] Supporting Character\n[3] Other Character\n[4] Antagonist\n[5] All\n[6] Done")
    charType = []
    typeChar = 0
    while typeChar != 6:
        typeChar = int(input())
        charType.append(typeChar)
    
    charType = list(dict.fromkeys(charType))
    charType.remove(6)

        
    comicChar = []        
    for i in range(len(charType)):
        if charType[i] == 1:
            for j in range(len(feat)):
                if chosChar in feat[j][1]:
                    comicChar.append(feat[j][0]+" - "+list1[int(feat[j][0])])
        elif charType[i] == 2:
            for j in range(len(supp)):
                if chosChar in supp[j][1]:
                    comicChar.append(supp[j][0]+" - "+list1[int(supp[j][0])])
        elif charType[i] == 3:
            for j in range(len(other)):
                if chosChar in other[j][1]:
                    comicChar.append(other[j][0]+" - "+list1[int(other[j][0])])
        elif charType[i] == 4:
            for j in range(len(antag)):
                if chosChar in antag[j][1]:
                    comicChar.append(antag[j][0]+" - "+list1[int(antag[j][0])])
        elif charType[i] == 5:
            for j in range(len(feat)):
                if chosChar in feat[j][1]:
                    comicChar.append(feat[j][0]+" - "+list1[int(feat[j][0])])
            for j in range(len(supp)):
                if chosChar in supp[j][1]:
                    comicChar.append(supp[j][0]+" - "+list1[int(supp[j][0])])
            for j in range(len(other)):
                if chosChar in other[j][1]:
                    comicChar.append(other[j][0]+" - "+list1[int(other[j][0])])
            for j in range(len(antag)):
                if chosChar in antag[j][1]:
                    comicChar.append(antag[j][0]+" - "+list1[int(antag[j][0])])
        else:
            print("please put what category you want for your character")
    allChar.append(comicChar)

bothComic = []
allCharComic = []
comicToStay = []
if charNum > 1:
    for i in range(len(allChar)):
        if i == 0:
            curComic = allChar[0]
        else:
            for j in range(len(allChar[i])):           
                if allChar[i][j] in curComic:
                    comicToStay.append(allChar[i][j])
            curComic = comicToStay
            comicToStay=[]
            
        #bothComic = [k for l, k in enumerate(bothComic) if l not in comicToGo]

                   
    for charp in curComic:
        print(charp)

#else:
    #for chars in comicChar:
      #  print(chars)



        
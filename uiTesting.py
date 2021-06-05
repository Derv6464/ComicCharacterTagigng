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

b = open("comicList.txt","w")

onlychar = []
for i in range(len(allchar)):
    onlychar.append(allchar[i][1])
    
noDup = list(dict.fromkeys(onlychar))

print("How many characters are you looking for?")
charNum = input()
while charNum.isdigit() == False or int(charNum) < 1:
    print("Invalid input")
    charNum = input()


allChar = []
chosChars = []
for k in range(int(charNum) ):
    print("what character do you want to read?  ["+str(k+1)+"]")
    char = str(input())

    posChar =[]
    for i in range(len(noDup)):
        if char in noDup[i] or char.lower() in noDup[i].lower():
            posChar.append(noDup[i])
    while not posChar:
        print("character not found, try again")
        print("what character do you want to read?  ["+str(k+1)+"]")
        char = str(input())

        posChar =[]
        for i in range(len(noDup)):
            if char in noDup[i] or char.lower() in noDup[i].lower():
                posChar.append(noDup[i])
        
    topFive = []
    top = 0
    topChar = "temp"
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
    
        chosNum = input("choose which character you were referenceing\n")
        while chosNum.isdigit() == False or int(chosNum) < 1 or int(chosNum) > 6:
            print("Invalid input")
            chosNum = input("choose which character you were referenceing\n")
            
        if int(chosNum) != 6:
            cnt = False
            chosChar = topFive[int(chosNum)-1]
        
    
    chosChars.append(chosChar)
    print("In what way do you want them to appear")
    print("[1] Featured Character \n[2] Supporting Character\n[3] Other Character\n[4] Antagonist\n[5] All\n[6] Done")
    charType = []
    typeChar = 0
    while int(typeChar) != 6:
        typeChar = input()
        while typeChar.isdigit() == False or int(typeChar) < 1 or int(typeChar) > 6:
            print("Invalid input")
            typeChar = input()
        charType.append(int(typeChar))
    
    charType = list(dict.fromkeys(charType))
    charType.remove(6)

        
    comicChar = []        
    for i in range(len(charType)):
        if charType[i] == 1:
            for j in range(len(feat)):
                if chosChar in feat[j][1]:
                    #print(feat[j][0]+" - "+list1[int(feat[j][0])])
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
curComic = []
if int(charNum) > 1:
    for i in range(len(allChar)):
        if i == 0:
            curComic = allChar[0]
        else:
            for j in range(len(allChar[i])):           
                if allChar[i][j] in curComic:
                    comicToStay.append(allChar[i][j])
            curComic = comicToStay
            comicToStay=[]
else:
    for i in range(len(allChar)):
        for j in range(len(allChar[i])):
            curComic.append(allChar[i][j])

            
        #bothComic = [k for l, k in enumerate(bothComic) if l not in comicToGo]

b.write("All the comics that include: ")
for charp in chosChars:
    if charp == chosChars[-1]:
        b.write(charp)
    elif charp == chosChars[-2]:
        b.write(charp + " and ")
    else:
        b.write(charp+ ", ")
    
b.write(" are ("+str(len(curComic))+" comics):")
for charp in curComic:
    print(charp)
    b.write("\n"+charp)

b.close()
#else:
    #for chars in comicChar:
      #  print(chars)



        
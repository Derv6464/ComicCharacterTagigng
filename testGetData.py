import requests
from bs4 import BeautifulSoup
import re
#test cases
#https://marvel.fandom.com/wiki/Young_Avengers_Vol_1_1
#https://marvel.fandom.com/wiki/Marvels_Vol_1_0
#https://marvel.fandom.com/wiki/Runaways_Vol_5_32
#https://marvel.fandom.com/wiki/Runaways_Vol_5_14
#https://marvel.fandom.com/wiki/House_of_M_Vol_1_8
#https://marvel.fandom.com/wiki/Wolverine:_Road_to_Hell_Vol_1_1
#https://marvel.fandom.com/wiki/Marvels_Vol_1_1
#https://marvel.fandom.com/wiki/Alias_Vol_1_2
d = open("feat.csv","w")
s = open("suppChar.csv","w")
o = open("otherChar.csv","w")
a = open("antagChar.csv","w")
r = requests.get("https://marvel.fandom.com/wiki/Alias_Vol_1_2")
soup = BeautifulSoup(r.content, 'html.parser')

results = soup.find('div', class_='mw-parser-output') #get all text in this div
bruh = str(results) 



l = 0
q = 0
antag = 0
other = 0
vill = 0
text2 = ''.join(bruh.split())  #join it all together
searchtxt = text2.split('<h2id="AppearingHeader1">')
searchtxt = searchtxt[1].split('<h2id="StoryTitle1">')
seartxt = searchtxt[0]
#var to check which catagories r on this site
featured = 0
antagonist = 0
supporting = 0
others = 0
villans = 0
rAnds = 0
if 'FeaturedCharacters:' in seartxt:
    featured = 1
    print("featured")
if 'SupportingCharacters:' in seartxt:
    supporting = 1
    print("supporting")
if 'Antagonists:' in seartxt:
    antagonist = 1
    print("antagonist")
if 'OtherCharacters:' in seartxt:
    others = 1
    print("other")
if 'Villains:' in seartxt:
    villans = 1
    print("villans")
if 'RacesandSpecies:' in seartxt:
    rAnds = 1
    print("r&s")


suppA = text2.split("Antagonists:")
suppO = text2.split("OtherCharacters:")


if len(suppA[0]) > len(suppO[0]):   #whether antag or other comes first
    other = 1                       #other is first
else:
    other = 0
if villans == 0:
    suppV = text2.split("Villains:")
    if other == 1:
        if len(suppO[0]) > len(suppV[0]):
            vill = 1
    else:
        if len(suppA[0]) > len(suppV[0]):
            vill = 1
else:
    vill = 0
    
#feat2 = BeautifulSoup(featCond, 'html.parser')
#supp2 = BeautifulSoup(suppCond, 'html.parser')
if featured == 1:
    g = []
    z = []
    if supporting == 1:                          #if supporting char first
        feat2 = bruh.split("Featured Characters:")
        feat3 = feat2[1].split("Supporting Characters:")
        feat4 = BeautifulSoup(feat3[0], 'html.parser')
    else:                   #if antag first
        feat2 = bruh.split("Featured Characters:")
        feat3 = feat2[1].split("Antagonists:")
        feat4 = BeautifulSoup(feat3[0], 'html.parser')

if supporting == 1:
    h = []
    if other != 1 and vill != 1:           #if antag first
        supp2 = bruh.split("Supporting Characters:")
        supp3 = supp2[1].split("Antagonists:")
        supp4 = BeautifulSoup(supp3[0], 'html.parser')
    elif vill != 1:                         #if other first
        supp2 = bruh.split("Supporting Characters:")
        supp3 = supp2[1].split("Other Characters:")
        supp4 = BeautifulSoup(supp3[0], 'html.parser')
    else:                          #if villan first
        supp2  = bruh.split("Supporting Characters:")
        supp3 = supp2[1].split("Villains:")
        supp4 = BeautifulSoup(supp3[0], 'html.parser')
        
if antagonist == 1:
    if other == 1 and rAnds == 1:
        anta2 = bruh.split("Antagonists:")
        anta3 = anta2[1].split("Races and Species:")
        anta4 = BeautifulSoup(anta3[0], 'html.parser')
    elif other == 1:
        anta2 = bruh.split("Antagonists:")
        anta3 = anta2[1].split("Locations:")
        anta4 = BeautifulSoup(anta3[0], 'html.parser')
    else:
        anta2 = bruh.split("Antagonists:")
        anta3 = anta
        tifulSoup(othe3[0], 'html.parser')
        
if villans == 1:
    if vill == 1:
        vill2 = bruh.split("Villains:")
        vill3 = vill2[1].split("Other Characters:")
        vill4 = BeautifulSoup(vill3[0], 'html.parser')
    elif rAnds == 1:
        vill2 = bruh.split("Villains:")
        vill3 = vill2[1].split("Races and Species:")
        vill4 = BeautifulSoup(vill3[0], 'html.parser')
    else:
        vill2 = bruh.split("Villains:")
        vill3 = vill2[1].split("Locations:")
        vill4 = BeautifulSoup(vill3[0], 'html.parser')

#get chars
linkFeat = []
linkSupp = []
linkAnta = []
linkOthe = []
linkVill = []

if featured == 1:
    for link in feat4.findAll('a'):
        linkFeat.append(link.get('href'))
    volNum = []
    for j in range(len(linkFeat)):
        if "Vol" in linkFeat[j]:
            volNum.append(j)
    linkFeat = [i for j, i in enumerate(linkFeat) if j not in volNum]
    for i in range(linkFeat.count(None)):   #removes any null values
        linkFeat.remove(None) 
    for i in range(len(linkFeat)):
        d.write(linkFeat[i] + "\n")

if supporting == 1:
    for link in supp4.findAll('a'):
        linkSupp.append(link.get('href'))
    for i in range(linkSupp.count(None)):    #removes any null values
        linkSupp.remove(None)
    for i in range(len(linkSupp)):
        s.write(linkSupp[i] + "\n")
        
if antagonist == 1:
    for link in anta4.findAll('a'):
        linkAnta.append(link.get('href'))
    for i in range(linkAnta.count(None)):    #removes any null values
        linkSupp.remove(None)
    for i in range(len(linkAnta)):
        a.write(linkAnta[i] + "\n")
        
if others == 1:
    for link in othe4.findAll('a'):
        linkOthe.append(link.get('href'))
    for i in range(linkOthe.count(None)):    #removes any null values
        linkOthe.remove(None)
    for i in range(len(linkOthe)):
        o.write(linkOthe[i] + "\n")
        
if villans == 1:
    for link in vill4.findAll('a'):
        linkVill.append(link.get('href'))
    for i in range(linkVill.count(None)):    #removes any null values
        linkVill.remove(None)
    for i in range(len(linkVill)):
        a.write(linkVill[i] + "\n")
  #gets rid of all in vol



#print(g1 + "\n" + "SUPPORTING" + "," + h1 + "\n")


d.close()
a.close()
o.close()
s.close()


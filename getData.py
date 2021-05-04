import requests
from bs4 import BeautifulSoup
import re
import csv
f = open("webpages.csv","r")
d = open("feat.csv","w")
s = open("suppChar.csv","w")
o = open("otherChar.csv","w")
a = open("antagChar.csv","w") #opening files

dataIn = f.read()
list1 = dataIn.split(",")
for i in range(1699):                 #for ammount of links
    r = requests.get(list1[i])        #get link
    soup = BeautifulSoup(r.content, 'html.parser')       #get web contents
    results = soup.find('div', class_='mw-parser-output')    #getting ceratin part of website
    bruh = str(results)   #putting in var

    l = 0
    q = 0
    antag = 0
    other = 0
    vill = 0
    text2 = ''.join(bruh.split())    #getting rid of all spaces
    searchtxt = text2.split('<h2id="AppearingHeader1">')
    if len(searchtxt) > 1:
        pass
    else:
        continue
        print("skipped")
    searchtxt = searchtxt[1].split('<h2id="StoryTitle1">')
    seartxt = searchtxt[0]
    #var to check which catagories r on this site
    featured = 0
    antagonist = 0
    supporting = 0
    others = 0
    villans = 0
    rAnds = 0
    #checking what sections r on the site
    if 'FeaturedCharacters:' in seartxt:
        featured = 1
        #print("featured")
    if 'SupportingCharacters:' in seartxt:
        supporting = 1
        #print("supporting")
    if 'Antagonists:' in seartxt:
        antagonist = 1
        #print("antagonist")
    if 'OtherCharacters:' in seartxt:
        others = 1
        #print("other")
    if 'Villains:' in seartxt:
        villans = 1
        print("villans", i)
    if 'RacesandSpecies:' in seartxt:
        rAnds = 1
        #print("r&s")
    
    #splits txt at given point
    suppA = text2.split("Antagonists")
    suppO = text2.split("OtherCharacters")


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
    
    if featured == 1:
        if supporting == 1:                          #if supporting char first
            feat2 = bruh.split("Featured Characters:")
            feat3 = feat2[1].split("Supporting Characters:")
            feat4 = BeautifulSoup(feat3[0], 'html.parser')
        else:                   #if antag first
            feat2 = bruh.split("Featured Characters:")
            feat3 = feat2[1].split("Antagonists:")
            feat4 = BeautifulSoup(feat3[0], 'html.parser')

    if supporting == 1:
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
            anta3 = anta2[1].split("Other Characters:")
            anta4 = BeautifulSoup(anta3[0], 'html.parser')
        
    if others == 1:
        if other == 1 and antagonist == 1:
            othe2 = bruh.split("Other Characters:")
            othe3 = othe2[1].split("Antagonists:")
            othe4 = BeautifulSoup(othe3[0], 'html.parser')
        elif rAnds == 1:
            othe2 = bruh.split("Other Characters:")
            othe3 = othe2[1].split("Races and Species:")
            othe4 = BeautifulSoup(othe3[0], 'html.parser')
        else:
            othe2 = bruh.split("Other Characters:")
            othe3 = othe2[1].split("Locations:")
            othe4 = BeautifulSoup(othe3[0], 'html.parser')
        
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

    if featured == 1:        #if featured characters exist
        for link in feat4.findAll('a'):      #get all links in the featured section
            linkFeat.append(link.get('href'))
        for j in range(linkFeat.count(None)):   #removes any null values
            linkFeat.remove(None) 
        volNum = []
        for j in range(len(linkFeat)):    #gets rid of any links that link to another comic
            if "Vol" in linkFeat[j]:
                volNum.append(j)
            else:
                pass
        linkFeat = [l for j, l in enumerate(linkFeat) if j not in volNum] 

        for j in range(len(linkFeat)):        #adds to file
            d.write(str(i) +"," + linkFeat[j] + "\n")

    if supporting == 1:
        for link in supp4.findAll('a'):
            linkSupp.append(link.get('href'))
        for j in range(linkSupp.count(None)):    #removes any null values
            linkSupp.remove(None)
        for j in range(len(linkSupp)):
            s.write(str(i) +"," + linkSupp[j] + "\n")
        
    if antagonist == 1:
        for link in anta4.findAll('a'):
            linkAnta.append(link.get('href'))
        for j in range(linkAnta.count(None)):    #removes any null values
            linkAnta.remove(None)
        for j in range(len(linkAnta)):
            a.write(str(i) +"," + linkAnta[j] + "\n")
        
    if others == 1:
        for link in othe4.findAll('a'):
            linkOthe.append(link.get('href'))
        for j in range(linkOthe.count(None)):    #removes any null values
            linkOthe.remove(None)
        for j in range(len(linkOthe)):
            o.write(str(i) +"," + linkOthe[j] + "\n")
        
    if villans == 1:
        for link in vill4.findAll('a'):
            linkVill.append(link.get('href'))
        for j in range(linkVill.count(None)):    #removes any null values
            linkVill.remove(None)
        for j in range(len(linkVill)):
            a.write(str(i) +"," + linkVill[j] + "\n")
    if i%10 == 0:
        print(i)
   

    

d.close()
a.close()
o.close()
s.close()
f.close()
print("done")



import requests
from bs4 import BeautifulSoup
import re
import csv
f = open("webpages.csv","r")
c = open("finalData.csv", "w")
w = open("featuredChatacters.csv","w")
e = open("supportingCharatres.csv","w")
z = open("WebLinks.csv","w")     #opening files
#adding headers
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
    suppA = text2.split("Antagonists")
    suppB = text2.split("OtherCharacters")
    feat = re.search('FeaturedCharacters:(.*)SupportingCharacters:', text2)   #getting text between the given text
    supp = re.search('SupportingCharacters:(.*)Antagonists:', text2)
    vilA = re.search('Villains:', text2)
    if feat:
        featCond = feat.group(1)   #grouping the text to one var
    else:
        feat = re.search('FeaturedCharacters:(.*)Antagonists', text2)   #condination in case text is between dif given text
        if feat:
            featCond = feat.group(1)
            antag = 1   #if text is between the second bit of text changes this
        else:
            q = 1   #if cant find any text between these parameters 
            pass
    if supp:
        suppCond = supp.group(1)
    else:
        supp = re.search('SupportingCharacters:(.*)Other', text2)
        if supp:
            suppCond = supp.group(1)
            other = 1
        else:
            l = 1
            pass
    if len(suppA[0]) > len(suppB[0]):
        other = 1
    else:
        other = 0
    if vilA:
        vill = 1
    
    if q != 1:   #if text has been found
        g = []
        if antag != 1:       #if it is between first two parameters
            feat2  = bruh.split("Featured Characters:")   #split the text at "featured"
            feat3 = feat2[1].split("Supporting Characters:")  #split the text after "featuerd" at "supporting"
            feat4 = BeautifulSoup(feat3[0], 'html.parser')   #change the text after "featured" but before "supporting" to a bs4.type
            feat5 = feat4.text   #change that to text (so html tags wont show)
        else:    #same as above but its between second two parameters
            feat2  = bruh.split("Featured Characters:")
            feat3 = feat2[1].split("Antagonists:")
            feat4 = BeautifulSoup(feat3[0], 'html.parser')
            feat5 = feat4.text
        for i2 in range(len(feat5)):  #for the legnth of feat5
            k = feat5.split("\n")    #split the text by whenever it gose onto a new line
            for o in range(len(k)):   #for legnth of k
                g.append(k[o])   #add it to g
        g = list(dict.fromkeys(g))
        links = []
        linkG = []
        for link in feat4.findAll('a'):
            links.append(link.get('href'))
        linkG = g
        if linkG:
            del linkG[0]
        volNum = []
        for j in range(len(links)):
            if links[j]:
                if "Vol" in links[j]:
                    volNum.append(j)
                else:
                    pass
                if links[j] is "#Chronology Notes":
                    volNum.append(j)
                else:
                    pass
            elif links[j] is None:
                links[j] = "n/a"
        links = [p for j, p in enumerate(links) if j not in volNum]
        while len(linkG) > len(links):
            links.append(' ')
        for j in range(len(linkG)):
            z.write(str(i) + "," + list1[i] + "," + linkG[j]+ "," + links[j] + "\n")
        
        x = 1
        for i3 in range(len(g)):   #adds a comma between each iteam
            g.insert(x,",")
            x = x + 2
        if g:
            del g[-1]    #gets rid of last extra comma
            del g[0:2]  #gets rid of first extra comma and space
        else:
            pass
        g1 = ' '.join([str(elem) for elem in g])    #makes the listt into on str
    else:
        g1 = "N/A"

#same as above but for supporting characters
    if l != 1:
        h = []
        if other != 1 and vill != 1:
            supp2  = bruh.split("Supporting Characters:")
            supp3 = supp2[1].split("Antagonists:")
            supp4 = BeautifulSoup(supp3[0], 'html.parser')
            supp5 = supp4.text
        elif vill != 1:
            supp2  = bruh.split("Supporting Characters:")
            supp3 = supp2[1].split("Other Characters:")
            supp4 = BeautifulSoup(supp3[0], 'html.parser')
            supp5 = supp4.text
        else:
            supp2  = bruh.split("Supporting Characters:")
            supp3 = supp2[1].split("Villains:")
            supp4 = BeautifulSoup(supp3[0], 'html.parser')
            supp5 = supp4.text
        for i4 in range(len(supp5)):
            u = supp5.split("\n")
            for o in range(len(u)):
                h.append(u[o])
        h = list(dict.fromkeys(h))
        links2 = []
        linkH = []
        for link in supp4.findAll('a'):
            links2.append(link.get('href'))
        linkH = h
        if linkH:
            del linkH[0]
        volNum2 = []
        for j in range(len(links2)):
            if links2[j]:
                if "Vol" in links2[j]:
                    volNum2.append(j)
                else:
                    pass
                if "#Chronology Notes" in links2[j]:
                    volNum2.append(j)
                else:
                    pass
            elif links2[j] is None:
                links2[j] = "n/a"
        links2 = [p for j, p in enumerate(links2) if j not in volNum2]
        while len(linkH) > len(links2):
            links2.append(' ')
        for j in range(len(linkH)):
            z.write(str(i) + "," + list1[i] + "," + linkH[j]+ "," + links2[j] + "\n")
        x = 1
        for i5 in range(len(h)):
            h.insert(x,",")
            x = x + 2
        if h:
            del h[-1]
            del h[0:2]
        else:
            pass
        h1 = ' '.join([str(elem) for elem in h])
    else: h1 = "N/A"
    
    d = list1[i].split("wiki/")    #separting the link to get the name of the comic
    d2 = d[1].replace("_"," ")     #replacing _ with " " to get comic name
    #writing this into files
    c.write(str(i+1) + "," + d2 + "," + list1[i] +"," + g1 + "," + h1 + "\n")
    e.write(str(i+1) + "," + d2 + "," + list1[i] +"," + h1 + "\n")
    w.write(str(i+1) + "," + d2 + "," + list1[i] +"," + g1 + "\n")
    
    #print(str(i+1) + "," + d2 + "," + list1[i] +"," + g1 + "," + h1 + "\n")
    print(i)
   

    

f.close()
c.close()
e.close()
w.close()
z.close()
print("done")



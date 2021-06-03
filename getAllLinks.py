from bs4 import BeautifulSoup
import requests
d = open("AllLinks.csv","w")
url = "https://marvel.fandom.com/wiki/Category:Comics"
url2 = "https://marvel.fandom.com/wiki/Category:Comics?from=%C2%A019420601All+Winners+Comics+Vol+1+5%0AAll+Winners+Comics+Vol+1+5"
allAllLink = []
i = 0
while url:
#for i in range(100):
    
    if i%10 == 0:
        print(i)
        print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    nextLink = soup.find('div', class_='category-page__pagination')
    results = soup.find('div', class_='category-page__members')


    allLink = []
    for link in results.findAll('a'):
        allLink.append(link.get('href'))
    
    
    allLink = list(dict.fromkeys(allLink))
    for a in allLink:
        allAllLink.append(a)

    nxtLnk = []
    for j in nextLink.findAll('a'):
        nxtLnk.append(j.get('href'))
    if i == 0:
        url = nxtLnk[0]
    elif i == 1:
        url = nxtLnk[1]
    elif i == 263:
        break
    else:
        url = nxtLnk[2]
    i += 1
    
    
allAllLink = list(dict.fromkeys(allAllLink))
for i in range(22):
    del allAllLink[0]
    
for a in allAllLink:
    #print(a)
    d.write(a + "\n")
    
d.close()
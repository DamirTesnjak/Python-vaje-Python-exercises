'''Game_of_Thrones total count views
    Avtor: Damir Tešnjak'''

from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = "https://en.wikipedia.org/wiki/Game_of_Thrones"

response = urlopen(url).read()
soup = BeautifulSoup(response)

first_level = []
for season in soup.findAll("a"):
    if "Season" in str(season.string):
        linkSeason = str("https://en.wikipedia.org" + season["href"])
        for i in range(1,8):
            if linkSeason.endswith("(season_" + str(i) + ")"):
                if linkSeason in first_level:
                    continue
                else:
                    first_level.append(linkSeason)
#print first_level

for link in first_level:
    urlSecondLevel = link
    secondResponse = urlopen(urlSecondLevel).read()
    seasonGOT = BeautifulSoup(secondResponse)

    totalViewPerSeason = 0
    for season in seasonGOT.findAll("tr", attrs={"class": "vevent"}):
        for cell in season.findAll("td"):
            try:
                if float(str(cell)[4:8]):
                    totalViewPerSeason += float(str(cell)[4:8])
            except ValueError:
                continue

    print "Total views on first broadcast day of episodes for season " + str(first_level.index(link) + 1) + \
          ": " + str(totalViewPerSeason) + " millions."



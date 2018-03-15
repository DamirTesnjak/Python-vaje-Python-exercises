# -*- coding: UTF-8 -*-

'''Avtor: Damir Tešnjak'''

#   SHRANJEVANJE SLIK DRŽAV ZASTAV IZ WIKIPEDIJE

from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import urllib


# Glavni naslov
mainURL = "https://en.wikipedia.org/wiki/List_of_sovereign_states"

# Branje html
response = urlopen(mainURL).read()
soup = BeautifulSoup(response)

# Prazni seznami
countries = []
linksCountries = []
countryFlags = []

# PRIDOBIVANJE IMENA DRŽAV IZ HTML-a

for country in soup.findAll("span"):
    try:
        name = country.get("id").encode("utf-8")
    except AttributeError:
        continue
    if name != "List_of_states":
        countries.append(name.replace("_"," "))
print countries

# EDITING COUNTRY NAMES FOR GETTING THEIR PROPER LINKS,
#SAVING LINKS INTO LIST

for country in soup.findAll("a"):
    try:
        country_name = country.get("href")
        name = country.get("title").encode("utf-8")

    except AttributeError:
        continue

    ''' Če ime države v znački <a> ...
    vsebuje attribut '(country)', jo spremenimo tako, da v seznamu 'countries'
    zamenjamo 'država' v 'država (countries)' 
     '''

    a = " (country)"
    if a in name:
        name_edit = name[:len(" (country")-2]

        ''' Dodamo urejeno ime države v seznam in odstranimo starega'''

        countries.insert(countries.index(name_edit), name)
        del countries[countries.index(name_edit)]
        print countries
    else:
        continue

    '''Za vsako značko <a>, ki v attributu 'title' vsebuje ime države,
    če se nahaja v seznamu 'countries', pridobimo URL posamezne države v Wikipediji.'''

    if name in countries:
        print name
        country_name = str(country.get("href"))
        links = "https://en.wikipedia.org" + country_name
        linksCountries.append(links)
        linksCountries.sort()
    else:
        continue


# Pridobivanje slike zastave države na posamezni spletni strani države

for countryFlag in countries[:-17]: # da upoštevamo samo države, ki so priznane

    # Pridobitev povezave strani slike zastave posamezne države

    flag1 = "https://en.wikipedia.org/wiki/" + countryFlag.replace(" ", "_") + "#/media/File:Flag_of_" + \
        countryFlag.replace(" ", "_") + ".svg"
    countryFlags.append(flag1)


# PRIDOBITEV POVEZAVE DO SLIKE ZASTAVE POSAMEZNE DRŽAVE

country_num = 0
for flag in countryFlags:
    countryFlagURL = flag
    response = urlopen(countryFlagURL).read()
    countrySoup = BeautifulSoup(response)

    # Pridobitev URL slike na podlagi značke <meta> in attributa 'property'

    for flagImage in countrySoup.findAll("meta"):
        if flagImage.get("property") == "og:image":
            print "Saving: " + countries[country_num] + ".jpg"

            # Shranjevanje slik zastav v podmapo 'Flags' projekta

            logo = urllib.urlretrieve(str(flagImage)[35:-4], "Flags/" + countries[country_num] + ".jpg")
            country_num += 1

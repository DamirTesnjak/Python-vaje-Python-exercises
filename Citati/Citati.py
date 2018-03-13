'''Citati
    Avtor: Damir Tešnjak'''

from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import random

url = "http://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()
soup = BeautifulSoup(response)

quotes = []

for quote in soup.findAll("p", attrs={"class": "quoteContent"}):
    quotes.append(quote.string)

step = 0

while step < 5:
    print quotes[random.randint(0, len(quotes) - 1)]
    step += 1

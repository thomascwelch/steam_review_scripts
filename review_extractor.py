
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import csv

only_col = SoupStrainer(class_='apphub_CardContentMain')

with open("bguide.html") as fp:
    soup = BeautifulSoup(fp, 'lxml', parse_only=only_col)

text = soup.get_text()
print(text)

f = open('bg.txt', 'w')
f.write(text)

f = csv.writer(open('bguide_reviews.csv', 'w'))
f.writerow(['Sentiment', 'Text'])

sentiments = soup.find_all('div', class_='title')
# ideas = soup.find_all('div', class_='apphub_CardTextContext')

for sentiment in sentiments:
    feeling = sentiment.contents[0]

    f.writerow([feeling])

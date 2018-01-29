from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from importmepls import ClothObj
import sqlite3
import time

# attempts to make program appear human
headers = {'User-Agent': 'Mozilla/5.0'}
ClothObjs = []
key = input("Brand to Search for: ")
conn = sqlite3.connect("clothes.db")

c= conn.cursor()
target = ['https://www.reddit.com/r/frugalmalefashion/new/','https://www.reddit.com/r/deals/new/',
          'https://www.reddit.com/r/SneakerDeals/new/', 'https://www.reddit.com/r/kicksmarket/new/',
          'https://www.reddit.com/r/MaleFashionMarket/', 'https://www.reddit.com/r/ThriftyThread/',
          'https://www.reddit.com/r/FashionRepsBST/']

for meme in target:
    try:
        print("SubReddit: ", meme[22:])
        # creates three new arrays to hold data from reddit ranks
        names = []
        urls = []
        votes = []
        #used to hold Array of objects

        def create_table():
            c.execute('CREATE TABLE IF NOT EXISTS ClothingPlot(names TEXT, urls TEXT, votes REAL)')


        def dynamic_data_entry(x):
            y = names[x]
            a = urls[x]
            z = votes[x]

            c.execute("INSERT INTO ClothingPlot(names, urls, votes) VALUES (?, ?, ?) ", (y, a, z))
            conn.commit()


        create_table()


        scrapey_Dad = urlopen(meme)
        page = scrapey_Dad.read()
        scrapey_Dad.close()

        money_scrape = soup(page, 'html.parser')  #does html parsing
        linkScout = (money_scrape.findAll("a", {"class":"title"}))  #grabs all sale links and descriptions in first page

        counter = 0
        for name in linkScout:
            names.append(name.get_text())
            urls.append(name['href'])

        linkScout = (money_scrape.findAll("div", {"class":"score unvoted"}))

        for name in linkScout:
            votes.append(name.get_text())

        for i in range(25):
            dynamic_data_entry(i)


        #counter = 0
        #while True:
         #  if (counter == 24):
          #      break
           # counter += 1
            #print("Name: %s" % names[counter])
            #print("URL: %s" % urls[counter])
            #print("Votes: %s" % votes[counter])
            #print()

        meme = ClothObj(names, votes, urls)
        ClothObjs.append(meme)
        meme.containsBrand(names, key, urls)  ## next get user input

    except:
        print("Blocked")
        time.sleep(10)
        continue
c.close()
conn.close()

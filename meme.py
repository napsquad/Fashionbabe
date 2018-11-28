from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from importmepls import ClothObj
import time

# attempts to make program appear human
headers = {'User-Agent': 'Mozilla/5.0'}
ClothObjs = []
key = input("Brand to Search for: ")

target = ['https://old.reddit.com/r/frugalmalefashion/new/','https://old.reddit.com/r/deals/new/',
          'https://old.reddit.com/r/SneakerDeals/new/', 'https://old.reddit.com/r/kicksmarket/new/',
          'https://old.reddit.com/r/MaleFashionMarket/', 'https://old.reddit.com/r/ThriftyThread/',
          'https://old.reddit.com/r/FashionRepsBST/']

for meme in target:
    try:
        print("SubReddit: ", meme[22:])
        # creates three new arrays to hold data from reddit ranks
        names = []
        urls = []
        votes = []
        #used to hold Array of objects

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

        meme = ClothObj(names, votes, urls)
        ClothObjs.append(meme)
        meme.containsBrand(names, key, urls)  ## next get user input

    except:
        print("Blocked")
        time.sleep(2)
        continue

import datetime

class ClothObj:
    def __init__(self, setName, setVotes, setUrl):
        self.name = setName
        self.votes = setVotes
        self.url = setUrl
        self.date = datetime.date  #date should be in ddmmyy format if possible

    def printobj(self):
        print("name: %s \n  date: %s \n votes: %s \n" % self.votes, self.name, self.date)

    def containsBrand(self, nameArr, sKey, linkArr):
        corr = 0
        for i in range(25):                             # for every item
            if (nameArr[i].lower()).find(sKey.lower()) != -1:             # if found
                print("found in :", nameArr[i])         # tell title in which name is found
                print("link : ", linkArr[i])            # provided corresponding link
                print()
                corr += 1                               # if found, incerement correct counter
        if corr <= 0:                                   # if nothing is found, tell the user
            print("item not found\n")
        else:
            corr -= 1

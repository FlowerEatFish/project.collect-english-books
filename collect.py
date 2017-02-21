import requests
from bs4 import BeautifulSoup

def GetStarRate (isbn):
    getUrl = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + isbn
    getHeader = {'user-agent' : 'Chrome/56.0.2924.87'}
    getRes = requests.get (getUrl, headers = getHeader) # getResource
    getPage = BeautifulSoup (getRes.text , 'html.parser')

    getStarPage = getPage.find_all (class_ = 'a-column a-span5 a-span-last')

    for checkStarRate in getStarPage:
        try:
            checkStarRate.find (class_ = 'a-icon-alt')
            getStar = checkStarRate.find (class_ = 'a-icon-alt')
            return getStar.string[1] + getStar.string[2] + getStar.string[3]
        except:
            getStar = 'None'
            return getStar

isbn = ["9781285198248","9781285851150"]
if isbn != None:
    for i in isbn:
        print ("Check ISBN: " + i)
        print (GetStarRate (i))

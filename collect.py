import requests
from bs4 import BeautifulSoup

def GetStarRate (isbn):
    # 自 Amazon 取得書籍資訊網頁
    getUrl = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + isbn
    getHeader = {'user-agent' : 'Chrome/56.0.2924.87'}
    getRes = requests.get (getUrl, headers = getHeader) # getResource
    getPage = BeautifulSoup (getRes.text , 'html.parser')

    # 尋找評價區塊
    getStarPage = getPage.find_all (class_ = 'a-row a-spacing-mini')
    
    # 檢查並收集星數或無評價
    for checkStarRate in getStarPage:
        try:
            checkStarRate.find (class_ = 'a-icon-alt')
            getStar = checkStarRate.find (class_ = 'a-icon-alt')
            return getStar.string
        except:
            getStar = 'None'
            return getStar

'''
# Demo
print("Run demo")
isbn = ["9781285198248","9781285851150"]
if isbn != None:
    for i in isbn:
        print ("Check ISBN: " + i)
        print (GetStarRate (i))
'''

import requests
from bs4 import BeautifulSoup

class AmazonCollection():
    #isbn = getISBN # int
    browser = 'Chrome/55.0.2924.87' # str
    result = {'name': '', 'author':  '', 'star': ''} # dict

    def __init__(self, getISBN):
        # 自 Amazon 取得書籍資訊網頁
        getUrl = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + getISBN
        getHeader = {'user-agent' : self.browser}
        getRes = requests.get(getUrl, headers = getHeader)
        self.getPage = BeautifulSoup(getRes.text, 'html.parser')
        self.getPage = self.getBookDetail()

        self.result['name'] = self.getBookName()
        self.result['author'] = self.getAuthor()
        self.result['star'] = self.getStar()

    def getBookDetail(self):
        return self.getPage.find(class_ = 'a-fixed-left-grid-col a-col-right')

    def getBookName(self):
        # a.title
        try:
            checkPage = self.getPage.find(class_ = 'a-link-normal s-access-detail-page a-text-normal')
            checkPage = checkPage.attrs
            return checkPage['title']
        except:
            return "None"

    def getAuthor(self):
        try:
            checkPage = self.getPage.find(class_ = 'a-row a-spacing-small')
            checkPage = checkPage.find(class_ = 'a-row a-spacing-none')
            checkPage = checkPage.find_all('span')

            author = ''
            num = 0
            for i in checkPage:
                if i.string == 'by ':
                    continue
                if num > 0:
                    author += ' and '
                if i.string is None:
                    i = i.find(class_ = 'a-link-normal a-text-normal')
                author += i.string
                num += 1

            return author
        except:
            return "None"

    def getStar(self):
        try:
            #checkPage = self.getPage.find(class_ = 'a-icon a-icon-star a-star-4-5')
            checkPage = self.getPage.find_all(class_ = 'a-icon-alt')
            print(len(checkPage), checkPage)
            for i in checkPage:
                print(i)
            return i.string
        except:
            return "None"

# Demo
if __name__ == '__main__':
    print("Run demo")
    isbn = ["9780553808049"]
    if isbn != None:
        for i in isbn:
            print ("Check ISBN: " + i)
            data = AmazonCollection(i)
            print (data.result)

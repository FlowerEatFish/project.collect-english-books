"""Collect book details from Amazon"""
import time
import requests
from bs4 import BeautifulSoup

class AmazonCollection(object):
    """isbn: int, return: detail{title: string, author: string, star: string, isbn: string}"""
    detail = {}

    def __init__(self, isbn):
        html_code = self.get_html_code(isbn)
        book_code = self.get_book_detail(html_code)

        self.detail['isbn'] = str(isbn)
        self.detail['title'] = self.get_book_name(book_code)
        self.detail['author'] = self.get_author(book_code)
        self.detail['star'] = self.get_star(book_code)

    @classmethod
    def get_html_code(cls, isbn):
        """isbn: int, return: class"""
        browser = (
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/62.0.3202.94 "
            "Safari/537.36"
            )
        url = (
            "https://www.amazon.com/s/ref=nb_sb_noss"
            "?url=search-alias%3Dstripbooks"
            "&field-keywords=" + str(isbn)
            )
        accept_type = (
            "text/html,"
            "application/xhtml+xml,"
            "application/xml;q=0.9,"
            "image/webp,"
            "*/*;q=0.8"
            )
        header = {
            "Accept": accept_type,
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "User-Agent": browser,
        }
        print('Url:', url)
        resource = requests.get(url, headers=header)
        source_code = BeautifulSoup(resource.text, 'html.parser')
        return source_code

    @classmethod
    def get_book_detail(cls, code):
        """code: class, return: class"""
        book_code = code.find_all(class_='a-fixed-left-grid-col a-col-right')
        return book_code[0]

    @classmethod
    def get_book_name(cls, code):
        """code: class, return: string"""
        try:
            title_code = code.find(class_='s-access-title')
            title = title_code.get_text()
            return title
        except:
            return "Title not found"

    @classmethod
    def get_author(cls, code):
        """code: class, return: string"""
        try:
            code_list = code.find_all(class_='a-row a-spacing-none')
            for author_code in code_list:
                author = author_code.get_text()
                if author[:2] == 'by':
                    return author
            return "Author not found"
        except:
            return "Author not found"

    @classmethod
    def get_star(cls, code):
        """code: class, return: string"""
        review_code = code.find_all(class_='a-icon-alt')
        try:
            index = 0
            text = review_code[index].get_text()
            while text == 'Prime':
                index += 1
                text = review_code[index].get_text()
            return text
        except:
            return 'Star not found'

# Demo
if __name__ == '__main__':
    print("Run demo")
    ISBN_LIST = ["9780553808049", "9780765338440", "9780132350884"]
    if ISBN_LIST != None:
        for ISBN in ISBN_LIST:
            print("ISBN:" + str(ISBN))
            DATA = AmazonCollection(ISBN)
            print(DATA.detail)
            if ISBN != ISBN_LIST[-1]:
                time.sleep(10)

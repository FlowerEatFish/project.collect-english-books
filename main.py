"""Demo."""
import time
import collect
import read
import write


def demo():
    """No parameter is required."""
    excel_data = read.CollectAllIsbn('test.xlsx')
    isbn_list = excel_data.data
    print(isbn_list, type(isbn_list))

    star_list = []
    for isbn in isbn_list:
        print('ISBN:', isbn)
        try:
            int(isbn)
            data = collect.AmazonCollection(str(isbn))
            print(data.detail)
            star_list.append(data.detail['star'])
            if isbn != isbn_list[-1]:
                time.sleep(6)
        except:
            print("No ISBN is available.")
            star_list.append("No ISBN is available.")

    write.export_result(isbn_list, star_list)

demo()

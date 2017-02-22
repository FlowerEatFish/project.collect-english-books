from openpyxl import Workbook

def ExportResult (isbnList, starList):
    print(type(isbnList))
    print(type(starList))
    wb = Workbook()
    ws = wb.active
    ws.title = "ISBN-star"

    ws['A1'] = "ISBN"
    for i in range(len(isbnList)):
        ws['A%d' % (i+2)] = isbnList[i]

    ws['B1'] = "Star"
    for i in range(len(starList)):
        ws['B%d' % (i+2)] = starList[i]

    wb.save('document.xlsx')

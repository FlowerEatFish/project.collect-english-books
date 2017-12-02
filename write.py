"""Write into new Excel file."""
from openpyxl import Workbook

def export_result(isbn_list, star_list):
    """isbn_list: list[int], star_list: list[string]"""
    print(type(isbn_list))
    print(type(star_list))
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "ISBN-star"

    worksheet['A1'] = "ISBN"
    for index, value in enumerate(isbn_list):
        worksheet['A%d' % (index+2)] = value

    worksheet['B1'] = "Star"
    for index, value in enumerate(star_list):
        worksheet['B%d' % (index+2)] = value

    workbook.save('document.xlsx')

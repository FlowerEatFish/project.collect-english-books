from openpyxl import load_workbook

def CheckGetAllIsbn_number (number):
    if type (number) is not int:
        print ("The number isn't integer, so set it into 10.")
        return 10
    else:
        print ("The number is integer, so set it into %d." % number)
        return number

def GetAllIsbn (number):
    # 檢查 number 是否為整數
    number = CheckGetAllIsbn_number (number)

    # 取得 Excel 檔案
    getExcel = load_workbook (filename = "test.xlsx")
    getSheet = getExcel[getExcel.get_sheet_names()[0]]
    #print (getSheet)
    #print(type(getSheet))

    # 自第一列抓取 ISBN 欄位
    for i in range (30):
        checkBlock = getSheet['%s1' % chr(ord('A')+i)]
        #print(type(checkBlock.value))
        #print (checkBlock.value)
        if checkBlock.value == "ISBN" :
            setColumn = '%s' % chr(ord('A')+i )
            #print(Row)
            break

    # 自 ISBN 欄位向下收集 ISBN
    getIsbnList = []
    for i in range (number):
        getIsbn = getSheet['%s%d' % (setColumn,(i+2))].value
        #print(type('%s%d' % (Row, (i+1))))
        #print (getIsbn)
        getIsbnList.append (getIsbn)

    return getIsbnList

'''
# Demo
print("Run demo")
GetAllIsbn(10)
'''

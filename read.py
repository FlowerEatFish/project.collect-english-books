from openpyxl import load_workbook

getExcel = load_workbook(filename = "test.xlsx")
getSheet = getExcel[getExcel.get_sheet_names()[0]]
print(getSheet)
#print(type(getSheet))

for i in range(20):
    checkBlock = getSheet['%s1' % chr(ord('A')+i)]
    #print(type(checkBlock.value))
    print(checkBlock.value)
    if checkBlock.value == "ISBN":
        setColumn = '%s' % chr(ord('A')+i )
        #print(Row)
        break

for i in range(10):
    #print(type('%s%d' % (Row, (i+1))))
    print(getSheet['%s%d' % (setColumn,(i+2))].value)

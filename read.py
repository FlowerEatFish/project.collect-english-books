from openpyxl import load_workbook

class CollectAllIsbn():
    def __init__(self, getPath):
        self.path = str(getPath)
        self.maxCollection = 100 # int, 最大收集數

        if self.checkFile():
            self.file = load_workbook(filename = self.path)
            self.data = self.collectIsbn()
        else:
            print('The path is incorrect.')
            self.data = 'No data due to file not found.'

    def checkFile(self):
        try:
            load_workbook(filename = self.path)
            return True
        except:
            return False

    def checkFirstColumn(self):
        getSheet = self.file[self.file.get_sheet_names()[0]]
        for i in range(50):
            checkBlock = getSheet['%s1' % chr(ord('A')+i)]
            if checkBlock.value == 'ISBN' or checkBlock.value == 'isbn':
                return '%s' % chr(ord('A')+i)

    def collectIsbn(self):
        setColumn = self.checkFirstColumn()
        getSheet = self.file[self.file.get_sheet_names()[0]]

        getIsbnList = []
        noneData = 0
        for i in range(self.maxCollection):
            if noneData > 2:
                break
            getIsbn = getSheet['%s%d' % (setColumn,(i+2))].value
            if getIsbn is None:
                noneData += 1
                getIsbnList.append('None')
            else:
                noneData = 0
                getIsbnList.append(getIsbn)
        return getIsbnList

# Demo
if __name__ == '__main__':
    getPath = 'test.xlsx'
    data = CollectAllIsbn(getPath)
    print(data.data)

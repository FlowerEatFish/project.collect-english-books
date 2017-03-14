import sys, main
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Book_UI():
    def __init__(self):
        super().__init__()
        self.loadPath = ""
        self.bookList = {'1':'書名','2':'作者','3':'出版社','4':'出版年','5':'版次'}
        self.initUI()

    def initUI(self):
        app = QApplication(sys.argv)

        inLabel = QLabel('輸入檔案：')
        #outLabel = QLabel('輸出檔案：')
        inEdit = QLineEdit()
        inEdit.setEnabled(0)
        inButton = QPushButton('瀏覽')
        inButton.clicked.connect(self.loadFile)

        buttonA = QCheckBox(self.bookList['1'])
        buttonB = QCheckBox(self.bookList['2'])
        buttonC = QCheckBox(self.bookList['3'])
        buttonD = QCheckBox(self.bookList['4'])
        buttonE = QCheckBox(self.bookList['5'])

        startButton = QPushButton('開始')
        startButton.clicked.connect(self.runBook)

        grid = QGridLayout()

        grid.addWidget(inLabel, 0, 0)
        grid.addWidget(inEdit, 0, 1, 1, 3)
        grid.addWidget(inButton, 0, 4)

        grid.addWidget(buttonA, 1, 0)
        grid.addWidget(buttonB, 1, 1)
        grid.addWidget(buttonC, 1, 2)
        grid.addWidget(buttonD, 1, 3)
        grid.addWidget(buttonE, 1 ,4)

        grid.addWidget(startButton, 2, 0)

        self.widget = QWidget()
        self.widget.setLayout(grid)

        self.widget.setWindowTitle('Book UI')
        self.widget.setGeometry(200, 100, 100, 50)

        self.widget.show()
        app.exec_()

    def loadFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Microsoft Office Excel (*.xlsx)", options=options)
        if fileName:
            print(fileName)

    def runBook(self):
        print('Run~')
        main.RunMain()

if __name__ == '__main__':
    Book_UI()

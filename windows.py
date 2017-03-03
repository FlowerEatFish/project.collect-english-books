from tkinter import *

class GUI_windows(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.inputText = Label(self)
        self.inputText["text"] = "輸入檔案："
        self.inputText.grid(row=0, column=0)

        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField.grid(row=0, column=1, columnspan=3)

        self.outputText = Label(self)
        self.outputText["text"] = "輸出檔案："
        self.outputText.grid(row=1, column=0)

        self.outputField = Entry(self)
        self.outputField["width"] = 50
        self.outputField.grid(row=1, column=1, columnspan=3)

        self.imputPath = Button(self)
        self.imputPath["text"] = "瀏覽"
        self.imputPath.grid(row=0, column=4)

        self.outputPath = Button(self)
        self.outputPath["text"] = "瀏覽"
        self.outputPath.grid(row=1, column=4)

        self.bookName = Checkbutton(self)
        self.bookName["text"] = "書名"
        self.bookName.grid(row=2, column=0)

        self.bookAuthor = Checkbutton(self)
        self.bookAuthor["text"] = "第一作者"
        self.bookAuthor.grid(row=2, column=1)

        self.bookPublisher = Checkbutton(self)
        self.bookPublisher["text"] = "出版社"
        self.bookPublisher.grid(row=2, column=2)

        self.bookPubYear = Checkbutton(self)
        self.bookPubYear["text"] = "出版年"
        self.bookPubYear.grid(row=2, column=3)

        self.bookStar = Checkbutton(self)
        self.bookStar["text"] = "評價"
        self.bookStar.grid(row=2, column=4)

        self.start = Button(self)
        self.start["text"] = "開始搜集圖書資訊"
        self.start.grid(row=3, column=2)

if __name__ == '__main__':
    root = Tk()
    root.title("快速搜集圖書資訊")
    root.resizable(0,0)
    app = GUI_windows(master=root)
    app.mainloop()

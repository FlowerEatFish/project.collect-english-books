# coding=utf-8
import read, collect, write, time

class RunMain():
    def __init__(self):
        readData = read.CollectAllIsbn('test.xlsx')
        print (readData.data, type(readData.data))

        starList = []
        for i in range (len(readData.data)):
            getData = readData.data[i]
            print('Check ISBN: ', getData)
            try:
                # 如果 ISBN 欄位裡面是 ISBN 的命令
                int (getData)
                #print("It's OK; it is %s" % str(isbnList[i]))
                data = collect.AmazonCollection (str(getData))
                print (data.result['star'])
                starList.append (data.result['star'])
                # 避免被 Amazon 封鎖
                time.sleep (12)
            except:
                # 如果不是的命令
                print ("No ISBN is available.")
                starList.append ("No ISBN is available.")

        write.ExportResult (readData.data, starList)

if __name__ == '__main__':
    RunMain()

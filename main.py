import read, collect, write, time

class RunMain():
    def __init__(self):
        isbnList = read.GetAllIsbn(15)
        print (isbnList)
        print (type (isbnList))

        starList = []
        for i in range (len(isbnList)):
            print(isbnList[i])
            try:
                # 如果 ISBN 欄位裡面是 ISBN 的命令
                int (isbnList[i])
                #print("It's OK; it is %s" % str(isbnList[i]))
                data = collect.AmazonCollection (str(isbnList[i]))
                print (data.result['star'])
                starList.append (data.result['star'])
                # 避免被 Amazon 封鎖
                time.sleep (10)
            except:
                # 如果不是的命令
                print ("No ISBN is available.")
                starList.append ("No ISBN is available.")

        write.ExportResult (isbnList, starList)

if __name__ == '__main__':
    RunMain()

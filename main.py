import read, collect, write, time

isbnList = read.GetAllIsbn(100)
print (isbnList)
print (type (isbnList))

starList = []
for i in range (len(isbnList)):
    print(isbnList[i])
    try:
        # 如果 ISBN 欄位裡面是 ISBN 的命令
        int (isbnList[i])
        #print("It's OK; it is %s" % str(isbnList[i]))
        print (collect.GetStarRate (str(isbnList[i])))
        starList.append (collect.GetStarRate (str(isbnList[i])))
        # 避免被 Amazon 封鎖
        time.sleep (5)
    except:
        # 如果不是的命令
        print ("No ISBN is available.")
        starList.append ("No ISBN is available.")

write.ExportResult (isbnList, starList)

import read, collect, time

isbnList = read.GetAllIsbn(15)
print (isbnList)
print (type (isbnList))

for i in range (len(isbnList)):
    print(isbnList[i])
    try:
        int (isbnList[i])
        print (collect.GetStarRate (str(isbnList[i]))
    except:
        print ("No ISBN is available.")
    time.sleep (3)

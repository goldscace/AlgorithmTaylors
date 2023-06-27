ItemStockDict={}


def AddItem(x,y):
    file=open("Stock.txt","a+")
    y=str(y)
    file.write(x.capitalize()+"\t\t||\t"+y+"\n")
    file.close()

def Descend():
    print("Item\t\t||\tStock")
    for i in DescendItemStockDict:
        Item=str(i[0])
        Stock=str(i[1])
        print(Item+"\t\t||\t"+Stock)

def rewriteDescend():
    file=open("Stock.txt","w+")
    for i in DescendItemStockDict:
        Item=str(i[0])
        Stock=str(i[1])
        file.write(Item+"\t\t||\t"+Stock+"\n")
    file.close()


def TurnintoDict():
    file.seek(0)
    ItemStockList=file.readlines()
    for i in ItemStockList:
        i=i.replace('\t','').strip().split("||")
        i[1]=int(i[1])
        ItemStockDict[i[0]]=i[1]

def rewriteStock():
    file=open("Stock.txt","w+")
    for i in ItemStockDict:
        Item=str(i)
        Stock=str(ItemStockDict[i])
        file.write(Item+"\t\t||\t"+Stock+"\n")
    file.close()

def CurrentStock():
    print("\nCurrent Items in Invetory")
    print("Item\t\t||\tStock")
    for i in ItemStockDict:
        ItemStockDict[i]=str(ItemStockDict[i])
        print(i+"\t\t||\t"+ItemStockDict[i])





while True:
    file=open("Stock.txt","r")
    file.seek(0)
    print("\nItem\t\t||\tStock")
    print(file.read())
    print('''What do you wish to do?
1. Insert new items
2. View items in descending order of number of stocks
3. Add stocks to selected items
4. Delete stocks on selected items
5. View items low in stocks
6. Exit''')
    try:
        answer=int(input("Your Answer: "))
    except:
        print("\nInvalid Answer. Try Again")
        continue
    if answer == 1:
        file.close()
        while True:
            item=str(input("\nWhat item: "))
            try:
                stocks=int(input("\nHow much: "))
                AddItem(item,stocks)
                break
            except:
                print("\nInvalid Answer. Try Again")
    elif answer == 2:
        TurnintoDict()
        DescendItemStockDict=sorted(ItemStockDict.items(), key=lambda stock:stock[1], reverse=True)
        print("\nDescending Order of Items according to stocks")
        ItemStockDict={}
        while True:
            try:
                Descend()
                answer=int(input('''
Do you wish to rewrite the file with this new order?
1. Yes
2. No
Your Answer: '''))
                if answer == 1: 
                    file.close()
                    rewriteDescend()
                    break
                elif answer ==2:
                    break
                else:
                    print("\nInvalid Answer. Try Again")
            except:
                print("\nInvalid Answer. Try Again")
    elif answer == 3:
        TurnintoDict()
        while True: 
            if answer == 2:
                break
            AddStockItem=str(input("\nWhich Item would you like to add stock: ")).capitalize()
            if AddStockItem not in ItemStockDict:
                print("\nStock does not exist! Add the name of the stock first.")
                break
            try:
                AddStockNumber=int(input("\nHow much: "))
            except:
                print("\nInvalid Answer. Pls try again")
                continue
            for i in ItemStockDict:
                if AddStockItem == i:
                    ItemStockDict[i]=int(ItemStockDict[i])
                    ItemStockDict[i]+=AddStockNumber
            file.close()
            rewriteStock()
            while True:
                try:
                    CurrentStock()
                    answer=int(input('''\nDo you want to add more?
1. Yes
2. No
Your Answer: '''))
                except:
                    print("\nInvalid Answer. Pls try again")
                    continue
                if answer == 1:
                    break
                elif answer == 2:
                    break
                else:
                    print("\nInvalid Answer. Pls try again")
    elif answer == 4:
        TurnintoDict()
        while True:
            if answer == 2:
                break
            DeleteStockItem=str(input("\nWhich Item would you like to remove stock: ")).capitalize()
            if DeleteStockItem not in ItemStockDict:
                print("\nStock does not exist!")
                break
            try:
                DeleteStockNumber=int(input("\nHow much: "))
            except:
                print("\nInvalid Answer. Pls try again")
                continue
            for i in ItemStockDict:
                if DeleteStockItem == i:
                    ItemStockDict[i]=int(ItemStockDict[i])
                    if ItemStockDict[i]-DeleteStockNumber<0:
                        print("\nThere is not enough",DeleteStockItem,"in inventory therefore can't minus")
                        break
                    else:
                        ItemStockDict[i]-=DeleteStockNumber
            file.close()
            rewriteStock()
            while True:
                try:
                    CurrentStock()
                    answer=int(input('''\nDo you want to minus more?
1. Yes
2. No
Your Answer: '''))
                except:
                    print("\nInvalid Answer. Pls try again")
                    continue
                if answer == 1:
                    break
                elif answer == 2:
                    break
                else:
                    print("\nInvalid Answer. Pls try again")
    elif answer == 5:
        TurnintoDict()
        print("\nItems Low in Stock (Less than 20)")
        print("Item\t\t||\tStock")
        for i in ItemStockDict:
            if ItemStockDict[i]<20:
                ItemStockDict[i]=str(ItemStockDict[i])
                print(i+"\t\t||\t"+ItemStockDict[i])
            else:
                continue
        while True:
            try:
                print('''\nGo back to main menu?
1. Yes''')
                answer=int(input("Your Answer: "))
                if answer==1:
                    break
            except:
                print("\nInvalid Answer. Try Again")
    elif answer == 6:
        break
    else:
        print("\nInvalid Answer. Try Again")
        continue
        
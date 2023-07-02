ItemStockDict={}
try:
    file=open("Stock.txt","x")
except:
    pass

def PrintingOutTheList(Item,Stock):
    if len(Item) >= 16:
        print(Item+"\t||\t"+Stock)
    elif len(Item) >= 8:
        print(Item+"\t\t||\t"+Stock)
    else:
        print(Item+"\t\t\t||\t"+Stock)

def RewriteTheFile(Item, Stock):
    file=open("Stock.txt","a+")
    if len(Item) >= 16:
        file.write(Item+"\t||\t"+Stock+"\n")
    elif len(Item) >= 8:
        file.write(Item+"\t\t||\t"+Stock+"\n")
    else:
        file.write(Item+"\t\t\t||\t"+Stock+"\n")

def AddItem(x,y):
    file=open("Stock.txt","a+")
    y=str(y)
    RewriteTheFile(x,y)
    file.close()

def PrintDescend():
    print("Item\t\t\t||\tStock")
    for i in DescendItemStockDict:
        Item=str(i)
        Stock=str(DescendItemStockDict[i])
        PrintingOutTheList(Item,Stock)

def rewriteDescend():
    file=open("Stock.txt","w+")
    for i in DescendItemStockDict:
        Item=str(i)
        Stock=str(DescendItemStockDict[i])
        RewriteTheFile(Item,Stock)
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
        RewriteTheFile(Item,Stock)
    file.close()

def CurrentStock():
    print("\nCurrent Items in Invetory")
    print("Item\t\t\t||\tStock")
    for i in ItemStockDict:
        ItemStockDict[i]=str(ItemStockDict[i])
        PrintingOutTheList(i,ItemStockDict[i])

while True:
    file=open("Stock.txt","r")
    file.seek(0)
    print("\nItem\t\t\t||\tStock")
    print(file.read())
    print('''
What do you wish to do?
1. Add a new item including its stock
2. Delete an item including its stock
3. View items in descending order of number of stocks
4. Add stocks to selected items
5. Delete stocks on selected items
6. View items low in stocks
7. Search for items and display its number of stocks left
8. Exit''')
    try:
        answer=int(input("Your Answer: "))
    except:
        print("\nInvalid Answer. Try Again")
        continue
    if answer == 1:
        TurnintoDict()
        while True:
            item=str(input("\nWhat item: ")).title()
            if item in ItemStockDict:
                print("Item is already in the list. Please try again.")
                continue
            try:
                stocks=int(input("\nHow much: "))
                AddItem(item,stocks)
                break
            except:
                print("\nInvalid Answer. Try Again")
    elif answer == 2:
        TurnintoDict()
        while True:
            item=str(input("\nWhat item: ")).title()
            if item not in ItemStockDict:
                print("Item doesn't exist. Please try again.")
                break
            else:
                answer = str(input("Are you sure? Answer yes or no: ")).capitalize()
                if answer == "Yes":
                    ItemStockDict.pop(item)
                    rewriteStock()
                    break
                elif answer == "No":
                    break
                else:
                    print("\nInvalid Answer. Try Again")
    elif answer == 3:
        TurnintoDict()
        Itemlist=list(ItemStockDict.items())
        l=len(Itemlist) 
        #bubble sort
        for i in range(l-1):
            for j in range(i+1,l):
                if Itemlist[i][1]<Itemlist[j][1]:
                    t=Itemlist[i]
                    Itemlist[i]=Itemlist[j]
                    Itemlist[j]=t
        DescendItemStockDict=dict(Itemlist)
        print("\nDescending Order of Items according to stocks")
        ItemStockDict={}
        while True:
            try:
                PrintDescend()
                answer=int(input('''
Do you wish to rewrite the file with this new order?
1. Yes
2. No
Your Answer: '''))
            except:
                print("\nInvalid Answer. Try Again")
                continue
            if answer == 1: 
                rewriteDescend()
                break
            elif answer ==2:
                break
            else:
                print("\nInvalid Answer. Try Again")
    elif answer == 4:
        TurnintoDict()
        while True: 
            if answer == 2:
                break
            AddStockItem=str(input("\nWhich Item would you like to add stock: ")).title()
            if AddStockItem not in ItemStockDict:
                print("\nStock does not exist! Add the name of the stock first.")
                break
            try:
                AddStockNumber=int(input("\nHow much: "))
                if AddStockNumber <= 0:
                    print("\nOnly numbers higher than 0. Try again")
                    continue
            except: 
                print("\nInvalid Answer. Pls try again")
                continue
            for i in ItemStockDict:
                if AddStockItem == i:
                    ItemStockDict[i]=int(ItemStockDict[i])
                    ItemStockDict[i]+=AddStockNumber
            rewriteStock()
            while True:
                try:
                    CurrentStock()
                    answer=int(input('''
\nDo you want to add more?
1. Yes
2. No
Your Answer: '''))
                    if answer == 1:
                        break
                    elif answer == 2:
                        break
                    else:
                        print("\nInvalid Answer. Pls try again")
                except:
                    print("\nInvalid Answer. Pls try again")
                    continue
    elif answer == 5:
        TurnintoDict()
        while True:
            if answer == 2:
                break
            DeleteStockItem=str(input("\nWhich Item would you like to remove stock: ")).title()
            if DeleteStockItem not in ItemStockDict:
                print("\nStock does not exist!")
                break
            try:
                DeleteStockNumber=int(input("\nHow much: "))
                if DeleteStockNumber <=0:
                    print("Only numbers higher than 0. Please try again")
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
            rewriteStock()
            while True:
                try:
                    CurrentStock()
                    answer=int(input(
'''\nDo you want to minus more?
1. Yes
2. No
Your Answer: '''))
                    if answer == 1:
                        break
                    elif answer == 2:
                        break
                    else:
                        print("\nInvalid Answer. Pls try again")
                except:
                    print("\nInvalid Answer. Pls try again")
                    continue
    elif answer == 6:
        TurnintoDict()
        print("\nItems Low in Stock (Less than 20)")
        print("Item\t\t\t||\tStock")
        for i in ItemStockDict:
            if ItemStockDict[i]<20:
                ItemStockDict[i]=str(ItemStockDict[i])
                PrintingOutTheList(i,ItemStockDict[i])
            else:
                continue
        while True:
            try:
                print("\nGo back to main menu?\n1. Yes")
                answer=int(input("Your Answer: "))
                if answer==1:
                    break
            except:
                print("\nInvalid Answer. Try Again")
    elif answer == 7:
        TurnintoDict()
        while True:
            if answer == 2:
                break
            StockToFind = str(input("\nWhat item do you wish to search for: ")).title()
            if StockToFind not in ItemStockDict:
                print("\nNo such stock is found. Please add them first.")
                break
            else:
                for i in ItemStockDict:
                    if StockToFind == i:
                        ItemStockDict[i]=str(ItemStockDict[i])
                        print("Item\t\t\t||\tStock")
                        PrintingOutTheList(i,ItemStockDict[i])              
                    else:
                        continue
                while True:
                    try:
                        answer = input(
'''\nDo you wish to search for other stocks?
1. Yes
2. No
Your Answer: ''')
                        answer=int(answer)
                        if answer == 1:
                            break
                        elif answer == 2:
                            break
                        else:
                            print("\nInvalid Answer. Please try again")
                            continue
                    except:
                        print("\nInvalid Answer. Please try again")
                        continue
    elif answer == 8:
        file.close()
        break
    else:
        print("\nInvalid Answer. Try Again")
        continue
        

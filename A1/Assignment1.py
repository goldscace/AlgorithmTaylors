def WhatToDo():
    print("\nEnter 0 to 5 for the following options: ")
    print("0 -> Issue new ticket number")
    print("1 -> Assign ticket in queue for bill payment to Counter 1")
    print("2 -> Assign ticket in queue for bill payment to Counter 2")
    print("3 -> Assign ticket in queue for bill payment to Counter 3")
    print("4 -> Assign ticket in queue for bill payment to Counter 4")
    print("5 -> Quit Program")
x=1000
y=2000
Bill=[]
License=[]
c1=["No Ticket"]
c2=["No Ticket"]
c3=["No Ticket"]
c4=["No Ticket"]

def CurrentCounter():
    print("\nTicket in queue for bill payment: ",Bill)
    print("Ticket in queue for license renew: ",License)
    print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,"\n")
    
WhatToDo()
while True:
    CurrentCounter()
    option=input("Enter your option: ")
    try:
        option=int(option)
    except:
        print("\nInvalid Number, pls try again")
        continue
    if option == 0:
        print("\nEnter 0 or 1 for the following options:")
        print("0 -> Bill payment")
        print("1 -> License renew\n")
        ticket=input("Enter your option: ")
        try:
            ticket=int(ticket)
        except:
            print("\nInvalid Number, pls try again")
            continue
        if ticket==0:
            x=x+1
            Bill.append(x)
        elif ticket==1:
            y=y+1
            License.append(y)
        else:
            print("\nInvalid Number, pls try again")
    elif option == 1:
        if Bill==[]:
            print("\nThere is no ticket in queue")
        else:
            c1=Bill.pop(0)
    elif option == 2:
        if Bill==[]:
            print("\nThere is no ticket in queue")
        else:
            c2=Bill.pop(0)
    elif option == 3:
        if License==[]:
            print("\nThere is no ticket in queue")
        else:
            c3=License.pop(0)
    elif option == 4:
        if License==[]:
            print("\nThere is no ticket in queue")
        else:
            c4=License.pop(0)
    elif option == 5: 
        print("\nQuiting Program...")
        break
    else:
        print("\nInvalid Number, pls try again")


    

 
print("Enter 0 to 5 for the following options: ")
print("0 -> Issue new ticket number")
print("1 -> Assign ticket in queue for bill payment to Counter 1")
print("2 -> Assign ticket in queue for bill payment to Counter 2")
print("3 -> Assign ticket in queue for bill payment to Counter 3")
print("4 -> Assign ticket in queue for bill payment to Counter 4")
print("5 -> Quit Program")
print(" ")
x=1000
y=2000
Bill=[]
License=[]
c1=[]
c2=[]
c3=[]
c4=[]

start=0

print("Ticket in queue for bill payment: ",Bill)
print("Ticket in queue for license renew: ",License)
print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
print("")

while start == 0:
    option=(input("Enter your option: "))
    try:
        option = int(option)
        if option == 0:
            print("")
            print("Enter 0 or 1 for the following options:")
            print("0 -> Bill payment")
            print("1 -> License renew")
            print("")
            ticket=(input("Enter your option: "))
            try:
                ticket =int(ticket)
                if ticket==0:
                    x=x+1
                    Bill.append(x)
                    print("")
                    print("Ticket in queue for Bill Payment: ",Bill)
                    print("Ticket in queue for License Renew: ",License)
                    print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
                    print("")
                elif ticket==1:
                    y=y+1
                    License.append(y)
                    print("")
                    print("Ticket in queue for Bill Payment: ",Bill)
                    print("Ticket in queue for License Renew: ",License)
                    print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
                    print("")
                else:
                    print("")
                    print("Invalid Number, pls try again")
                    print("Ticket in queue for Bill Payment: ",Bill)
                    print("Ticket in queue for License Renew: ",License)
                    print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
                    print("")
            except:
                print("")
                print("Invalid Number, pls try again")
                print("Ticket in queue for Bill Payment: ",Bill)
                print("Ticket in queue for License Renew: ",License)
                print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
                print("")
        elif option == 1:
            if Bill==[]:
                print("")
                print("There is no ticket in queue")
                print("Ticket in queue for Bill Payment: ",Bill)
                print("Ticket in queue for License Renew: ",License)
                print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
                print("")
            else:
                c1=Bill.pop(0)
                print("")
                print("Ticket in queue for Bill Payment: ",Bill)
                print("Ticket in queue for License Renew: ",License)
                print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
                print("")
        elif option == 2:
            if Bill==[]:
                print("")
                print("There is no ticket in queue")
                print("Ticket in queue for Bill Payment: ",Bill)
                print("Ticket in queue for License Renew: ",License)
                print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
                print("")
            else:
                c2=Bill.pop(0)
                print("")
                print("Ticket in queue for Bill Payment: ",Bill)
                print("Ticket in queue for License Renew: ",License)
                print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
                print("")
        elif option == 3:
            if License==[]:
                print("")
                print("There is no ticket in queue")
                print("Ticket in queue for Bill Payment: ",Bill)
                print("Ticket in queue for License Renew: ",License)
                print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
                print("")
            else:
                c3=License.pop(0)
                print("")
                print("Ticket in queue for Bill Payment: ",Bill)
                print("Ticket in queue for License Renew: ",License)
                print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
                print("")
        elif option == 4:
            if License==[]:
                print("")
                print("There is no ticket in queue")
                print("Ticket in queue for Bill Payment: ",Bill)
                print("Ticket in queue for License Renew: ",License)
                print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
                print("")
            else:
                c4=License.pop(0)
                print("")
                print("Ticket in queue for Bill Payment: ",Bill)
                print("Ticket in queue for License Renew: ",License)
                print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
                print("")
        elif option == 5:
            print("")  
            print("Quiting Program...")
            break
        else:
            print("")
            print("Invalid Number, pls try again")
            print("Ticket in queue for Bill Payment: ",Bill)
            print("Ticket in queue for License Renew: ",License)
            print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
            print("")
    except:
        print("")
        print("Invalid Number, pls try again")
        print("Ticket in queue for Bill Payment: ",Bill)
        print("Ticket in queue for License Renew: ",License)
        print("Tickets at counter: Counter 1:",c1," Counter 2:",c2," Counter 3:",c3," Counter 4:",c4,)
        print("")

    
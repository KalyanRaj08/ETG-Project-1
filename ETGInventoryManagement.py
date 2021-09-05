import json
import getpass
import datetime
import math

na=' '

def clrscr():
    print( "\n" * 100 )

def intro():
    clrscr()
    print("\n"*5)
    print('\t\t\tKK SUPERMARKET!!!!!!!')
    print('\t\t\tBy:Kalyan Rajkumar K')

def newuser():
    clrscr()
    print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
    print(chr(12)*80)
    f=0
    u = input('ENTER USERNAME:')
    p = input('ENTER PASSWORD:')
    fd = open("Accounts.json","r")
    t = fd.read()
    fd.close()
    acc = json.loads(t)
    for i in acc:
        if i == u:
            f=1
    if u == '!' or p == '!':
        f=1
        print('THE USERNAME or PASSWORD IS A RESTRICTED CHARACTER \n \t\t (OR)')
    if f==1 :
        print('USERNAME ALREADY EXISTS!!!!')
        enter = input('PRESS ENTER TO CONTINUE!!')
    else:
        acc[u]=p
        t=json.dumps(acc)
        fd = open("Accounts.json", "w")
        fd.write(t)
        fd.close()
        print("YOUR ACCOUNT HAS BEEN CREATED, SO KINDLY LOGIN IN FRONT PAGE")
        enter = input('PRESS ENTER TO CONTINUE!!')


def acclist():
    clrscr()
    print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
    print(chr(12) * 80)
    fd = open("Accounts.json", "r")
    t = fd.read()
    acc = json.loads(t)
    fd.close()
    for i in acc:
        print(i)
    enter = input('PRESS ENTER TO CONTINUE!!')

def delacc():
    fd = open("Accounts.json", "r")
    t = fd.read()
    fd.close()
    f=0
    acc = json.loads(t)
    acclist()
    h = input('ENTER ACCOUNT USERNAME TO BE DELETED:')
    f= acc.pop(h,'!')
    t= json.dumps(acc)
    fd = open("Accounts.json", "w")
    fd.write(t)
    fd.close()
    if f=='!':
        print('NO SUCH USER AVAILABLE!!!!!')
        enter = input('PRESS ENTER TO CONTINUE!!')
    else :
        print('ACOUNT DELETED SUCCESSFULLY!!!!')
        enter = input('PRESS ENTER TO CONTINUE!!')

def menu():
    clrscr()
    print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
    print(chr(12) * 80)
    ch=0
    while ch!=4:
        clrscr()
        print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
        print(chr(12) * 80)
        print('1.Admin')
        print('2.Customer order')
        print('3.Search for a Product')
        print('4.Signout')
        ch = input('Enter your choice :')
        try:
            ch = int(ch)
            if ch == 1:
                passi()
                break
            elif ch == 2:
                order()
            elif ch == 3:
                searfun()
            elif ch == 4:
                print('\t\t\tTHANK YOU!!')
                enter = input('PRESS ENTER TO QUIT!!')
                break
            else:
                print('Invalid option!!')
                enter = input('PRESS ENTER TO CONTINUE!!')
        except:
            print('Invalid option!!')
            enter = input('PRESS ENTER TO CONTINUE!!')

def login():
    clrscr()
    global na
    print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
    print(chr(12) * 80)
    fd = open("Accounts.json", "r")
    t = fd.read()
    acc = json.loads(t)
    u = input('\n\n\nUsername:')
    p1=acc.get(u,'!')
    p2 = input('\n\n\nPassword:')
    if p1==p2:
        na=u
        menu()
    elif p1=='!':
        print('\t\tUSERNAME DOSENT EXIST')
        enter = input('PRESS ENTER TO CONTINUE!!')
    else:
        print('\t\tUSERNAME AND PASSWORD DOSENT MATCH')
        enter = input('PRESS ENTER TO CONTINUE!!')
    fd.close()

def addfun():
    clrscr()
    print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
    print(chr(12) * 80)
    f1=0
    f2=0
    fd = open("Products.json", "r")
    t = fd.read()
    fd.close()
    prod = json.loads(t)
    try:
        pn = input('Enter product number:')
        n = input('Enter product name:')
        a = int(input('Enter number of products available:'))
        p = float(input('Enter product price:'))
        d = float(input('Enter product discount rate:'))
        e = datetime.datetime.now()
        day = e.strftime("%Y-%m-%d %H:%M:%S")
        for i in prod:
            if pn == i:
                f1 = 1
            j = prod.get(i)
            if n == j.get('name'):
                f2 = 1
        if f1 == 1:
            print('PRODUCT ID ALREADY EXISTS!!!! CANNOT ADD ITEM!!!')
            enter = input('PRESS ENTER TO CONTINUE!!')
        elif f2 == 1:
            print('PRODUCT NAME ALREADY EXISTS!!!! CANNOT ADD ITEM!!!')
            enter = input('PRESS ENTER TO CONTINUE!!')
        else :
            dic={}
            dic['name'] = str(n)
            dic['avail'] = str(a)
            dic['price'] = str(p)
            dic['disc'] = str(d)
            dic['day'] = str(day)
            prod[str(pn)] = dic
            t = json.dumps(prod)
            fd = open("Products.json", "w")
            fd.write(t)
            fd.close()

    except:
        print('\t\tINVALID INPUT, TRY AGAIN!!!!')
        enter = input('PRESS ENTER TO CONTINUE!!')

def listfun():
    clrscr()
    print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
    print(chr(12) * 80)
    fd = open("Products.json", "r")
    t = fd.read()
    prod = json.loads(t)
    for i in prod:
        print('Product Number :',i)
        j=prod.get(i)
        print('Product Name :', j.get('name'))
        print('Product Availaility :',j.get('avail'))
        print('Product Price:',j.get('price'))
        print('Product Discount Value(In Rupees) :',j.get('disc'))
        print('Product Latest Stock-In Date :',j.get('day'))
        print()
    fd.close()

def delfun():
    listfun()
    fd = open("Products.json", "r")
    t = fd.read()
    fd.close()
    prod = json.loads(t)
    h = input("ENTER PRODUCT NAME TO BE DELETED :")
    f=0
    for i in prod:
        if prod[i]['name'] == h:
            pid = i
            f = 1
    if f==1:
        prod.pop(str(pid))
        t= json.dumps(prod)
        fd = open("Products.json", "w")
        fd.write(t)
        fd.close()
        print('\t\tPRODUCT REMOVED!!!!')
        enter = input('PRESS ENTER TO CONTINUE!!')

    else:
        print('\t\tPRODUCT DOESNT EXIST, TRY AGAIN!!!!')
        enter = input('PRESS ENTER TO CONTINUE!!')

def searfun():
    listfun()
    fd = open("Products.json", "r")
    t = fd.read()
    fd.close()
    prod = json.loads(t)
    h = input("ENTER PRODUCT NAME TO BE SEARCHED :")
    f=0
    for i in prod:
        if prod[i]['name'] == h:
            print('Product Number :', i)
            j = prod.get(i)
            print('Product Name :', j.get('name'))
            print('Product Availaility :', j.get('avail'))
            print('Product Price:', j.get('price'))
            print('Product Discount Value(In Rupees) :', j.get('disc'))
            print('Product Latest Stock-In Date :', j.get('day'))
            print()
            f = 1
    if f==1:
        enter = input('PRESS ENTER TO CONTINUE!!')

    else:
        print('\t\tPRODUCT DOESNT EXIST, TRY AGAIN!!!!')
        enter = input('PRESS ENTER TO CONTINUE!!')

def order():
    listfun()
    fz = open("Sales.json", "r")
    t1 = fz.read()
    fz.close()
    sales = json.loads(t1)
    fd = open("Products.json", "r")
    t = fd.read()
    fd.close()
    prod = json.loads(t)
    ch = 'y'
    f1=0
    f2=0
    ord = {}
    while ch=='y':
        pr = input('Enter product you want to buy :')
        n = int(input('Enter required number of product selected :'))
        for i in prod:
            if prod[i]['name'] == pr:
                pid = i
                f1 = 1
            if int(prod[i]['avail']) - n >=  0:
                f2 = 1
        if f1 ==1 and f2==1:
            ord[pid] = n

        elif f1 == 0:
            print('\t\tPRODUCT NAME DOESNT EXIST!!!!')
            enter = input('PRESS ENTER TO CONTINUE!!')
        elif f2 == 0:
            print('\t\tSADLY THAT MUCH PRODUCT IS NOT AVAILABLE IN OUR INVENTORY!!!!!')
            enter = input('PRESS ENTER TO CONTINUE!!')
        ch = input('Do you want to continue (Enter y to order another product): ')
    bill = {}
    clrscr()
    print('\t\t\t BILL')
    print('User:', na)
    s = 0.0
    print('{:<15}'.format('Product ID'), '|', '{:<15}'.format('Product name'), '|', '{:<15}'.format('Quantity'), '|', '{:<15}'.format('Price'))
    item = []
    quant = []
    for k in ord:
        for i in prod:
            j = prod.get(i)
            if k == i:
                prod[i]['avail'] = int(prod[i]['avail']) - n
                z = (float(prod[i]['price']) - float(prod[i]['disc'])) * n
                print('{:<15}'.format(i), '|', '{:<15}'.format(j.get('name')), '|', '{:<15}'.format(n), '|', '{:<15}'.format(z))
                item.append(j.get('name'))
                quant.append(int(n))
                s+=z
    bill['uname'] = na
    bill['total'] = float(s)
    bill['item'] = item
    bill['quant'] = quant
    print("TOTAL AMOUNT           : ", s)
    enter = input('PRESS ENTER TO CONTINUE!!')
    e = datetime.datetime.now()
    day = e.strftime("%Y-%m-%d %H:%M:%S")
    sales[str(day)] = bill
    t1 = json.dumps(sales)
    fz = open("Sales.json", "w")
    fz.write(t1)
    fz.close()
    t = json.dumps(prod)
    fd = open("Products.json", "w")
    fd.write(t)
    fd.close()

def billist():
    clrscr()
    print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
    print(chr(12) * 80)
    fz = open("Sales.json", "r")
    t1 = fz.read()
    sales = json.loads(t1)
    for i in sales:
        print('USER NAME : ', sales[i]['uname'])
        print('DATE :',i)
        print('BILL PRICE : ', sales[i]['total'])
        print('ITEMS:-')
        for j in range(len(sales[i]['item'])):
            print('{:<20}'.format(sales[i]['item'][j]), '\t\t', '{:<20}'.format(sales[i]['quant'][j]))
        print('\n')
    enter = input('PRESS ENTER TO CONTINUE!!')
    fz.close()

def adminfun():
    clrscr()
    print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
    print(chr(12) * 80)
    ch=0
    while ch!=5:
        clrscr()
        print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
        print(chr(12) * 80)
        print('1.Add Product')
        print('2.Remove Product')
        print('3.Search for a Product')
        print('4.See bill list')
        print('5.Back to main menu')
        ch=input('Enter your choice:')
        try:
            ch=int(ch)
            if ch==1:
                addfun()
            elif ch==2:
                delfun()
            elif ch==3:
                searfun()
                enter = input('PRESS ENTER TO CONTINUE!!')
            elif ch==4:
                billist()
            elif ch==5:continue
            else:
                print('Invalid Option!!')
                enter=input('PRESS ENTER TO CONTINUE!!')
        except:
            print('Invalid Option!!')
            enter=input('PRESS ENTER TO CONTINUE!!')

def passi():
    clrscr()
    print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
    print(chr(12) * 80)
    p=''
    pa=input('Admin Password :')
    if pa == p:
        adminfun()
    else:
        print('WRONG PASSWORD ONLY ADMINS ARE ALLOWED!!')
        enter=input('PRESS ENTER TO CONTINUE!!')

intro()
enter=input('PRESS ENTER TO CONTINUE!!')
clrscr()
print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
print(chr(12) * 80)
ch=0
while ch!=4:
    clrscr()
    print('\t\tKK SUPERMARKET WELCOMES YOU!!!')
    print(chr(12) * 80)
    print('1.New to login')
    print('2.Already have an account')
    print('3.Delete account')
    print('4.Exit')
    ch=input('Enter your choice:')
    try:
        ch=int(ch)
        if ch==1:newuser()
        elif ch==2:login()
        elif ch==3:delacc()
        elif ch==4:
            intro()
            print('\t\t\tTHANK YOU FOR USING THIS APP')
            enter=input('PRESS ENTER TO CONTINUE!!')
        else:
            print('Invalid option')
            enter=input('PRESS ENTER TO CONTINUE!!')
    except:
            print('Invalid option')
            enter=input('PRESS ENTER TO CONTINUE!!')
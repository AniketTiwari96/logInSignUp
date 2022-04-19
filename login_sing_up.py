import json
dct={}
while True:
    print('\33[93m',"press 1 for sing_up\npress 2 for sing_in\npress 3 for update\npress 4 delet\npress 5for exit",'\33[0m')
    def sing_up():
        try:
            with open("login_sing_up.json","r")as fobj:
                r=json.load(fobj)
                print(r)
                n=input("enter your gmail id: ")
                if "@" in n:
                    with open("login_sing_up.json","w")as fobj2:
                        dct[n]={"name":input("enter your name: "),
                        "password":int(input("enter your password: ")),
                        "phoon_number":int(input("enter your phoon number: "))}
                        json.dump(dct,fobj2,indent=4)
                else:
                    print("your email not right: ")
        except:
            n=input("enter your gmail id :")
            
            if "@" in n:
                with open("login_sing_up.json","w")as fobj:
                    dct[n]={"name":input("enter your new name: "),
                    "password":int(input("enter your new password: ")),
                    "phoon_number":int(input("enter your new phoon nnumber"))}                    
                    json.dump(dct,fobj,indent=4)
            else:
                print("gmail not right: ")   

    def sing_in():
        try:
            with open("login_sing_up.json","r")as fobj:
                r=json.load(fobj)
                # print("this is your data",r)
                n=input("enter your your gmail id: ")
                p=int(input("enter your password: "))
                if n in r:
                    if p==r[n]['password']:
                        print(r[n])
                    else:
                        print("this password is not right: ")
                else:
                    print("this gmail id not exit: ")
        except:
            print("plese create your account before sing in: ")
    
    def update():
        try:
            with open("login_sing_up.json","r")as fobj:
                r=json.load(fobj)
                n=input("enter your gmail id: ")
                p=int(input("enter your password: "))
                if n in r:
                    if p ==r[n]['password']:
                        with open("login_sing_up.json","w")as fobj1:
                            dct[n]={"name":input("enter your name:"),"password":int(input("enter your password: ")),"phoon_number":int(input("enter your phoon number: "))}
                            json.dump(dct,fobj1,indent=4)
                    else:
                        print("your password not right: ")
                else:
                    print("your gmail id not exit: ")
        except:
              print("plese create your account before sing in: ")


    def delet():
        try:
            n=input("enter your gmail id: ")
            with open("login_sing_up.json","r")as fobj:
                r=json.load(fobj)
                if n in r:
                    with open('pra.json','w') as fobj1:
                        r.pop(n)
                        json.dump(r,fobj1,indent=4)
                    print("data deleted: ")
                
                else:
                    print("this gmail id not right: ")
        except:
            print("plese create your account before sing in: ")

    choice=int(input("plese enter your choice :"))
    if choice==1:
        sing_up()
    if choice==2:
        sing_in()
    if choice==3:
        update()
    if choice==4:
        delet()
    if choice==5:
        break

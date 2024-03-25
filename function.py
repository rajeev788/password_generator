def login ():
     username=input("enter your user name")
     password=input("enter your password")
     data={"raj":"123"}
     if username in data and data[username] == password:
         print("login sucessfull")
         calculator()

     else:
        print("login not sucessful")

def calculator():
        count="y"
        while count=="y":
                        a= int(input("enter the first number"))
                        b= int(input("enter the second number"))
                        c= input("which operation you want to perform (add/subtract/divide/multiply)")
                        d=["add","subtract","multiply","divide"]
                        if(c  not in d):
                         print("you enterd the wrong operation ")
                
                        if c=="add":
                                print(a+b)
                        elif c=="subtract":
                         print(a-b)
                        elif c=="multiply":
                         print(a*b)
                        elif c=="subtract":
                         print(a-b)
                        elif c=="divide":
                                  print(a/b)
                        count=input("do you want to run the calculator again")
                        if count=="n":
                                break

login()


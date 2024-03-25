while True:
        try:
                a=float(input('enter the first no:'))
                b=float(input('enter the second no:'))
                break
        except:
                print("invalid login")
c=input('enter the operation u want to perform(+,-,*,/):')
d=['-','+','*','/']
 
while c not in d:
    print("you entered the wrong operation")
    break
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="_":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="*":
    print(a/b)

    #ask the user i fhe  wants to  to run the calculator again 
    
    #if he waants to run calculator again run it from the start else end the calculator
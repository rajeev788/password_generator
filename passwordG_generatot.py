from curses.ascii import isalnum, isalpha
import random

pp = ["a","A","#","$","*","^","&","H","J","P","R","q","e","y","i","@","G","k","s","I","X","v","/","[","]","|","w"]

def passw():
    a = input("Type ['c' to check a passwords strength] and ['g' to generate a new password]: ")
    if a == "c":
        a1 = input("Type the password: ")
        check(a1)
    elif a == "g":
        a2 = generate()
        print(f"Your new generated password: {a2}")

def generate():
    i = 0
    a4 = ""
    while i < 8:
        a2 = random.randrange(0,20)
        a3 = random.choice(pp)
        a4 += str(a2) + a3
        i+=1
    return a4

def check(p):
    a1 = 0
    a2 = 0
    for i in p:
        if i.isdigit():
            a1 += 1
        elif i.isalpha():
            a2 += 1
    
    if a1 <= 2 and a2 >=12:
        print("Your password is weak")
    elif a1 <= 4 and a2 >= 10:
        print("Your password is fine")
    elif a1 <= 6 and a2 >= 8:
        print("Your password is strong boi")


passw()
generate()
check()

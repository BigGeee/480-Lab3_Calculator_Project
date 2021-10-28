# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 13:51:12 2021

@author: georg
"""






def inputnum():
    input1 = float(input("Enter your first number: "))
    input2 = float(input("Enter your second number: "))
    inputs = [input1,input2]
    return inputs

add = lambda x,y: x+y

sub = lambda x,y: x-y

mult = lambda x,y: x*y

div = lambda x,y : x/y


    


while 1 > 0:
    cmd = input("Would yo like to do additon, subtraction, multiplication, or division, or quit? Enter +,-,*,/, or '!q' to quit:    ")
    if cmd == "!q":
        break  
    elif cmd == "+":
        i = inputnum()
        num = add(i[0], i[1])
        print(i[0], " + ", i[1], " = ", num)
    elif cmd == "-":
        i = inputnum()
        num = sub(i[0], i[1])
        print(i[0], " - ", i[1], " = ", num)
    elif cmd == "*":
        i = inputnum()
        num = mult(i[0], i[1])
        print(i[0], " * ", i[1], " = ", num)
    elif cmd == "/":
        i = inputnum()
        num = div(i[0], i[1])
        print(i[0], " / ", i[1], " = ", num)
    else:
        print("Error, input is invalid")
    

        

                
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:25:22 2021

@author: georg
"""

operators = {
        "+",
        "-",
        "*",
        "/",
        "^",
        "~",
        "sin",
        "cos",
        "tan",
        "cot",
        "arcsin",
        "arccos",
        "arctan",
        "arcctn",
        "log",
        "ln"
        "."
        }
leftAsscoc = {"+","-","*","/"}
rightAssoc = {
        "~",
        "."
        "sin",
        "cos",
        "tan",
        "cot",
        "arcsin",
        "arccos",
        "arctan",
        "arcctn",
        "log",
        "ln"}

priority = {
    
        "~": 4, #negative operator
        ".": 4,
        "(": 4,
        ")": 4,
        "^": 3,
        "sin":2,
        "cos":2,
        "tan":2,
        "cot":2,
        "arcsin":2,
        "arccos":2,
        "arctan":2,
        "arcctn":2,
        "log":2,
        "ln":2,
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
        
}




def shuntingYard(string):
    output = []
    stack = []
    funct = ""
    digit = ""
    i= 0
    
    while i < len(string):
        functionAdd = False
        digitAdd = False
        decFound = False
        currChar = string[i]
        if currChar == " ":
            continue
        elif currChar.isdigit():
            tempChar = currChar
            if i == len(string)-1:
                digit += tempChar
            else:
                while tempChar.isdigit() or tempChar == ".":
                    if tempChar == "." and decFound == True:
                        raise Exception("Error: Nested Decimal Found")
                    if tempChar == "." and decFound == False:
                        decFound = True
                    digit += tempChar
                    i += 1
                    digitAdd == True
                    if i == len(string):
                       break
                    else:
                       tempChar = string[i]
                i -= 1 # i dont know why but this makes the program work
                
            output.append(digit)
            digit = ""
            decFound = False
            
        elif currChar.isalpha():
            tempChar = currChar
            while tempChar.isalpha():
                funct += tempChar
                i += 1
                if i == len(string)-1:
                    break
                else:
                    tempChar = string[i]
            print(funct)
            if funct in operators:
                stack.append(funct)
                functionAdd = True
                funct = ""
            else:
                raise Exception("Error: Unknown Fucntion!")
                
        elif currChar in operators:
            
            op1 = currChar
            
            while len(stack) > 0:
                op2 = stack[-1]  
                if op2 in operators and (op1 in leftAsscoc and (priority[op1] <= priority[op2])) or (op1 in rightAssoc and (priority[op1] < priority[op2])):
                    output.append(stack.pop())
                else:
                    break
            stack.append(op1)
        elif currChar == "(":
            stack.append(currChar)
        elif currChar == ")":
            foundLeft = False
            
            while len(stack) > 0:
                curr = stack.pop()
                if curr == "(":
                    foundLeft = True
                    break
                else:
                    output.append(curr)
            if(foundLeft == False):
                raise Exception("Parenthesis mismatched")
        else:
            raise Exception("Unknown token: ", currChar)
            
        if(functionAdd == False and digitAdd == False):
            i += 1
            
    while len(stack) > 0:
        temp = stack.pop()
        if temp == "(" or temp == ")":
            raise Exception("Parenthesis mismatched")
        output.append(temp)
    return output
                
print(shuntingYard("8.3+1"))           
                
print(shuntingYard("1+8.3")) 



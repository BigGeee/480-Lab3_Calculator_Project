# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:25:22 2021

@author: georg
"""

operators = {"+","-","*","/","^","~"}
functions = { 
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
        }
leftAsscoc = {"+","-","*","/"}
rightAssoc = {"~"}

priority = {
    
        "~": 4,
        "(": 3,
        ")": 3,
        "^": 3,
        "sin": 3,
        "cos": 3,
        "tan": 3,
        "cot": 3,
        "arcsin": 3,
        "arccos": 3,
        "arctan": 3,
        "arcctn": 3,
        "log": 3,
        "ln": 3,
        "*": 2,
        "/": 2,
        "%": 2,
        "+": 1,
        "-": 1,
}




def shuntingYard(string):
    output = []
    stack = []
    funct = ""
    i= 0
    
    while i < len(string):
        functionAdd = False
        currChar = string[i]
        
        if currChar == " ":
            continue
        elif currChar.isdigit():
            output.append(currChar)
        elif currChar.isalpha():
            tempChar = currChar
            while tempChar.isalpha():
                funct += tempChar
                i += 1
                tempChar = string[i]
            if funct in functions:
                stack.append(funct)
                functionAdd = True
                funct = ""
                
            
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
            
        if(functionAdd == False):
            i += 1
    while len(stack) > 0:
        temp = stack.pop()
        if temp == "(" or temp == ")":
            raise Exception("Parenthesis mismatched")
        output.append(temp)
    return " ".join(output)
                
print(shuntingYard("sin21"))           
                

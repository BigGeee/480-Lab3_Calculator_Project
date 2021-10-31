# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:25:22 2021

@author: georg
"""

import math

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
        "ln",
        }
functions = {
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
        "ln",
    }
leftAsscoc = {"+","-","*","/"}
rightAssoc = {
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
        }

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
        elif currChar.isdigit() or currChar == ".":
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
                i -= 1 
            if digit == ".":
                raise Exception("Error: Lone Decimal Point Found")
            output.append(str(float(digit)))
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
            if funct in operators:
                stack.append(funct)
                functionAdd = True
                funct = ""
            else:
                raise Exception("Error: Unknown Fucntion!", funct)
                
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
                


#evaluation function based off code found from https://www.techiedelight.com/evaluate-given-postfix-expression/

def evalPostfix(exp):
    """
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
        "ln",
 """
    # base case
    if not exp:
        exit(-1)
 
    # create an empty stack
    stack = []
 
    # traverse the given expression
    for ch in exp:
 
        # if the current is an operand, push it into the stack
        if ch.replace(".","",1).isdigit():
            stack.append(float(ch))
        elif ch in functions:
            x = stack.pop()
            if ch == "~":
                stack.append(x * -1)
            if ch == "sin":
                stack.append(math.sin(x))
            elif ch == "cos":
                stack.append(math.cos(x))
            elif ch == "tan":
                stack.append(math.tan(x))
            elif ch == "cot":
                stack.append((math.cos(x)/math.sin(x)))
            elif ch == "arcsin":
                stack.append(math.asin(x))
            elif ch == "arccos":
                stack.append(math.acos(x))
            elif ch == "arctan":
                stack.append(math.atan(x))
            elif ch == "arcctg":
                stack.append((math.acos(x)/math.asin(x)))
            elif ch == "log":
                stack.append(math.log10(x))
            elif ch == "ln":
                stack.append(math.log(x))
        # if the current is an operator
        else:
            # remove the top two elements from the stack
            x = stack.pop()
            y = stack.pop()
 
            # evaluate the expression 'x op y', and push the
            # result back to the stack
            if ch == '+':
                stack.append(y + x)
            elif ch == '-':
                stack.append(y - x)
            elif ch == '*':
                stack.append(y * x)
            elif ch == '/':
                stack.append(y // x)
            elif ch == "^":
                stack.append(pow(y,x))
    
 
    # At this point, the stack is left with only one element, i.e.,
    # expression result
    return stack.pop()

#test statement
#~5.78+~(4-2.23)+sin(0)*cos(1)/(1+tan(2*~ln(~3+2*(1.23+arcsin(1)))))

while 1 > 0:
    userinput = input("Please Input a Valid Math Expression: ")
    if "exit" in userinput:
        break
    else:
        evalui = shuntingYard(userinput)
        print("= ",evalPostfix(evalui))

#Below is the Code that defines arithmatic operations of the calculator written in python.

#Definition for addition function

def add(x,y): 
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("provided both the inputs should be numeric")  
    return x+y

#Defintion for Subtraction function

def subtract(x,y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("provided both the inputs should be numeric")
    return x-y

#Definition for Multiplication function

def multiply(x,y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("provided both the inputs should be numeric")
    return x * y

#Defintion for Division Function

def divide(x,y):
    if y==0:
        return "Infinite result !! Division by zero NOT POSSIBLE"
    else:
        return x / y 
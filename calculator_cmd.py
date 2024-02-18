def calculator(a,b,c):
    if (c=="+"):
        return a+b
    elif(c=="-"):
        return a-b
    elif(c=="/"):
        return a/b
    elif(c=="*"):
        return a*b
    else:
        return "Select valid arithmetic operator"
a=float(input("Enter the first value: "))
b=float(input("Enter the second value: "))
c=input("Enter the arithmetic operation + or - or / or *: ")
print(calculator(a,b,c))    

    


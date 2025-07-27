a = float(input("enter the first number "))
op = input("enter the oprator (+,-,*,/)")
b = float(input("enter the second number "))

if op == '+':
    print("answer",a+b)
elif op == '-':
    print("answer",a-b) 
elif op == '*':
    print("answer",a*b)
elif op == '/':
    print("answer",a/b)  
else:
    raise ValueError(f"Invalid operator '{op}'. Please use +, -, * or /")








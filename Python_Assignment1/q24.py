# 24
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

op = input("Enter operator +,-,/,*: ")

if op == '+':
    print("Sum: ", num1+num2)
elif op == '-':
    print("Difference: ", num1-num2)
elif op == '*':
    print("Product: ", num1*num2)
elif op == '/':
    print("Quotient of ",num1,"/",num2,": ",  num1/num2)
    print("Quotient of ", num2, "/", num1, ": ", num2 / num1)
else:
    print("Invalid operator")

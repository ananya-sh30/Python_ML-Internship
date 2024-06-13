import math
# 3
# (Method 1)

x = int(input("Enter number: "))
print(math.factorial(x))

# (Method2)
fact = 1
for i in range(1, x+1):
    fact = fact*i
print("Factorial: ", fact)

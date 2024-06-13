# 11
n = int(input("Enter value of n: "))
num1 = 0
num2 = 1
sum = 0
print(num1, num2, sep=" ", end=" ")
for i in range(n-2):
    sum = num1 + num2
    print(sum, end=" ")
    num1 = num2
    num2 = sum
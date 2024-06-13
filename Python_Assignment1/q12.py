
# 12
num = int(input("Enter number: "))
sumOfDigits = 0
while num > 0:
    digi = num % 10
    sumOfDigits += digi
    num //= 10
print("Sum of digits is: ", sumOfDigits)
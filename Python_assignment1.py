import math
from datetime import date
import csv

# 1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum is: ", num1+num2)

# 2
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3
# (Method 1)

x = int(input("Enter number: "))
print(math.factorial(x))

# (Method2)
fact = 1
for i in range(1, x+1):
    fact = fact*i
print("Factorial: ", fact)


# 4
name = input("Name?: ")
print("Hello and welcome " + name)

# 5
str = input("Enter to write: ")
file1 = open("demoConnect.txt", 'w')
print("Input string: " + str, file=file1)

# 6
fileRead = open("demoConnect.txt", 'r')
print(fileRead.read())

# 7
str = input("Enter string: ")
print("Length: ", len(str))

# 8
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Result: ", str1+str2)

# 9
str = input("Enter string: ")
sub = input("Enter substring to check: ")

if sub in str:
    print("Present")
else:
    print("Absent")

# 10
str = input("Enter string: ")
print(str.upper())

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


# 12
num = int(input("Enter number: "))
sumOfDigits = 0
while num > 0:
    digi = num % 10
    sumOfDigits += digi
    num //= 10
print("Sum of digits is: ", sumOfDigits)

# 13
year = int(input("Enter birth year: "))
currDate = date.today()
currYear = currDate.year
age = currYear - year
print("Age: ", age)

# 14
str1 = input("Line: ")
print(str1)
while str1:
    str1 = input("Line: ")
    print(str1)

# 15
with open('file1.csv', newline='') as file1:
    csvFile = csv.reader(file1)
    for row in csvFile:
        print(row)

# 16
str = input("Enter string: ")
dictOfChr = {}
for i in str:
    if i not in dictOfChr:
        dictOfChr[i] = str.count(i)
        
print(dictOfChr)

# 17
str = input("Enter string: ")
print(str.title())


# 18
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
check = True
if len(str1) == len(str2):
    for i in str1:
        if str1.count(i) == str2.count(i):
            continue
        else:
            print("They are not anagrams")
            check = False
            break
    if check:
        print("They are anagrams")
else:
    print("They are not anagrams")

# 19
str = input("Enter string: ")
str2 = ""
for i in str:
    if ord('a') <= ord(i) <= ord('z'):
        str2 = str2+i

    if ord('A') <= ord(i) <= ord('Z'):
        str2 = str2 + i

    if ord('0') <= ord(i) <= ord('9'):
        str2 = str2 + i

    if i == " ":
        str2 = str2 + i
    else:
        continue

str = str2
print("New string: ", str)

# 20
li = list(input("Enter elements for list: "))
sum = 0;
for i in li:
    sum += int(i)
print("Sum: ", sum)

# 21
li = []
size = int(input("Enter size of list: "))
for i in range(size):
    x = int(input("Enter element to add in the list: "))
    li.append(x)

print(li)
ele = int(input("Enter element to count: "))
print("Count is: ", li.count(ele))

# 22
li = []
size = int(input("Enter size of list: "))
for i in range(size):
    x = int(input("Enter element to add in the list: "))
    li.append(x)

print(li)

print("Max element: ", max(li))
print("Min element: ", min(li))

# 23
unit = input("Unit? Enter C for celsius and F for fahrenheit: ")
temp = int(input("Enter temperature: "))
if unit == 'C' or unit == 'c':
    fah = (temp*9)/5 + 32
    print("Temperature in fahrenheit: ", fah)
elif unit == 'F' or unit == 'f':
    cel = ((temp-32)*5)/9
    print("Temperature in celsius: ", cel)
else:
    print("Invalid unit")

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

# 25
file1 = open("file1.txt", 'r')
file2 = open("file2.txt", 'a')
for i in file1:
    file2.write(i)
    
print("Content copied")

# 26
# (Method 1)
str = input("Enter a string: ")
start = input("Check for prefix: ")
end = input("Check for suffix: ")
if str.startswith(start):
    print("Suffix found")
else:
    print("Suffix not found")

if str.endswith(end):
    print("Prefix found")
else:
    print("Prefix not found")

# (Method 2)
str = input("Enter a string: ")
start = input("Check for prefix: ")
end = input("Check for suffix: ")
stLen = len(start)
enLen = len(end)

if str[:stLen] == start:
    print("Suffix found")
else:
    print("Suffix not found")
if str[-enLen:] == end:
    print("Prefix found")
else:
    print("Prefix not found")

# 27
str = input("Enter a string: ")
li = list(str)
print("List is: ", li)


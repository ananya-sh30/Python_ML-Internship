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
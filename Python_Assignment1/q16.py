# 16
str = input("Enter string: ")
dictOfChr = {}
for i in str:
    if i not in dictOfChr:
        dictOfChr[i] = str.count(i)
        
print(dictOfChr)
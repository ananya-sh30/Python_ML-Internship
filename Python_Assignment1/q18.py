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
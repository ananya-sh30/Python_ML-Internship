# 21
li = []
size = int(input("Enter size of list: "))
for i in range(size):
    x = int(input("Enter element to add in the list: "))
    li.append(x)

print(li)
ele = int(input("Enter element to count: "))
print("Count is: ", li.count(ele))
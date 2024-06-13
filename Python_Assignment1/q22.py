# 22
li = []
size = int(input("Enter size of list: "))
for i in range(size):
    x = int(input("Enter element to add in the list: "))
    li.append(x)

print(li)

print("Max element: ", max(li))
print("Min element: ", min(li))
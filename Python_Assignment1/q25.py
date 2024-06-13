# 25
file1 = open("file1.txt", 'r')
file2 = open("file2.txt", 'a')
for i in file1:
    file2.write(i)
    
print("Content copied")
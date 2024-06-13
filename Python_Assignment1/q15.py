import csv
# 15
with open('file1.csv', newline='') as file1:
    csvFile = csv.reader(file1)
    for row in csvFile:
        print(row)
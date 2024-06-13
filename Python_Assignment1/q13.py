from datetime import date

# 13
year = int(input("Enter birth year: "))
currDate = date.today()
currYear = currDate.year
age = currYear - year
print("Age: ", age)

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
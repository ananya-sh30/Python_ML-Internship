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

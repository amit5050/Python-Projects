import math

arrays = int(input("Enter your number: "))
dup_or_not = str(input("Do you Duplicate numbers or odd numbers?(dup / odd) "))

if dup_or_not == "odd":
    for x in range(arrays):
        if (x%2==1):
            print(x)

elif dup_or_not == "dup":
    for x in range(arrays + 2):
        if (x%2==0):
            print(x) 
    
else:
    for x in range(arrays + 1):
        print(x)

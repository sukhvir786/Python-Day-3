"""
    Program to find sum of the digits
    Part 2
"""
SUM = 0
n = int(input("Enter any integer value : "))
while n!=0:
    rem = n%10
    SUM = SUM + rem
    n = n//10
    if n==0 and SUM>9:
        n = SUM
        SUM = 0
print("Sum of the digits : ",SUM)

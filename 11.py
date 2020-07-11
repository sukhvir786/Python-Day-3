"""
    Program to find sum of the digits
"""
SUM = 0
n = int(input("Enter any integer value : "))
while n!=0:
    rem = n%10
    SUM = SUM + rem
    n = n//10
print("Sum of the digits : ",SUM)

"""
    Harshad Number
"""
SUM = 0
n = int(input("Enter any integer value : "))
m = n
while n!=0:
    rem = n%10
    SUM = SUM + rem
    n = n//10
print("Sum of the digits : ",SUM)
if m%SUM == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")
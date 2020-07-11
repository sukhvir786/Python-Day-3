"""
    Armstrong Number
"""
SUM = 0
n = int(input("Enter any integer value : "))
m = n
while n!=0:
    rem = n%10
    SUM = SUM + rem*rem*rem
    n = n//10
print("Sum of the digits : ",SUM)
if m == SUM:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
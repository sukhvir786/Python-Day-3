"""
Reverse of a number
"""
rev = 0
n = int(input("Enter any number"))
while n!=0:
    rev = rev*10
    rev = rev + n%10
    n = n//10
print("Rev of the number is : ",rev)
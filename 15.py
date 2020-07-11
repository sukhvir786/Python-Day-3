"""
    Palindrom number
"""
rev = 0
n = int(input("Enter any number : "))
m = n
while n!=0:
    rev = rev*10
    rev = rev + n%10
    n = n//10
print("Rev of the number is : ",rev)
if m==rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
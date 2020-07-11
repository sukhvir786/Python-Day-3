"""
    program to find factorial of a number
    using for loop
"""
fact = 1
n = int(input("enter any number : "))
for i in range(1,n+1):
    fact = fact*i
print("Factorial of the number is : ",fact)
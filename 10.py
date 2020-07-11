"""
    Fibonacci Series
"""
n = int (input("enter count : "))
print("Fibonacci Series: ")
a = 0
b = 1
print(a,b,end=" ")
for i in range(2,n):
    c = b+a
    print(c,end=" ")
    a = b
    b = c
    

"""
    patterns in python part 2
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="   ")
    print(" ")
print()

for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end="   ")
    print(" ")
print()

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="   ")
    print(" ")
print()
        
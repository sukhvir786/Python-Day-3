"""
    patterns in python part 3
"""
print("")
for i in range(1,6):
    for j in range(1,6):
        if i == j:
            print(j,end='  ')
        else:
            print(" ",end='  ')
    print(" ")
print("")
for i in range(1,6):
    for j in range(1,6):
        if i != j:
            print(j,end='  ')
        else:
            print(" ",end='  ')
    print(" ")
print("")
for i in range(1,6):
    for j in range(1,6):
        if i+j == 6:
            print(j,end='  ')
        else:
            print(" ",end='  ')
    print(" ")
print("")
for i in range(1,6):
    for j in range(1,6):
        if i+j != 6:
            print(j,end='  ')
        else:
            print(" ",end='  ')
    print(" ")
print("")
for i in range(1,6):
    for j in range(1,6):
        if i == j or i+j == 6:
            print(j,end='  ')
        else:
            print(" ",end='  ')
    print(" ")


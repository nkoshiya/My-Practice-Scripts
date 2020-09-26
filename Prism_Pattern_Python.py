rows = int(input("enter a number: "))
for i in range(0,rows+1):
    print(" " * (rows - i), end='')
    for j in range(i):
        print(str(i), end='')
    print(str(i)*(i-1), end='')
    print()
for i in range(rows-1,0,-1):
    print(" " *(rows - i), end='')
    for j in range(i):
        print(str(i), end='')
    print(str(i) * (i - 1), end='')
    print()


rows = 15
for x in range(rows, 0, -1):
    num = x
    for y in range(0, x):
        print(num, end=' ')
    print("\r")
print()

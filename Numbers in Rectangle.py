m = int(input())
n = int(input())

for i in range(m):
    count = 0
    for j in range(n):
        number = 7
        row = number + count
        count = count + 1
        print(row, end=" ")
    print()
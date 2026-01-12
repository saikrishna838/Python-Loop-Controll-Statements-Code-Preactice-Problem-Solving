n = int(input())
m = int(input())

num = m * n


for i in range(n):
    for j in range(m):
        print(num, end = " ")
        num = num -1
    print()
        
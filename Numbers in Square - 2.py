n = int(input())



for i in range(n, 0, -1):
    count = 0
    for j in range(n):
        num = n - count
        count = count + 1
        print(num, end=" ")
    print()
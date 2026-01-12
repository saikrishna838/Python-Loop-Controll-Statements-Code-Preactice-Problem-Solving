n = int(input())

k = sum(range(1, n + 1))

for i in range(n):
    for space in range(i):
        print(" ", end = " ")
        
    for j in range(n - i):
        print(k, end = " ")
        k = k - 1
    print()

s = int(input())
n = int(input())

for i in range(1, n + 1):
    space1 = " " * (n - i)
    print(space1, end = "")
    for j in range(s, s + i):
        print(j, end = " ")
    print()
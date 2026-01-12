n = int(input())
count = 0
for a in range(1, n):
    for b in range(a + 1, n):
        for c in range(b + 1, n):
            if a + b + c == n:
                count = count + 1
print(count)
        
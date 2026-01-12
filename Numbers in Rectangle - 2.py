m = int(input())
n = int(input())
k = 1
for i in range(1, m + 1):
    pattern = ""
    for j in range(1, n + 1):
        pattern = pattern + str(k) + " "
        k = k + 1
    print(pattern)
    
    
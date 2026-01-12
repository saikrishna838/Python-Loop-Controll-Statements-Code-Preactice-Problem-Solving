s = int(input())
n = int(input())

k = sum(range(1, n + 1))
start_number = k + s - 1

for row in range(1, n + 1):
    for column in range(row):
        print(start_number, end = " ")
        start_number = start_number - 1
        
    print()
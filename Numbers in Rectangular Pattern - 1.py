m = int(input())
n = int(input())

numbers = ""

for i in range(1, n + 1):
    numbers = numbers + (str(i) + " ")

print(numbers)

for i in range(1, m):
    print(numbers)
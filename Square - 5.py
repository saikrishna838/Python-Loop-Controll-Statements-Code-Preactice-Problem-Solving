s = int(input())
n = int(input())

row = ""
for i in range(n ):
    numbers = s + i
    row = row + (str(numbers) + " ")

for i in range(n):
    print(row)
    
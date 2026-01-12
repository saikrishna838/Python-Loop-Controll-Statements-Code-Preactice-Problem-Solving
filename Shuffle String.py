n = input()


length = len(n)
shuffled = ""
for i in range(length):
    index = int(input())
    shuffled = shuffled + n[index]
print(shuffled)
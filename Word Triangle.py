n = input()
length = len(n)
name = ""

for i in range(1, length + 1):
    name = n[:i]
    print(name)
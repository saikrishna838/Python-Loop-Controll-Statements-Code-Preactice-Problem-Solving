n = int(input())

for i in range(1, n + 3):
    if i == 1 or i == (n + 2):
        hyphens = ("- ") * n
        row = "+ " + hyphens + "+"
    else:
        spaces = ("  ") * n
        row = "| " + spaces + "|"
    
    print(row)
        
        
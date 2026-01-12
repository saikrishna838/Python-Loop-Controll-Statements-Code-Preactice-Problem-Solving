n = int(input())
string = str(n)
length = len(string)
factor = 0

for char in string:
    if int(char) % 2 == 0:
        factor = factor + 1
        
if factor > 2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")
    
    
n = int(input())
stars = 1
for i in range(1, n + 1):
    each_row = "* " * stars
    stars = stars + 2
    
    print(each_row)
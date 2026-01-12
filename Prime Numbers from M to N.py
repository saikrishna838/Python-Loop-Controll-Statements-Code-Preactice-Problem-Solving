m = int(input())
n = int(input())

if not (m > 1):
    m = 2

for number in range(m, n + 1):
    no_of_factors = 0
    for i in range(2, number):
        if (number % i) == 0:
            no_of_factors = no_of_factors + 1
    
    if no_of_factors ==0:
        print(number)
    
    
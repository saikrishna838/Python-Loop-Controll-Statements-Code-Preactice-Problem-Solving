n = int(input())

for number in range(2, n + 1):
    no_of_factors = 0
    for i in range(2, number):
        if(number % i) == 0:
            no_of_factors = no_of_factors + 1
        
    if no_of_factors == 0:
        print(number)
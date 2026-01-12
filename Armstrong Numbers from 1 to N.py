n = int(input())

for number in range(1, n + 1):
    sum_of_power_of_digits = 0
    number = str(number)
    power = len(number)
    
    
    for each_digit in number:
        each_digit = int(each_digit)
        sum_of_power_of_digits = sum_of_power_of_digits + (each_digit ** power)
        
    number = int(number)
    is_armstrong = sum_of_power_of_digits == number
    
    if is_armstrong:
        print(number)
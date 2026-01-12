string = input()

length = len(string)
first_char_lowercase = string[0].lower()
result_string = first_char_lowercase

for index in range(1, length):
    uppercase_char = string[index].upper()
    if string[index] == uppercase_char:
        lowercase_char = string[index].lower()
        result_string = result_string + ("-") + lowercase_char
    else:
        result_string = result_string + string[index]
    
print(result_string)
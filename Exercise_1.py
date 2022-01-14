l_1 = [1,11,14,5,8,9]

def ten_or_less(integer_list):
    values = [num for num in integer_list if num < 10]
    print(values)

ten_or_less(l_1)

# using the 'return' command

def ten_or_less(integer_list):
    return [num for num in integer_list if num < 10]
    
ten_or_less(l_1)

# for some reason in VSCode the output when using 'return' doesn't pop up in the terminal.
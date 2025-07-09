# Using the code below, classify the identifiers as global, local, or built-in.
# For our purposes, you may assume this code is the entire program.

def multiply(left, right): # multiply is global, left & right are local
    return left * right

def get_num(prompt): # get_num is global
    return float(input(prompt)) # float and input are built in, prompt is local

first_number = get_num('Enter the first number: ') # first_number is global
second_number = get_num('Enter the second number: ') # second_number is global
product = multiply(first_number, second_number) # product is global
print(f'{first_number} * {second_number} = {product}') # print is built-in
# In the code shown below, identify all of the function names and parameters 
# present in the code. Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply, left, right on line 4
# get_num, prompt on line 7
# float and input on line 8
# get_num on lines 10, 11
# multiply on line 12
# print on line 13
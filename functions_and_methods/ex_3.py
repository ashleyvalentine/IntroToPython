# Write a program that uses a multiply function to multiply two numbers and 
# returns the result. Ask the user to enter the two numbers, then output the 
# numbers and result as a simple equation.

first_number = input('Enter the first number: ')
second_number = input('Enter the second number: ')

def multiply (first_number, second_number) :
    result = float(first_number) * float(second_number)
    return result

total = multiply(first_number, second_number)

print(f'{first_number} * {second_number} = {total}')
# Write a program named age.py that asks the user to enter their age, then 
# calculates and reports the future age 10, 20, 30, and 40 years from now. 

age = input("What's your age? ")
age = int(age)

def add_age(age, increment):
    future_age = age + increment
    return f'''You are {age} years old. In {increment} years, you will be 
    {future_age}.'''

print(add_age(age, 10))
print(add_age(age, 20))
print(add_age(age, 30))
print(add_age(age, 40))
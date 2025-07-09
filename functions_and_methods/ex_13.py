# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# It will throw an error. The function definition is incorrect. Any parameter
# following a parameter given a default value must also have a default value.
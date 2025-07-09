

# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# It will print 42, 3.141592, and 2.718. The second and third parameters have 
# default values but these are only used if there are no arguments given in
# those positions.
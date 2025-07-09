# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# This will also raise an error because foo is defined with two parameters, and 
# it is fed three on line 7.
# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# an error will be thrown because the variable foo is only available within the
# scope of the function set_foo
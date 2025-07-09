# Take a look at this code snippet:

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# What does this program print? Why?
# It will print 'bar' because line six creates a new variable foo that is only
# scoped to the function set_foo. 
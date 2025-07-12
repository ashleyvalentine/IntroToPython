# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# This code will print 'Empty' because when the function is_list_empty is
# invoked on line 9, it is passed the argument of an empty list. The 
# conditional starting on line 4 will evaluate to the else block because an 
# empty list is a falsy value.


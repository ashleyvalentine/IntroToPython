# What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# The constant variable NAME is assigned the value 'Victor'. The print method 
# is called three times, concatenating the constant variable NAME with a 
# string. The variable NAME is then reassigned to the value 'Nina'. This is 
# bad practice, as the value of a constant variable should not be changed. 
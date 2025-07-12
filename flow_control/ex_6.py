# Write a function that takes a string as an argument and returns an all-caps 
# version of the string when the string is longer than 10 characters. 
# Otherwise, it should return the original string. Example: change 'hello 
# world' to 'HELLO WORLD', but don't change 'goodbye'.

def capitalize_long_string(string):
    if len(string) > 10:
        capitalized_string = string.upper()
        return capitalized_string
    else:
        return string
# When you pass a list to a function,
# the function gets a reference to the list.

# delete_head removes the first element from a list:
print('function: DELETE HEAD')
# first, create the function

# this function recives an argument


def delete_head(t):
    del t[0]


letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)


# tail returns all but the first element of a list:
print('Function:TAIL')


def tail(t):
    return t[1:]


letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)

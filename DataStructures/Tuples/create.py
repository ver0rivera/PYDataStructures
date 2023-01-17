
print('TUPLES ARE IMMUTABLE')
# To create a tuple with a single element, you have to include the final comma:
t1 = ('a',)
print(type(t1))

# Another way to construct a tuple is the built-in function tuple.
# With no argument, it creates an empty tuple:
t = tuple()
print(t)

# If the argument is a sequence (string, list, or tuple),
# the result of the call to tuple is a tuple with the elements of the sequence:
t = tuple('lupins')
print(t)

# Most list operators also work on tuples. The bracket operator indexes an element:
t = ('a', 'b', 'c', 'd', 'e')
print(t[0])

# And the slice operator selects a range of elements.
print(t[1:3])

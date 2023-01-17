# A dictionary is like a list, but more general.
# in a dictionary, the indices can be (almost) any type.

# You can think of a dictionary as a mapping between
#  a set of indices (which are called keys) and a set of values.
# Each key maps to a value

print('DICT')

# The function dict creates a new dictionary with no items.
# Because dict is the name of a built-in function,
# you should avoid using it as a variable name.
eng2sp = dict()
print(eng2sp)
# The curly brackets, {}, represent an empty dictionary.
#  To add items to the dictio- nary, you can use square brackets:
eng2sp['one'] = 'uno'
print(eng2sp)

# the elements of a dictionary are never indexed with integer indices.
#  Instead, you use the keys to look up the corresponding values:
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp['two'])

# The len function works on dictionaries; it returns the number of key-value pairs:
print('LEN FUNCTION')
print(len(eng2sp))

# The in operator works on dictionaries;
# it tells you whether something appears as a key in the dictionary
print('IN OPERATOR')
print('one' in eng2sp)
print('uno' in eng2sp)

# To see whether something appears as a value in a dictionary,
# you can use the method values, which returns the values as a list,
#  and then use the in operator:
print('VALUES OPERATOR')
vals = list(eng2sp.values())
print('uno' in vals)

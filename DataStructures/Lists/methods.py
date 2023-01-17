
# For example, append adds a new element to the end of a list:
print('APPEND')
t = ['a', 'b', 'c']
t.append('d')
print(t)

# extend takes a list as an argument and appends all of the elements
print('EXTEND')

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

# sort arranges the elements of the list from low to high:
print('SORT')
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)

print('----------DELETING ELEMENTS----------')

# If you know the index of the element you want, you can use pop:
# If you don’t provide an index, it deletes and returns the last element.
print('POP')
t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print('element deleted:')
print(x)

# If you don’t need the removed value, you can use the del operator:
print('DEL')
t = ['a', 'b', 'c']
del t[1]
print(t)

# To remove more than one element, you can use del with a slice index
print('DEL WITH SLICE')
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)

# If you know the element you want to remove
# (but not the index), you can use remove:
# The return value from remove is None
print('REMOVE')
t = ['a', 'b', 'c']
t.remove('b')
print(t)

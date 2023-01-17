# The association of a variable with an object is called a reference.
# An object with more than one reference has more than one name,
# so we say that the object is ALIASED.
print('OBJECT ALIASED')
a = [1, 2, 3]
b = a
b[0] = 17
print(a)

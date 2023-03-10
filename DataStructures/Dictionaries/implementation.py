word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
else:
    d[c] = d[c] + 1
print(d)

# Because the get method automatically handles
# the case where a key is not in a dictionary,
# we can reduce four lines down to one and eliminate the if statement.
print('get method')
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)

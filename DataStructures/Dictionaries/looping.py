# FOR statement with keys
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

# For example if we wanted to find all the entries
# in a dictionary with a value above ten,
# we could write the following code:
print('select special keys')
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])

# If you want to print the keys in alphabetical order,
#  you first make a list of the keys in the dictionary using
#  the keys method available in dictionary objects,
# and then sort that list and loop through the sorted list
print('print keys in alphabetical order')
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])

# The comparison operators work with tuples and other sequences.
# Python starts by comparing the first element from each sequence.
# If they are equal, it goes on to the next element, and so on,
# until it finds elements that differ.

print((0, 1, 2) < (0, 3, 4))

print((0, 1, 2000000) < (0, 3, 4))

print('The sort function works the same way. It sorts primarily by first element, but in the case of a tie, it sorts by second element, and so on')

print('DSU')

# Decorate a sequence by building a list of tuples with one or more sort keys preceding the elements from the sequence,
# Sort the list of tuples using the Python built-in sort,
# Undecorate by extracting the sorted elements of the sequence.

# For example, suppose you have a list of words and
# you want to sort them from longest to shortest

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
# tells sort to go in decreasing order.
t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)

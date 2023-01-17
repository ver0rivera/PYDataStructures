# To convert from a string to a list of characters, you can use list:
# The list function breaks a string into individual letters.
print('Convert using LIST')
s = 'spam'
t = list(s)
print(t)

# If you want to break a string into words, you can use the split method:
print('Convert using SPLIT')
s = 'pining for the fjords'
t = s.split()
print(t)
# you can use the index operator (square bracket)
# to look at a particular word in the list.
print(t[2])


# You can call split with an optional argument called
#  a delimiter that specifies which characters to use as word boundaries.
print('SPLIT WITH DELIMITER')
s = 'spam-spam-spam'
delimiter = '-'
print(s.split(delimiter))

# join is the inverse of split.
# It takes a list of strings and concatenates the elements.
print('JOIN')
t = ['pining', 'for', 'the', 'fjords']
# To concatenate strings without spaces, you can use the empty string, “”, as a delimiter.
delimiter = ' '
print(delimiter.join(t))

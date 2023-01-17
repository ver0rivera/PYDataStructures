# Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for
# each of the messages. You can pull the hour out from the 'From '
#  line by finding the time and then splitting the string a second
#  time using a colon. From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dictionary = dict()
for line in handle:
    if "From:" in line:
        continue
    if "From" in line:
        word = line.split()
        item = word[5]
        itemSplit = item.split(":")[0]
        dictionary[itemSplit] = dictionary.get(itemSplit, 0)+1

datos = sorted([(d, f) for f, d in dictionary.items()], reverse=True)
lst = list()
for f, k in datos:
    lst.append([k, f])
for f, k in sorted(lst):
    print(f, k)

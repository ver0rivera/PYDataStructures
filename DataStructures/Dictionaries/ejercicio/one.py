# Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number
# of mail messages. The program looks for 'From '
# lines and takes the second word of those lines as
# the person who sent the mail. The program creates
# a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
#  After the dictionary is produced, the program reads through
# the dictionary using a maximum loop to find the most prolific committer.

name = "mbox-short.txt"
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lst = list()
emails = list()
dictionary = dict()
space = ""

for line in handle:
    lst = line.rstrip()
    newlst = lst.split()
    if 'From' in newlst:
        emails.append(newlst[1])
for name in emails:
    dictionary[name] = dictionary.get(name, 0) + 1

nameListMAX = [key
               for key, value in dictionary.items()
               if value == max(dictionary.values())]
nameM = space.join(nameListMAX)

print(nameM, max(dictionary.values()))

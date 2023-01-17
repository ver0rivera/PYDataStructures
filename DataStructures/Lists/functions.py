
# There are a number of built-in functions that can
#  be used on lists that allow you to quickly look
# through a list without writing your own loops:
nums = [3, 41, 12, 9, 74, 15]
print('LEN')
print(len(nums))
print('MAX')
print(max(nums))
print('MIN')
print(min(nums))
print('SUM')
# The sum() function only works when the list elements are numbers.
print(sum(nums))
print('SUM/LEN')
print(sum(nums)/len(nums))


# FIRST MINI PROGRAM WITH LOOPS
print('MINI PROGRAM')
numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)


# The + operator concatenates lists:
print('CONCATENACION +')
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# Similarly, the operator repeats a list a given number of times:
print('REPETICION *')
operation1 = [0] * 4
print(operation1)

operation2 = [1, 2, 3] * 3
print(operation2)

# The slice operator also works on lists:

print('SLICE OPERATOR :')
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

# A slice operator on the left side of an assignment can update multiple elements:
print('slice-UPDATE elements')
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)

numbers = [1, 2, 3, 4, 5, [12, 13, 23, 34, 54]]
letters = ['a', 'b', 'c', 'd', 'e', 'f']

mix = letters + numbers
print(mix)

# adding lists
letters += numbers
print(letters)

# print index of letters
print(letters[2])

# accessing nested list
print(letters[11][2])

"""
variableName=[ operation  for loop if statement (optinal)]
"""
squares = [num ** 2 for num in range(1, 11)]
oddSquares = [num ** 2 for num in range(1, 11) if num ** 2 % 2 != 0]
evenSquares = [num ** 2 for num in range(1, 11) if num ** 2 % 2 == 0]

print(squares)
print(evenSquares)
print(oddSquares)

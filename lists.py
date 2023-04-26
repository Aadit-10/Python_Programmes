letter=['a','b','c']
num=[1,2,3]
print(num+letter)
letter.append('hello')
print(letter)
print(letter[0:2])

# List functions
rainfall=[2,4,56,78,234,90,54,34,21]

print(min(rainfall))
print(max(rainfall))
print((sum(rainfall)))
print(len(rainfall))
print(sorted(rainfall,reverse=True))
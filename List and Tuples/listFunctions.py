things = ["first"]

# APPEND
things.append("another thing")
print(things)
# EXTEND
things.extend("another thing")
print(things)

# INSERT
things.insert(0, 'zero')  # index and value
print(things)

# REMOVE removing if u give the correct name of the variable stored
things.remove('a')
print(things)

# POP simply using pop will remove last element else it will remove specified index
things.pop(1)
print(things)

# INDEX
print(things.index("o"))
print(things.index("n", 1, 4))  # this will search for n in between 1 and 4

""" other methods 
list.clear() clears elements in list also del a[:3] delete from 3rd index
list.count(item)
list.sort(KEY=none,reverse=false)
list.reverse()
list.copy()
"""

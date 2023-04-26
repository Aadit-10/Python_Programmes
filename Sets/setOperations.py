a={1,2,3}
b={4,5,6}

# UNION
print(a.union(b))# a|b another way to find union

# intersection
print(a.intersection(b))#a&b

#difference
print(a.difference(b))#a-b

# EQUALS
print(a==b)

# SUBSET
print(b.issubset(a))

# SUPERSET
print(b.issuperset(a))


c=frozenset([1,2,4])
# frozensets are immutable 
a = {1, 2, 3}
b = {3, 4, 5}

print(a)
# print(a[0]) no indexing possible as it is unordered
for item in a:
    print(item)

a.add(4)
print(a)
a.update(b)  # only unique elemnts will be updated ||||set is unique
print(a)

a.remove(5)
a.discard(8)
print(a.pop())
print(a)

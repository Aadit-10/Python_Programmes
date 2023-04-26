numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8)
m = ('a', 23, 'were')
letters = ('a', 'b', 'c', 'd')

two_dim = ((2, 3), (4, 5), (5, 7))
print(m[2])
print(two_dim[2][0])

packing_tuples = 2, 5, "space"
print(packing_tuples)
a, b, c = packing_tuples
print(a)
print(b)
print(c)
print(packing_tuples)

print(numbers[:3])
print("Even numbers :", numbers[0::2])
print("Odd Numbers :", numbers[1::2])

for item in letters + numbers:
    print(item)


def area_and_circumference_of_circle(r):
    import math
    return (math.pi * r ** 2, 2 * math.pi * r)


print(area_and_circumference_of_circle(7))

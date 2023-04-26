class car():
    pass

honda=car()
mazda=car()

honda.weight=260
honda.model="NRZ"

mazda.weight=260
mazda.model="NRZ"

# print in 2 diff ways
print(honda.weight)
print(honda.model)
print(mazda.__dict__)
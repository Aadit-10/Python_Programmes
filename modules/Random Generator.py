import random


def petrol_values():
    possible_prices = []
    price = 1.10
    output = []
    while price <= 1.45:
        price += .01
        possible_prices.append(round(price, 2))
    for i in range(0, 30):
        output.append(random.choice(possible_prices))
    # return random.sample(possible_prices, 30)
    return output


def petrol_values2():
    output = []
    for i in range(0, 30):
        output.append(random.randint(140, 145) / 100)
    return output

print(petrol_values2())
# print(petrol_values())

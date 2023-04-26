rainfall=[23,45,56,76,87,32,65]
location= "amsterdam"

def print_rainfall(values):
    day=1
    for value in values:
        print("Day ",day,":",value)
        day+=1

def avg_rainfall(values):
    import math
    return math.fsum(values)/len(values)

def change_location(new_location):
    global location
    location=new_location
    print("the new location is ",location)


print_rainfall(rainfall)
print(avg_rainfall(rainfall))
print(location)
change_location("new york")
print(location)

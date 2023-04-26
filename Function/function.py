def pyramid(layer):
    star="*"      #this function used to make a triangle
    for i in range(0,layer):
        print(star.center(20," "))
        star+='**'

def circle_area(radius):
    import math
    return math.pi*radius**2
def surface_cuboid(l,w,h):
    """ this function takes lw h as inp and print sa"""
    return 2*(l*w+w*h+h*l)

print(circle_area(5))

print(surface_cuboid.__doc__)
pyramid(5)
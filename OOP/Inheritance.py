class Cat:
    def __init__(self, mass, lifespan, behaviour):
        self.mass = mass
        self.lifespan = lifespan
        self.behaviour = behaviour

    def vocalise(self):
        print("meowww")


class Leopard(Cat):
    def vocalise(self):
        print("errrrrr")

tommy = Cat(990, 25, 47)
print(tommy.vocalise())

leo = Leopard(90, 40, 14)
print(leo.vocalise())
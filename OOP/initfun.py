class Car:
    def __init__(self, make, model, year,max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed=max_speed
        self.speed = 0

    def accelarate(self,add_speed=5):
        self.speed+=add_speed

myCar = Car('suzuki', 'wagonR', 2022,123)
dreamCar = Car('Nissan', 'GTR', 2011,345)
dreamCar.accelarate(20)

print(myCar.__dict__)
print(dreamCar.__dict__)
# print('dream car is {}{}'.format(dreamCar.make, dreamCar.model) )

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self._model = model
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self._model

    def get_year(self):
        return self.__year

    def get_model(self,new_model):
         self._model=new_model

nisaan=Car("niss","hai",2013)
# print(nisaan.__make) this is not possible as make is private
print(nisaan.get_make())
print(nisaan.get_year())


"""
_ protected attributes
__ private attributes
"""
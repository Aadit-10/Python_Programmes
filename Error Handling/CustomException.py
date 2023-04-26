class RecipeNotFoundException(Exception):
    def __init__(self):
        self.message = 'RecipeNotFoundException'


try:
    recipe = '2 eggs'
    if recipe != str:
        raise RecipeNotFoundException
    
except RecipeNotFoundException as e:
    print(e.message)

print("i am here")

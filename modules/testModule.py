import myModule
"""if u use from myModule import * then when just use area(r) no need myModule.area(r)"""

r = float(input("Enter radius: "))
print("The circumference is ", myModule.circumference(r))
print("The area is ", myModule.area(r))

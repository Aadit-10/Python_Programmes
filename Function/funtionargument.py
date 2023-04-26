def fancy_name_plate(*names):
    for name in names :
        print("#######################")
        print("#---------------------#")
        print("##"+name.center(28 , "-")+"##")
        print("#---------------------#")
        print("#######################")

def fancy_name_plate_defargs(name,lenght=26,symbol='&'):
    print(symbol * lenght)
    print(symbol * 2 + (lenght-4) * '-' + symbol*2)
    print(symbol * 2 + name.center(lenght - 4,'-')  + symbol * 2)
    print(symbol * 2 + (lenght - 4) * '-' + symbol * 2)
    print(symbol*lenght)

fancy_name_plate('sanjin','you are iren men')
fancy_name_plate_defargs('bob',18,'%')
fancy_name_plate_defargs('Anna',12,'#')
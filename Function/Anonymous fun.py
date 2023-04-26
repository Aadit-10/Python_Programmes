
months=['January','February','March','april','may','june','july','august','september','october','november','december']
kinetic_energy=lambda m,v : (m*v**2)/2
print('Kinetic Energy : ',kinetic_energy(80,30))

mass_energy= lambda m,c=299792458 : m*c**2
print('Mass Energy : ',mass_energy(.00000034))

grav_force= lambda m1 , m2 =5.972 *10**24,r=6371000:6.6 * 10 ** -11 * m1 * m2 /r**2
print("my grav force ",grav_force(84))

# print abbrevations of the month
abv_month=list(map(lambda month :month[:3].upper(),months))

print(abv_month)
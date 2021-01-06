#works out the altitude of a satellite given its time period

#constants
G = float(6.67e-11);
M = float(5.97e24);
R = float(6371e3);
pi = 3.14;

time = float(input("Enter the time interval of the satellite: "));

T = time**2;
GMT = G*M*T;
print("GMT:", GMT);

temp = GMT/(4*(pi**2));
print (temp);

temp = temp**(1/3);
print(temp);

h = temp - R;

print("The altitude in meters would be", h);

#c)
#24 hours = 35,000km
#90 mins = 4,200km
#45 mins = -2,200km

#d)
#differenc is 71km
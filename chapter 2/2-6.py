#planetary orbits
from math import sqrt, pi

#constants
G = 6.6738e-11;
M = 1.9891e30;

#input
perR = float(input("Enter distance from the Sun at perihelion: "));
perV = float(input("Enter velocity at perihelion: "));

#calculate velocity at aphelion
a = 1.0;
b = -((2*G*M) / (perR*perV));
c = -((perV**2) - ((2*G*M)/perR));

d = (b**2) - (4*a*c);

root1 = (-b + sqrt(d)) / (2*a);
root2 = (-b - sqrt(d)) / (2*a);

#take the lowest root
if(root1 < root2 or root2 < 0):
    apV = root1;
else:
    apV = root2;

apR = (perR*perV) / apV;

#calculate other properties
major = 0.5*(perR + apR);
minor = sqrt(perR * apR);

period = (2*pi*major*minor) / (perR * perV);
periodY = period / 31536000;

eccentricity = (apR - perR) / (apR + perR);

print("Distance at aphelion:", apR);
print("Velocity at aphelion:", apV);
print("Time period:", period, "seconds or:", periodY, "years");
print("Orbit eccentricity:", eccentricity);
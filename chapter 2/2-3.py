#coverts Cartesian coordinates (x,y) to polar coordinates (r, d)
from math import atan, pi

x = float(input("Enter the x coordinate: "));
y = float(input("Enter the y coordinate: "));

r = (x**2 + y**2)**0.5;
radians = atan(y/x);
d = (radians*180)/pi;

print("r:", r, "degrees:", d);
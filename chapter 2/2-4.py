#calculate the speed in years of travel for a observer at rest and an observer on the rocket

x = float(input("Enter distance to travel, in light years: "));
v = float(input("Enter speed, as fraction of c: "));

restT = x/v;

perceivedT = restT * (1 - ((v**2)/1))**0.5;

print("Time for people on earth:", restT);
print("Time for people on rocket:", perceivedT);
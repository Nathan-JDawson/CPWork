# s = 0.5at^2
# t = sqrt(2s/a)
# s = user input
# a = g = 9.81

g = float(9.81);
s = float(input("Enter height of tower: "));

t = ((2*s)/g)**0.5;

print("It would take",t,"seconds for the ball to hit the ground");
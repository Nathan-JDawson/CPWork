#madelung constant
from math import sqrt

#constants
L = 150; #total atoms in each direction

sum = 0.0;
for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            if(i != 0 and j != 0 and k != 0):
                magnitude = sqrt((i**2) + (j**2) + (k**2));
                if((i + j + k) % 2 == 0):
                    sum += 1/magnitude;
                else:
                    sum -= 1/magnitude;
                #endif
            #endif
        #endfor
    #endfor
#endfor
m = sum;
print("The Madelung constant is:", m);
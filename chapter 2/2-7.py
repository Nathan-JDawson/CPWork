#catalan numbers
c0, c1 = 1, 1;
n = 1;

while(c0 < 1e9):
    print(int(c0));
    c0, c1 = c1, (((4*n) + 2) / (n + 2)) * c1;
    n+=1;
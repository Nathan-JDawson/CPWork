#semi-empirical mass

#constants
a1 = 15.8;
a2 = 18.3;
a3 = 0.714;
a4 = 23.2;

#calculations


for atomicNum in range(1, 101):
    max = [0,0]; # max0 = mass number, max1 = energy per nucleon
    for massNum in range(atomicNum, (atomicNum * 3) + 1):
        if(massNum % 2 != 0):
            a5 = 0;
        elif(atomicNum % 2 == 0):
            a5 = 12.0;
        else:
            a5 = -12.0;

        bindingEnergy = (a1*massNum) - (a2 * (massNum**(2/3))) - (a3 * ((atomicNum**2)/(massNum**(1/3)))) - (a4 * ((massNum - (2 * atomicNum))**2 / massNum)) + (a5/(massNum**0.5));
        perNucleon = bindingEnergy/massNum;

        if(perNucleon > max[1]):
            max[0] = massNum;
            max[1] = perNucleon;

    print("Most stable nucleus for atomic number", atomicNum, "has mass number:", max[0], "with binding energy per nucleon:", max[1]);
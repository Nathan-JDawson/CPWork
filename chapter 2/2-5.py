#quantum step calculation - probability of transmission and reflection
from scipy.constants import h, pi

mass = 9.11e-31;
e = 10;
v = 9;

hcross = h / (2*pi);
wave1 = ((2*mass*e)**0.5) / hcross;
wave2 = ((2*mass*(e-v))**0.5) / hcross;

tProb = (4 * wave1 * wave2) / (wave1 + wave2)**2;
rProb = ((wave1 - wave2) / (wave1 + wave2))**2;

print("Probability of transmission is", tProb, "and probability of reflection is", rProb);
# This code calculates the Magnetic Field, B [T], using current, Ienc [A], and distance,
# rad [m]. We define pi [dimensionless], and permeability of free space, mu0 [T m A^-1]

# Constants
pi = 3.14
mu0 = 12.0E-07

# input
Ienc = 25 
rad = 0.1

# Magnetic field 
B = (mu0/(2*pi))*(Ienc/rad)

# output
print(B)

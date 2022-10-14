# The Habitable Zone (HZ) of a star is the region where
# liquid water, and therefore, life, could potentially exist.
# For example, Earth lies in the Sun's HZ.

# imports statements (math for calculations)
import math

# opens input file and output file
input_file = open("hz.in")
output_file = open("hz.out", "w")

# accepts and type-casts inputs
# m_v is apparent magnitude of star
# d is distance from Earth in parsecs
# bc is bolometric correction constant of star
m_v, d, bc = [float(i) for i in input_file.readline().split()]

# calculates absolute magnitude
M_v = m_v - 5*(math.log((0.1 * d), 10))

# calculates bolometric magnitude
M_bol = M_v + bc

# calculates absolute luminosity
L_star = (0.1)**((M_bol - 4.72)/2.5)

# calculates inner and outer radii of HZ
r_i = math.sqrt(L_star/1.1)
r_o = math.sqrt(L_star/0.53)

# writes inner and outer radii in output file
output_file.write(str(r_i) + " " + str(r_o))


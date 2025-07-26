# Given a complex number, convert it to polar coordinates (modulus and phase angle)

import cmath

# Input complex number (e.g. 1+2j)
z = complex(input("Enter a complex number (e.g., 1+2j): "))

# Calculate modulus and phase
modulus = abs(z)
phase = cmath.phase(z)

# Output
print("Modulus:", modulus)
print("Phase angle (in radians):", phase)

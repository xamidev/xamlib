# Returns the orbital radius (for e=0 orbits only)

from math import pi

def roundOrbitRadius(circumference):
    return circumference/(2*pi)
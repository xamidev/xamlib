# Returns the orbital speed of a spaceship

from math import pi
from roundOrbitCircumference import roundOrbitCircumference

def orbitalSpeed(orbitRadius, orbitalPeriod):
    return roundOrbitCircumference(orbitRadius)/orbitalPeriod
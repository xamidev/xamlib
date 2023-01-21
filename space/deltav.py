# Calculating the DeltaV of a spacecraft

from math import log, e

def deltav(startingMass, endMass, gasEjectionSpeed):
    return gasEjectionSpeed*log(startingMass/endMass, e)
# Returns a planet's liberation speed (speed needed to escape influence sphere)

import algebra

gravitationalConstant =6.67430E-11

def planetLiberationSpeed(planetMass, planetRadius):
    return algebra.sqroot.sqroot((2*gravitationalConstant*planetMass)/planetRadius)
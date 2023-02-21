# Calculating the excentricity of an orbit

def excent(apoapsisRadius, periapsisRadius):
    return 1-(2/(apoapsisRadius/periapsisRadius+1))
from algebra import sqroot

def quadratic(a,b,c): # Resolves a quadratic equation. Returns a list
    delta=b**2+4*a*c
    solutions=[]
    if delta>0:
        solutions.append((-b-sqroot(delta))/2*a)
        solutions.append((-b+sqroot(delta))/2*a)
    elif delta==0:
        solutions.append(-b/2*a)
    return solutions
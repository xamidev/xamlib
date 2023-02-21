import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)
  
from algebra.sqroot import sqroot  

def length2d(x, y):
    return sqroot(x**2+y**2)
def length3d(x, y, z):
    return sqroot(x**2+y**2+z**2)
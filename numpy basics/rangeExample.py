import numpy as np 
from cgitb import small

# Range of numbers with a adder
even=np.arange(0,100,2)
print(even)

# Linespace Example Range of numbers along with how many numbers you want in between that.

sample=np.linspace(2, 10, 25)
print(sample)

# useful to evaluate function at lots of points
x=np.linspace(0,2*np.pi,100) 
print(np.sin(x))


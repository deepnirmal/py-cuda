

import numpy as np

# Rank = dimensions

from numpy.core.multiarray import dtype
#int 1-D Array example - Rank 1
a=np.array([1,2,4,5,6])
print(a.dtype)

#Float 1-D Array example - Rank 1
b=np.array([1.1,2.2,3.3])
print(b.dtype)

#Int 2-D Array
check=np.array([[1,2,3],[2,3,4],[3,4,5]])

print(check)

#2-D complex num array - Rank 2
c=np.array([ [1,2],[3,4] ],dtype=complex)

print(*c)

zeros=np.zeros((3,4))
print(zeros)

ones2D=np.ones((3,4), dtype=np.int32)
print(ones2D)
print("\n3D array")
#3-D array Rank-3
ones3D=np.ones((2,3,4), dtype=np.int32)
print(ones3D)




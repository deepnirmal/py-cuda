'''
Created on 06-Aug-2016
@author: DEEP
'''
import numpy as np
#1-D array
a=np.arange(6) 
print(a)

# 2-D array
b=np.arange(12).reshape(4,3)
print(b)

# 3-D array
c=np.arange(24).reshape(2,3,4)
print(c)

aa=np.arange(10000)
print(aa)

bb=np.arange(10000).reshape(100,100)
print(bb)
#To disable this behaviour and force NumPy to print the entire array, you can change the printing options using set_printoptions.
np.set_printoptions(threshold='nan')
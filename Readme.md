# py-cuda
### This repo consist of basics of Numpy programming and Py-cuda sample programs that uses Nvidia GPU for parallel computation

###Local setup [Windows] : 
####The following software was used here:
* Python 2.7 or 3.3 
* NumPy 1.3.0 
* Scipy 0.7.1 
* Pycuda version 1.2 or get the latest version from here : [Pycuda install](http://git.tiker.net/trees/pycuda.git/)
* Nvidia nsight GPU software

####Install first pycuda python package
``` 
python setup.py install 
``` 
####Chose any IDE like Eclipse PyDev or Sublime Text or Visual Studio ( anything works fine ) <br/>
####Import two modules from package pycuda along with Numpy :
```
import pycuda.driver as drv
import pycuda.autoinit
import numpy
```


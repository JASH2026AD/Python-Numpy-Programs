import numpy as np
#1D Array
a=np.array([19,7,18,3,5])
b=a.view()
b[0]=7
print(a)
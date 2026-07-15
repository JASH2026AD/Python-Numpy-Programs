import numpy as np
#1D Array
a=np.array([[19,7,18,3,5],[6,3,6,9,21]])
print(np.median(a)) #→ Finds the median of all elements.
print(np.median(a, axis=0)) #→ Finds the median of each column.
print(np.median(a, axis=1))# → Finds the median of each row.

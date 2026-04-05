"""#Day 9

##Numpy
"""

!pip install streamlit

import numpy

lst = [1,2,3,4,5]
print((lst))

arr = numpy.array([1,2,3,4,5])
print(arr.mean())

import numpy as np
arr = np.arange(1,10,2)
arr

import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[1,2,3]])

print('Total :', arr.size)
print('Rows  :', np.size(arr,0)) #Rows
print ('col  :', np.size(arr,1)) #Colums
arr

import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[1,2,3]])

print('Total :', arr.size)
print( np.size(arr,0), np.size(arr,1)) #Rows #Colums
print(arr.shape)

import numpy as np
arr1 = np.array([1,2,3,1,2,3])
arr2 = np.array([[1,2,3],[1,2,3]])

print(arr1.ndim)
print(arr2.ndim)

arr3 = np.array(arr1, ndmin = 3)
print(arr3)

arr = np.zeros(shape = (3,5), dtype = int)

print(arr)

arr = np.zeros(shape = (3,5), dtype = bool)

print(arr)

arr = np.zeros(shape = (8,8), dtype = 'int')

print(arr)

"""##Q. Chess matrix"""

(0,0),(0,2),(0,4),(0,6)
(1,1),(1,3),(1,5),(1,7)

import numpy as np
for i in range(len(arr)):
  for j in range (len(arr[i])):
    if (i+j)%2 == 0:
      arr[i][j] = 1
arr

"""##Q. Eye Function ( middle value to 1.)"""

np.eye(4, dtype =int)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt

# %matplotlib inline

plt.hist(np.random.randn(10000000), bins = 1000);

import pandas as pd

lst = [1,2,3,4,5]

pd.Series(lst)

pd.Series(index = ['Eshant', 'Pranjal', 'Jayesh', 'Ashish'], data = [1,2,3,4])

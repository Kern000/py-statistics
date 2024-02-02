import numpy as np;
# use pip3 install numpy

# one-dimension array
arr = [20, 2, 7, 1, 34] 

print("25th percentile: ", np.percentile(arr, 25, method="linear"))
print("50th percentile: ", np.percentile(arr, 50, method="linear"))
print("75th percentile: ", np.percentile(arr, 75, method="linear"))
print("100th percentile: ", np.percentile(arr, 100, method="linear"))

""" percentile expects
// numpy.percentile(  array, 
                        percentileToCompute:float, 
                        axis=None, 
                        method='linear'
                    )
// can apply on unsorted array and it will return the value at percentile
// returns value at percentile
"""

# numpy axis default is 0 column, 1 row, meaning flattened array
# method for estimating percentile
import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    valList = []
    total = 0
    for t in range(len(L)):
        total += np.exp(L[t])
    for i in range(len(L)):
        a = np.exp(L[i]) / total
        valList.append(a)
    
    return valList    

"""
GIVEN SOLUTION

import numpy as np

def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result
    
    # Note: The function np.divide can also be used here, as follows:
    # def softmax(L):
    #     expL(np.exp(L))
    #     return np.divide (expL, expL.sum())

"""
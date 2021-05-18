import numpy as np
k=np.array([[1,2,3],[4,5,6]])
def transpose(k):#returns the transpose of the matrix
    a=k.shape[0]
    b=k.shape[1]
    return k.reshape(b,a)
def stddev(k):#returns the standard deviation of the set
    return np.matmul(np.transpose(k),k)
print(stddev(k))
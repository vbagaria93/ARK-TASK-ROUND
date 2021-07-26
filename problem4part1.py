import pandas as pd
from re import I
import numpy as np
import sys
import matplotlib.pyplot as plt
sys.setrecursionlimit(10**8)
df=pd.read_csv('Data1.csv')
j=df.to_numpy()
stddevp=0.01
p_matrix=np.zeros((6,6))
"""Ive made velocity a measured state cause change in velocity and acceleration would come out to be the same ,
   if it is integrated in the control state matrix"""
for i in range (0,6):
    p_matrix[i][i]=stddevp**2
p_mat=p_matrix
def identity(n):
    a=np.zeros((n,n),dtype=float)
    for i in range (0,n):
         a[i][i]=1
    return(a)
def firstp(k,q):
    """Gives the first predicted values through the velocities in the 6 columns"""
    """k is a 18*10000 matrix"""
    """based on the assumption that the time lag between the readings is a second
    The state control variable is the acceleration and the state is position and velocity in all the three directions"""
    a=np.zeros(3)
    for i in range (0,3):
        s=0.0
        for j in range (i,18,3):
                    s+=k[q+1][j]-k[q][j]
        a[i]=s/6.0
    return a #returns only the velocity in three directions along a row
a_coeff=np.zeros((6,6))
b_coeff=np.zeros((6,3))
for i in range (0,3):
    a_coeff[i][i]=1
    a_coeff[i+3][i+3]=1
    a_coeff[i][i+3]=1 
    b_coeff[i][i]=.5
    b_coeff[i+3][i]=1
""" assuming the time gap/lag to be one second """
def error(matrix):
    """assumes a 6 x 1 matrix and returns the R error matrix(6*6),
    since ive averaged the velocity from all the six stations,
     the error in velocity can be assumed to have 10 percent error just like the position"""
    a=np.zeros((6,6))
    for i in range (0,6):
        a[i][i]=(matrix[i][0]/5)**2
    return a         
def kalman_gain(predicted,error):
    """assumes the predicted matrix and the error and returns the kalman gain matrix
    I have ignored the covariance and only used variance and x y and z motion are independent of each other,
    so naturally H is an identity matrix"""
    q=predicted + error
    a=np.zeros((6,6))
    for i in range (0,6):
        a[i][i]=predicted[i][i]/q[i][i]
    return a
predicted_values=np.zeros((9997,3))
predicted_values[0]=j[0,0:3]
predicted_velocity=np.zeros((9998,3))
predicted_velocity[0]=firstp(j,0)
"""print(j[0,:]) remember where it begins from"""
def format(predicted,index,predicted_velocity):#index begins from 0
    a=np.zeros((6,1))
    for i in range (0,3):
        a[i][0]=predicted[index][i]
        a[i+3][0]=predicted_velocity[index][i]# there might be a logical mistake here, look out for it.
    return a
def acceleration(array,index):#index should begin from 0
    a=np.zeros(3)
    b=np.zeros((3,1))
    a=firstp(array,index)-firstp(array,index-1)
    for i in range(0,3):
        b[i][0]=a[i]
    return b
def latest(a_coeff,b_coeff,array,index,predicted_values,predicted_velocity):#in a lot of places index will be one ahed of track,look out for it
     statec=acceleration(array,index+1)
     """previous velocity is accepted and the latest state is evolved"""
     latest_state=np.matmul(b_coeff,statec)+np.matmul(a_coeff,format(predicted_values,index,predicted_velocity)) 
     return latest_state
def sensor_fusion(array,p_matrix,index,a_coeff,b_coeff,predicted_values,predicted_velocity):
     measurement=np.zeros((6,1))
     if index ==9997:
         return predicted_values
     for i in range (0,3):
         measurement[i][0]=array[index][i]
     measurement[3:6,0]=firstp(array,index)
     errorf=error(measurement)
     kalman_factor=kalman_gain(p_matrix,errorf)
     latest_state=latest(a_coeff,b_coeff,array,index-1,predicted_values,predicted_velocity)
     final=latest_state+np.matmul(kalman_factor,(measurement-latest_state))
     p_matrix=np.matmul((identity(6)-kalman_factor),p_matrix)
     p_matrix=np.matmul(a_coeff,p_matrix)
     p_matrix=np.matmul(p_matrix,np.transpose(a_coeff))
     for i in range (0,3):
         predicted_values[index][i]=final[i]
         predicted_velocity[index][i]=final[i+3]
     return sensor_fusion(array,p_matrix,index+1,a_coeff,b_coeff,predicted_values,predicted_velocity)
ww=sensor_fusion(j,p_matrix,1,a_coeff,b_coeff,predicted_values,predicted_velocity)
y=[]
for i in range (0,9997):
    y.append(i)
plt.plot(y,ww[:,0])
plt.show()
e=pd.DataFrame(ww,columns=['x','y','z'])
e.to_csv('Reducednoise.csv')
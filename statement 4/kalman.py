from re import I
import numpy as np
import pandas as pd#We will calculate trajectories with respect to different ground stations,I have assumed the time gap between readings to be 1 second
def identity(n):#function to return a identity matrix
    a=np.zeros((n,n),dtype=float)
    for i in range (0,n):
         a[i][i]=1
    return(a)
def diagm(k):#returns a diagonal matrix
    for i in range (0,k.shape[0]):
       for j in range (0,k.shape[0]): 
         if(i!=j):
             k[i][j]=0
    return k
def stddev(k):#returns the standard deviation of the set
    return (np.matmul(np.transpose(k),k).astype(np.float))
def sum1(k): #3 calculate the average speed,accepts 1 column of the data frame
        c =0
        for i in range (0,9998):
            if (k[i]*k[i+1])>0 and (k[i+1] >  k[i]):
                    c+=k[i+1]-k[i]
            elif ((k[i]*k[i+1])>0 and k[i]>k[i+1]):
                    c+=k[i]-k[i+1]
            elif (k[i]<0 and k[i+1]>0):
                    c+=k[i+1]-k[i]
            elif (k[i]>0 and k[i+1]<0):
                    c+=k[i]-k[i+1]
        return c/10000.0
def retp(k,y):
         d=sum1(k[:,y])
         if(k[0][y]>k[1][y]):
             return k[0][y]-d
         elif(k[0][y]<k[1][y]):
             return k[0][y]+d
def upd(k,d,i,j):#k is the original matrix,d has the kalman value from previous readings,for ith row and jth column
         u=sum1(k[:,j])
         if(k[i][j]>k[i+1][j]):
             return d[i-1][j]-u
         elif(k[i][j]<k[i+1][j]):
            return d[i-1][j]+u
df=pd.read_csv('Data1.csv')
df.columns=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R']
df.to_csv('ff.csv')
j=df.to_numpy()
c=np.zeros((3,1),dtype=float)
d=np.zeros((3,1),dtype=float)
for i in range(0,3):
     c[i][0]=retp(j,i)
     d[i][0]=j[1][i]#we store the original measurements here
#for the first row(first iteration) we will have to calculate the standard deviation manually, after that we can use Kalman Gain
a1=np.zeros((1,3),dtype=float)
for i in range (0,3):#Matrix to help us calculate the Mean Squared Error
     a1[0][i]=j[1][i]-c[i]
     if (a1[0][i]<0):
         a1[0][i]=-a1[0][i]
a2=stddev(a1)# a2 is the state covariance matrix and I have assumed the error(measurement covariance R) to be 10 percent of the readings,that is not constant,but...
a2=diagm(a2)
Rma= identity(3)
for i in range (0,3):
     Rma[i][i] = (j[1][i]*0.10)**2#assuming the error due to lag be ten percent of the readings
kalman=identity(3)
for i in range (0,3):
     kalman [i][i]=(a2[i][i])/(a2[i][i]+Rma[i][i])
predicted=np.zeros((9999,3))
for i in range (0,3):
     predicted[0][i]=c[i][0]
p = c+np.matmul(kalman,(d-c))
for i in range(0,3):
     predicted[1][i]=p[i]#storing all values as predicted by Kalman Filter
for i in range (2,9999):
     a2=np.matmul((identity(3)-kalman),a2)#process covariance matrix for the next steps
     for i1 in range (0,3):
        Rma[i1][i1]=(j[i][i1]*0.10)**2
     for i1 in range (0,3):
         kalman[i1][i1]=a2[i1][i1]/(a2[i1][i1]+Rma[i1][i1])
     for i1 in range (0,3):
         d[i1][0]=j[i][i1]
         c[i1][0]=upd(j,predicted,i-1,i1)
     p=c+np.matmul(kalman,(d-c))
     for i1 in range (0,3):
         predicted[i][i1]=p[i1]
print(predicted)
e=pd.DataFrame(predicted,columns=['A','B','C'])
e.to_csv('first_Station:.csv')
     






  

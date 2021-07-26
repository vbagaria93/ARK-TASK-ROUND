import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('Data1.csv')
j=df.to_numpy()
y=[]
for i in range (0,9999):
    y.append(i)
plt.plot(y,j[:,0])

plt.show()
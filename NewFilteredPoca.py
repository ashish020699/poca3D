'''
This Code uses NewFilteredPoca.txt File containing around 20.9k rows and 5 columns ... 
Columns 1-3 contain x,y,z axes of Poca Points 
Column 4 contains scattering distance which can be used as color for Plotting 
Multiple Poca points are  being Displayed and a scatterplot is generated

'''
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

headers = ["px","py","pz","color_angle","not_reqd"]
df = pd.read_csv("NewFilteredPoca.txt",delimiter = " ",names = headers)
print (df.shape)

xList = []
yList = []
zList = []
aList=[]
for index in range (df.shape[0]):
   if((index%10000)==0):
        print("Num of Events processed : "+str(index))
   row = df.iloc[index]
   Poca_x = float(row[0])
   Poca_y = float(row[1])
   Poca_z = float(row[2])
   Color  = float(row[3])
   xList.append(Poca_x)
   yList.append(Poca_y)
   zList.append(Poca_z) 
   aList.append(Color)
print (len(xList))
#print (len(yList))
#print (len(zList))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
cm = plt.get_cmap("RdYlGn")
xArray = np.array(xList)
yArray = np.array(yList)
zArray = np.array(zList)
N = len(aList)
col=np.arange(N)

colAList=[]
for val in aList:
    colAList.append(val*1000000)
ax.scatter(xArray,yArray,zArray,s=1) # for default color
#ax.scatter(xArray,yArray,zArray,s=1,c=aList,cmap=cm) # for Colormap
plt.show()

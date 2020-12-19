import numpy
import csv
from scipy.ndimage.filters import laplace
from scipy.ndimage.measurements import label
import scipy.signal
import scipy.interpolate
import matplotlib.pyplot as plt

weight_file = open("target.csv", 'r') # 读取前两行作为x,y
weight_list = weight_file.readlines()
weight_file.close()

input_x = numpy.asfarray(weight_list[0].split(','))
input_y = numpy.asfarray(weight_list[1].split(','))
#-----------------原始数据--------------------
tck = scipy.interpolate.splrep(input_x, input_y) # 生成用于绘制b样条的准备数据，每一个x对应一个(t,c,k)，包含the vector of knots, the B-spline coefficients, and the degree of the spline.
y_bspline = scipy.interpolate.splev(input_x, tck,der=0) # der = 0 即原始的B样条拟合。
output_y = scipy.interpolate.splev(input_x, tck,der=1) # der = 1 即一次求导
#-----------------原始数据--------------------

#------------------处理后---------------------
input_y_SG = scipy.signal.savgol_filter(input_y,21,2) #首先对y进行一次 Savitzky-Golay 滤波，时间窗21，2阶多项式
tck_SG = scipy.interpolate.splrep(input_x, input_y_SG) 
y_bspline_SG = scipy.interpolate.splev(input_x, tck_SG,der=0) 
output_y_SG = scipy.interpolate.splev(input_x, tck_SG,der=1) 
output_y_SG = scipy.signal.savgol_filter(output_y_SG,11,3) #首先对y进行第二次 Savitzky-Golay 滤波，时间窗11，3阶多项式
#------------------处理后---------------------

plt.figure()
plt.grid(True)

plt.plot(input_x, y_bspline,':',label="locomotion")
plt.plot(input_x, output_y,':',label="velocity")

plt.plot(input_x, y_bspline_SG,'b--',label="locomotion_SG")
plt.plot(input_x, output_y_SG,'r--',label="velocity_SG")

plt.legend(loc='best') # 绘制图例
plt.ylabel("[m]")
plt.xlabel("time[s]")

plt.show()



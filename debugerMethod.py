import matplotlib.pyplot as plt   # 导入模块 matplotlib.pyplot，并简写成 plt 
import matplotlib.ticker as ticker
import numpy as np                # 导入模块 numpy，并简写成 np
'''
a = [0,0.2,-0.1]
St = 0.2
T = 0.1
s = 0
for ai in a :
    s += ai
if(s == 0):
    s = 1
    a[0] = 1
for i in range(len(a)):
    a[i] *= St*T/s
    ''' 


x = np.linspace(0, 2, 500)
A = 0.2*x-0.1*x**2     # 曲线 A

plt.figure() 
plt.plot(x, A, label="A") # 绘制曲线 A
plt.show()
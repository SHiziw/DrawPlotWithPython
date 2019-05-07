import matplotlib.pyplot as plt   # 导入模块 matplotlib.pyplot，并简写成 plt 
import numpy as np                # 导入模块 numpy，并简写成 np

Time = np.linspace(0, 1.5, 500)
A = 0.75*(50/120)*30*(1-np.exp(-20*Time))*np.sin(15.7*Time)      # 曲线 A
B = 0.75*(70/120)*30*(1-np.exp(-20*Time))*np.sin(15.7*Time-0.6981)      # 曲线 B
C = 0.75*30*(1-np.exp(-20*Time))*np.sin(15.7*Time-1.3963)
D = 0.75*30*(1-np.exp(-20*Time))*np.sin(15.7*Time-2.0944)
E = 0.75*(70/120)*30*(1-np.exp(-20*Time))*np.sin(15.7*Time-2.7925)
F = 0.75*(50/120)*30*(1-np.exp(-20*Time))*np.sin(15.7*Time-3.49066)
plt.figure()    # 定义一个图像窗口
plt.plot(Time, A, label="A") # 绘制曲线 A
plt.plot(Time, B, label="B") # 绘制曲线 B
plt.plot(Time, C, label="C")
plt.plot(Time, D, label="D")
plt.plot(Time, E, label="E")
plt.plot(Time, F, label="F")
plt.xlabel("time[s]")
plt.ylabel("locomotion[mm]")
plt.legend(loc='best') # 绘制图例
plt.scatter([1.1], [-3.712027777219703], s=15, color="green") # 绘制小绿点
plt.annotate("t=1.1s", xy=(1.13, 13))   # 绘制旁边的文字t = 1.1s
plt.vlines(1.1, -22.5, 22.5, colors = "black", linewidth=1.5, linestyle="--") # 绘制黑色竖线

plt.show()
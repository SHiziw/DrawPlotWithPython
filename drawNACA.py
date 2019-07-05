import matplotlib.pyplot as plt   # 导入模块 matplotlib.pyplot，并简写成 plt 
import matplotlib.ticker as ticker
import numpy as np                # 导入模块 numpy，并简写成 np

cx=0.
cy=0.
c=0.5     # 轴线长度
t=0.2     # 控制机翼厚度
pivot=0.25  # 机翼俯仰运动的轴心所占轴线的比例
m=100

def drawpart1():
    addred(cx-c*pivot,cy)
    for i in range(1,101):
        xx = (i/m)**2.
        add(cx+c*(xx-pivot),cy+t*c*offset(xx))
    plt.xlim(-0.5,0.5)                          #设置x轴刻度范围
    plt.xticks(np.linspace(-0.5,0.5,7,endpoint=True)) # 设置x轴记号
    plt.ylim(-0.5,0.5)                          #设置y轴刻度范围

def drawpart2():
    addred(cx+c*(1-pivot),cy)
    for i in range(101,1,-1):
        xx = (i/m)**2.
        add(cx+c*(xx-pivot),cy-0.5*c*offset(xx))
    plt.xlim(-0.5,0.5)                          #设置x轴刻度范围
    plt.xticks(np.linspace(-0.5,0.5,5,endpoint=True)) # 设置x轴记号
    plt.ylim(-0.5,0.5)                          #设置y轴刻度范围 
    plt.yticks(np.linspace(-0.5,0.5,5,endpoint=True)) # 设置y轴记号   
def add(x,y):
    plt.scatter(x,y, s=5, color="green") # 绘制小绿点

def addred(x,y):
    plt.scatter(x,y, s=15, color="red") # 绘制小红点

def offset(x):
    return 5*(0.2969*np.sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)
  
drawpart1()
drawpart2()
'''
x = np.linspace(0, 1.5, 500)
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
'''

plt.show()
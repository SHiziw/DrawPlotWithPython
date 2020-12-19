import matplotlib.pyplot as plt   # 导入模块 matplotlib.pyplot，并简写成 plt 
import numpy as np                # 导入模块 numpy，并简写成 np
PI = 3.1415926
class wave_control:
    PI = 3.1415926
    def __init__(self, length, n, A, T, wave_length, degree = None):
        self.L = length
        self.n = n
        self.A = A
        self.T = T
        self.wave = wave_length
        self.degree = degree # 用来弧度角度转换
        
        self.dx = 2*PI*self.L/((n-1)*self.wave)
        self.freq = 1/self.T
        self.omg = 2*PI/self.T
        self.head = "(1-exp(-20*time))*"
        self.wave_part = self.head + "{:.2f}*cos({:.2f}*time-{:.3f}*i)"\
            .format(self.A, self.omg,self.dx)
    
    def show_wave_part(self):
        print("function: "+self.wave_part)
        return
    # 打印相关信息
    def show_data(self):        
        print("鳍条间距: {:.2f}".format(self.L/(self.n-1)))
        print("频率：{:.2f}".format(self.freq))
a = wave_control(length=148,n=7,A=10,T=0.4,wave_length=100) #10.5
a.show_wave_part()
a.show_data()


x = np.linspace(0, a.L, 500)
A = a.A*np.sin(-2*PI*x/a.wave)      # 曲线 A

plt.figure(figsize=(8,8), dpi=80)    # 定义一个图像窗口
plt.plot(x, A, label="A") # 绘制曲线 A

plt.xlim(0, a.L)
plt.ylim(-0.5*a.L, 0.5*a.L)
plt.xlabel("wave length[mm]")
plt.ylabel("locomotion[mm]")
plt.legend(loc='best') # 绘制图例


plt.show()

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import csv
 
plt.rcParams['font.sans-serif'] = ['STSong']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['mathtext.fontset'] = 'stix' # 设置数学字体为类times样式
 
def fourier(x, *a):
    w = 2 * np.pi / 0.622 #除以周期
    ret = 0
    for deg in range(0, int(len(a) / 2) + 1):
        ret += a[deg] * np.cos(deg * w * x) + a[len(a) - deg - 1] * np.sin(deg * w * x)
    return ret
 
 
def main(x, y):
    popt, pcov = curve_fit(fourier, x, y,p0 = [1] * 44)


    fig, axs = plt.subplots(2, 1,figsize=(5, 5)) # 页面全宽6.22
    axs[0].plot(x, y, color='r', label="原始曲线")
    axs[0].plot(x, fourier(x, *popt), color='g', label="拟合曲线")
    #axs[0].set_xlim(0, 2)
    axs[0].legend() # 打开图例
    axs[0].set_xlabel('time',fontsize=12) # 设置x坐标标题，字体大小
    axs[0].set_ylabel('locomotion',fontsize=12) # 设置y坐标标题，字体大小
    axs[0].tick_params(labelsize=12) # 设置刻度线字体大小（重要）
    axs[0].grid(True) # 打开网格线

 
    x1 = np.arange(1, 9, 1)
    y1 = popt[:35:-1]
    axs[1].plot(x1, y1, color='r', label="h rate")
    axs[1].set_ylabel('系数',fontsize=12)
    axs[1].set_xlabel('i',fontsize=12)
    axs[1].tick_params(labelsize=12) # 设置刻度线字体大小（重要）
    axs[1].grid(True)
    fig.tight_layout()
    plt.show()

    return popt
 
 
if __name__ == '__main__':
    x=[]
    y=[]
    with open('target_large_table.csv', 'r', newline='') as table_file:
        large_table = csv.reader(table_file)
        counter = 0
        for line in large_table:
            if counter == 0:
                #去除表头
                counter += 1
            else:
                temp_data = np.asfarray(line)
                x.append(temp_data[0])
                y.append(temp_data[1])
                counter += 1


    x = np.array(x)
    print(len(x))
    y = np.array(y)
    popt = main(x, y)
    print("参数如下：")
    print(popt)
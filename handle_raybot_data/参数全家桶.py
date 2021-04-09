import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np

    def draw_bar(self, labels, quants):
        width = 0.8
        ind = np.linspace(1, 66, 65)
        # 绘图参数全家桶
        params = {
            'axes.labelsize': '16',
            'xtick.labelsize': '16',
            'ytick.labelsize': '13',
            'lines.linewidth': '2',
            'legend.fontsize': '20',
            'figure.figsize': '26, 24'  # set figure size
        }
       pylab.rcParams.update(params)
       # make a square figure
       fig = plt.figure(1)
       ax = fig.add_subplot(111)
       # Bar Plot
       #横的柱状图
       ax.barh(ind - width / 2, quants, width, color='blue')
       #竖的柱状图
       #ax.bar(ind - width / 2, quants, width, color='blue')
       # Set the ticks on x-axis
       ax.set_yticks(ind)
       ax.set_yticklabels(labels)
       #竖的柱状图
       #ax.set_xticks(ind)
       #ax.set_xticklabels(labels)
       # labels
       ax.set_xlabel('xxx')
       ax.set_ylabel('xxxxxxxx')
       # title
       ax.set_title('xxxxxxxxxxxxx')
       plt.grid(True)
       #也可以这样设置图片大小
       #plt.figure(figsize=())
       #plt.show()
       plt.savefig("bar.jpg")
       plt.close()
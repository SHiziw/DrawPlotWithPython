import numpy
import csv
import scipy.signal
import scipy.interpolate
import matplotlib.pyplot as plt

propeller_time_s = []
propeller_thrust_N = []
counter = 0
level = 10

with open('target_large_table.csv', 'r', newline='') as table_file:
    large_table = csv.reader(table_file)
    for line in large_table:
        temp_data = numpy.asfarray(line)
        if counter == 0:
            propeller_time_s.append(temp_data[0]/1000)
            propeller_thrust_N.append(temp_data[1])
        counter += 1
        if counter == 10:
            counter = 0

with open("output_large_table.csv","w", newline='') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(propeller_time_s)
    writer.writerow(propeller_thrust_N)

#-----------------SG处理后--------------------
propeller_y_SG = scipy.signal.savgol_filter(propeller_thrust_N,101,2) #首先对y进行一次 Savitzky-Golay 滤波，时间窗21，2阶多项式
#tck_SG = scipy.interpolate.splrep(propeller_time_s, propeller_y_SG) 
#propeller_deriv_y_SG = scipy.interpolate.splev(propeller_time_s, tck_SG,der=0) 
propeller_deriv_y_SG = scipy.signal.medfilt(propeller_y_SG,kernel_size=101) #进行中值滤波
#propeller_deriv_y_SG = scipy.signal.savgol_filter(propeller_deriv_y_SG,211,4) #首先对y进行第二次 Savitzky-Golay 滤波，时间窗11，3阶多项式
#-----------------SG处理后--------------------

plt.figure()
plt.grid(True)

plt.plot(propeller_time_s, propeller_thrust_N,':',label="propeller_thrust")
plt.plot(propeller_time_s, propeller_deriv_y_SG,'r-',label="propeller_thrust(filter)")

plt.legend(loc='best') # 绘制图例
plt.ylabel("[m]")
plt.xlabel("time[s]")

plt.show()

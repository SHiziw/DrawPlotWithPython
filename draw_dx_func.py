import RayPID #导入的PID算法
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline


def test_pid(P, I , D, L):

    pid = RayPID.PID(P, I, D)

    pid.SetPoint=1
    sample_time=0.005 #采样间隔

    END = L # 总采样次数
    feedback = 0
    feedback2 = 0
    v=0
    v2=0
    feedback_list = []
    time_list = []
    feedback2_list = []

    for i in range(1, END):
        v+=(10-2*v)*sample_time
        feedback +=v*sample_time 
        feedback_list.append(feedback)
        v2+=(5-v2)*sample_time
        feedback2 +=v2*sample_time 
        feedback2_list.append(feedback2)
        time_list.append(i)

    time_sm = np.array(time_list)
    time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)
    feedback_smooth = spline(time_list, feedback_list, time_smooth)
    feedback2_smooth = spline(time_list, feedback2_list, time_smooth)
    plt.figure(0)
    plt.grid(True)
    plt.plot(time_smooth, feedback_smooth,'b-')
    plt.plot(time_smooth, feedback2_smooth,'r-')
    plt.xlim((0, L))
    plt.ylim((min(feedback_list)-0.5, max(feedback_list)+0.5))
    plt.xlabel('time ({0}s)'.format(L*pid.sample_time))
    plt.ylabel('PID (PV)')
    plt.title('PythonTEST PID',fontsize=15)



    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    test_pid(0.8, 0.9, 0.005, L=1000)
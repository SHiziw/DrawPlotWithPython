import numpy as np
import matplotlib.pyplot as plt
Time = 1.1
C = 0.75*30*(1-np.exp(-20*Time))*np.sin(15.7*Time-1.3963)
print(C)
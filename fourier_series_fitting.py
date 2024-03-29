from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
 
plt.rcParams['font.sans-serif'] = ['STSong']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['mathtext.fontset'] = 'stix' # 设置数学字体为类times样式
 
def fourier(x, *a):
    w = 2 * np.pi / 200
    ret = 0
    for deg in range(0, int(len(a) / 2) + 1):
        ret += a[deg] * np.cos(deg * w * x) + a[len(a) - deg - 1] * np.sin(deg * w * x)
    return ret
 
 
def main(x, y):
    popt, pcov = curve_fit(fourier, x, y, [1.0] * 100)
    plt.ylim(0, 700)
    plt.xlim(1, 201)
    plt.plot(x, y, color='r', label="original")
    plt.plot(x, fourier(x, *popt), color='g', label="fitting")
    plt.legend()
    plt.show()
    return popt
 
 
if __name__ == '__main__':
    x = np.arange(1, 201, 1)
    print(len(x))
    y = [490, 477, 467, 458, 450, 442, 433, 426, 419, 413, 411, 428, 445, 441, 434, 436, 446, 442, 427, 414, 402,
         391, 381, 372, 366, 363, 363, 364, 366, 372, 382, 397, 414, 430, 444, 460, 481, 502, 522, 539, 551, 561,
         567, 569, 568, 566, 570, 576, 578, 574, 565, 553, 541, 529, 519, 507, 496, 486, 494, 528, 551, 563, 576,
         596, 612, 624, 631, 636, 639, 640, 640, 638, 635, 633, 630, 625, 620, 615, 609, 603, 597, 590, 584, 578,
         571, 559, 541, 529, 524, 511, 486, 454, 422, 394, 372, 348, 340, 335, 334, 332, 332, 332, 332, 332, 333,
         336, 339, 341, 344, 349, 355, 360, 366, 372, 383, 396, 408, 419, 432, 448, 463, 473, 482, 493, 511, 530,
         551, 568, 580, 595, 597, 597, 595, 593, 598, 606, 619, 632, 642, 653, 659, 658, 653, 645, 640, 641, 643,
         650, 656, 659, 659, 655, 649, 640, 632, 626, 621, 614, 603, 590, 575, 564, 550, 530, 519, 507, 495, 484,
         472, 462, 452, 445, 437, 430, 423, 417, 423, 442, 445, 435, 423, 422, 431, 436, 428, 413, 401, 390, 381,
         373, 367, 363, 364, 365, 367, 371, 378, 396, 411, 428]
    # print(len(y))
    y = np.array(y)
    popt = main(x, y)
    print("参数如下：")
    print(popt)
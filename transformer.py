#这是一个程序，把时间序列进行切分
#@param threshold用来调整切分颗粒度
import matplotlib.pyplot as plt
import numpy as np
from numpy import repeat,tile
#首先建立一堆数据
nums = 0.3*np.random.randn(300,1)
for i in range(100):
    nums[i] += 1
for i in range(200,300):
    nums[i] += 10
#plt.plot(nums)
#plt.show()
sequence = tile(nums,(10,1))
#plt.plot(sequence)
#plt.show()
#开始进行拟合
stack = []
pre = 0
threshold = 10
for i in range(len(sequence)):
    if i > pre and np.sum(np.square(sequence[pre:i]-np.mean(sequence[pre:i]))) > threshold:
            stack.append(i)
            pre = i
print(stack)

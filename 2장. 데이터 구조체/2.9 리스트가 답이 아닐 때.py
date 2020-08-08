# 실수 천만개 -> array
# FIFO나 LIFO - deque
# 'item in my_collection' 많이 쓰고 항목 수가 많다 -> set

# array
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

fp=open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)

#memoryview
numbers = array('h', [-2 ,-1, 0, 1, 2])
memv = memoryview(numbers)
print(memv)
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)

#NumPy, SciPy
import numpy as np
a = np.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = 3, 4
print(a) # !
print(a[2])
print(a[2,1])
print(a[:,1])
print(a.transpose())

# ####
# floats = np.loadtxt('floats-10M-lines.txt')
# print(floats[-3:])
# floats *= .5
# print(floats[-3:])

# from time import perf_counter as pc
# t0 = pc()
# floats /= 3
# print(pc() - t0)
# np.save('floats-10M', floats)
# floats2 = np.load('floats-10M.npy', 'r+')
# floats2 *= 6
# print(floats2[-3:])

# deque(덱)
from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11,22,33])
print(dq)
dq.extendleft([10,20,30,40])
print(dq)
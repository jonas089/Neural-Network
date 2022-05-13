from numba import jit
from numba.experimental import jitclass
from numba import boolean, int32, float64, uint8
import time
import hashlib
spec=[
    ('a', int32),
    ('b', int32)
]

@jitclass(spec)
class a_CUDA_class():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
'''
@jit
def a_CUDA_func(instance, c, list):
    r = instance.addition()
    for i in range(0, 1000000000000000000):
        r += c
        #print(instance.addition() + c)
    print(r)

def a_CPU_func(instance, c):
    r = instance.addition()
    for i in range(0,1000):
        r += c
        #print(instance.addition() + c)
    print(r)

list = [1,2]

start = time.time()
instance = a_CUDA_class(5, 1)
a_CUDA_func(instance, 1, list)
print("CUDA: " + str(time.time()-start))

start = time.time()
a_CPU_func(instance, 1)
print("CPU: " + str(time.time()-start))
'''

# Comparing hashing power of CPU and GPU

@jit
def GPU(data):



def CPU(data):


def Compute_x_hashes(x)
    for i in range(0, x):
        data = str(c) + str(time.time())

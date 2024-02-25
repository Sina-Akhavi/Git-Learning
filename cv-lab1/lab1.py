import numpy as np

# l = [1, 2, 3]
# l1 = np.array(l)

# print(l1)
# print(type(l))
#
# zeros_list = np.zeros(10)
# print(zeros_list)
#
# print(l1.dtype)

# l1 = np.zeros(3, dtype=np.int64)
# print(l1)

# a = np.arange(10, dtype=np.int8)
# print(f'size={a.size}, ndim={a.ndim}, nbytes={a.nbytes}, itemsize={a.itemsize}')
#
# import sys
# sys_size = sys.getsizeof(a)
# print("sys_siz=", sys_size)

l1 = [1, 2, 3]
l2 = [3, 4, 5]

l3 = l1 + l2

l1 = np.array(l1)
l2 = np.array(l2)

l3 = l1 + l2
print(l3)

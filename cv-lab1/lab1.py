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

# l1 = [1, 2, 3]
# l2 = [3, 4, 5]
#
# l3 = l1 + l2
#
# l1 = np.array(l1)
# l2 = np.array(l2)
#
# l3 = l1 + l2
# print(l3)




# a = np.array([1, 2, 3], dtype=np.float64)
# print(a)
a = np.array([0,10,20,30,40, 50, 60, 70, 80, 90, 100])

# ---------------------- slicing -------------------------
# b = a[::-1]
# b[0] = 11
#
# print("b=", b)
# print("a=", a)
#
# b = a[[1, 2, 3, 3, 5]] # when You want elements in indices 1, 2, 3, 3 and 5
#
# print("what is b? ", b)

# ---------------------- 2D arrays -------------------------
A = np.array([[1, 2, 3], [2, 5, 6], [3, 3, 3]])
# print("A[1, 2]=", A[1, 2])
# a = A.shape[::-1]
# print("a=", a)

# m = A[0, :] # equal to A[0]
# m[0] = -1
# print(A)
# b = A[[0], :]

# A = np.array([1, 2, 3, 4])
# b = A[[2, 2, 3]]
# print('b=', b)

# b = A[:, [2]]
# print("b=", b)

# b = A[:, [2]]
# print("b=", b)

#
# A = np.array([1, 2, 3, 4])
# b = A[[[1], [3]]]
# print(b)


A = np.array([[1, 2, 3, 5], [2, 5, 6, 5], [3, 3, 3, 5]])
# r = np.array([0, 1, 0, 2, 2]) # select some elements in the first dimension
#
# print("output=", A[r, :])

# A[:, 0] = 1 # make elements in col1 zero
# print("A=", A)

# B = np.array([[1,1,1,1], [2,2,2,2], [3,3,3,3]])
# C = A * B
# print("C=", C)

# ----------------------- dot product for matrices -----------------------
A = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
B = np.array([[1,1,1], [2,2,2], [3,3,3], [2,2,2]])

C = np.dot(A, B)
print("C=", C)

print("mul=", A @ B)

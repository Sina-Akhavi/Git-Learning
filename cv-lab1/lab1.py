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
# A = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# B = np.array([[1,1,1], [2,2,2], [3,3,3], [2,2,2]])
#
# C = np.dot(A, B)
# print("C=", C)
#
# print("mul=", A @ B)

# ------------------------ creating random matrices ------------------------
# print(np.random.random((2, 3)), "\n\n")
#
# print(np.random.rand(2, 3))


# ------------------------ Numpy slices ------------------------
# A = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# b = A.copy() # creates a copy of A
#
# b[0] = 9
# print("A=", A)

# ------------------------------- Mask -------------------------------
# A = np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12]])

# Mask = np.array([[True, False, True, False],
#                  [True, True, False, False],
#                  [False, False, False, True]])
#
# print("masked A=", A[Mask])
#
#
# A[Mask] = 222
#
# print("A=\n", A)

# mask = A % 2 == 0
# A[mask] = -1
# print("A=", A)

# ------------------------ Operations on arrays ------------------------
# A = np.array([[1, 3, 4, 5],
#               [11, 3, 4, 5],
#              [1, 3, 4, 15]])
#
# print("A.max()=", A.max()) # maximum elements
# print("A.max(axis=0)=", A.max(axis=0)) # maximum elements in columns
# print("A.max(axis=1)=", A.max(axis=1)) # maximum elements in rows
# print("A.max(axis=1, keepdims=True)=", A.max(axis=1, keepdims=True)) # maximum elements in columns
#
# print("A.mean(axis=1)=", A.mean(axis=1)) # takes the average of each row

# ------------------------- concatenations -------------------------
X = np.array([[1,2],[3,4]])
Y = np.array([[10,20,30],[40,50,60]])
Z = np.array([[7,7],[8,8],[9,9]])

# A = np.concatenate((X,Z))
# print("A=", A)
# A = np.concatenate((X,Z), axis=0)
# print("A=", A)
#
# A = np.concatenate((X,Y), axis=1)
# print("A=", A)

# A = np.vstack((X,Z))
# print("A=", A)

# A = np.hstack((X,Y))
# print("A=", A)


# A = np.tile(Y,(4,3))
# print("A=", A)

# ------------------------------- Reshaping -------------------------------
# A = np.array([[1, 2],[3, 5]])
# (A_reshaped = A.reshape(4, 3)) === (A.shape = (4, 3))


# print("A_reshaped=", A)
# print("A=", A)

# ----------------------- ravel vs flatten -----------------------
A = np.array([[1, 2], [3, 5], [9, 9]])

a1 = A.flatten() # altering a1 does not affect A
a1[1] = -13
print("A=\n", A)

a2 = A.ravel() # altering a2 does affect A
a2[1] = -13
print("A=\n", A)

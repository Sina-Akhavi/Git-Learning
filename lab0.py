# i = 4
# print(type(i))

# float_i = 4.0
# print(type(float_i))

# l = [10, 20, 30, 40.2, 'salam']
# for k in l:
#     print(k)

# while 2 > 1:
#     print("Hi")

# ----------------- lambda function -----------------
# f = lambda x, y: x + y
#
# output = f(1, 2)
# print(output)

# ---------------- task1: matrix multiplication ----------------
def mul(A, B):
    m1 = len(A)
    n1 = len(A[0])

    m2 = len(B)
    n2 = len(B[0])

    if n1 != m2:
        return []

    output = [[0 for _ in range(n2)] for _ in range(m1)]

    for i in range(m1):  # A row
        for j in range(n2):  # B column
            for q in range(n1):
                output[i][j] += A[i][q] * B[q][j]

    return output


A = [[1, 0, 0],
     [0, 0, 3],
     [0, 2, 0]]

B = [[1, 1],
     [0, .5],
     [2, 1 / 3.0]]

C = [[1, 0, 0],
     [0, 0, 0.5],
     [0, 1 / 3.0, 0]]

print(mul(A, B))
print(mul(B,A))  # m x n    a * q
print(mul(A,C))
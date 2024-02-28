import numpy as np
import matplotlib.pyplot as plt
# A = np.array([[2, 3, 4],
#               [2, 4, 5]])
#
#
# A_reversed = A[::-1]
# # print(A_reversed)
#
# concatenated_array = np.concatenate((A, A_reversed), axis=0)
# print(f'concatenated_array=\n', concatenated_array)

# ---------------------- task 2 ----------------------
img = plt.imread('./masoleh_gray.jpg')

# print("img=\n",img)
# print("img type=\n", type(img))
# print("img shape=\n",img.shape)

concatenated_img = np.concatenate((img, img[::-1]), axis=0)
plt.imshow(concatenated_img, cmap='gray')
plt.show()

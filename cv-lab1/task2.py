import numpy as np
import matplotlib.pyplot as plt

# ---------------------- task 2 ----------------------
img = plt.imread('./masoleh_gray.jpg')

# print("img=\n",img)
# print("img type=\n", type(img))
# print("img shape=\n",img.shape)

concatenated_img = np.concatenate((img, img[::-1]), axis=0)
plt.imshow(concatenated_img, cmap='gray')
plt.show()

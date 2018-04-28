import numpy as np
from PIL import Image

img1 = "E.png"
img2 = "I.png"
img3 = "key1.png"
img4 = "key2.png"

e = Image.open(img1)
i = Image.open(img2)
k1 = Image.open(img3)
k2 = Image.open(img4)
W = 400
H = 300
temp = np.zeros((W, H), int) # an initial W*H list
E = np.array(e) # transform img to array
# print E
I = np.array(i)
K1 = np.array(k1)
K2 = np.array(k2)
w = [0, 0, 0]
# print temp

def Learing(W, H, E, I, K1, K2, w, temp): # define a function to learn the value of w
    m = [K1, K2, I]
    a = []
    e = []
    epoch = 1
    y = 0
    while (epoch==1 | epoch<(W*H) & np.abs(w[y]-w[y-1])):
        for x in range(W*H):
            a[x] = np.dot(w[x], m[x])
            e[x] = E[x] - a[x]
            w[x + 1] = w[x] + a * e[x] * m[x]
        epoch += 1
    y += 1
    return  w


# e = w1k1 + w2k2 + w3i
print(Learing(W, H, E, I, K1, K2, w, temp))
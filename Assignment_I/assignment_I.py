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
#temp = np.zeros((W, H), int) # an initial W*H list
E = np.array(e) # transform img to array
# print E
I1 = np.array(i)
K1 = np.array(k1)
K2 = np.array(k2)
w = [0, 0, 0]
# print temp

def Learing(W, H, E, I1, K1, K2, w): # define a function to learn the value of w
    #m = [K1, K2, I1]
    a = []
    e = []
    apha = 0.00001
    epoch = 1
    y = 0
    #while (epoch==1 or epoch<(W*H) and np.abs(w[y]-w[y-1])>0):
    for x in range(W*H):
        a[x] = w[0]*K1[x] + w[1]*K2[x] + w[3]*K3[x]
        e[x] = E[x] - a[x]
        w[0] = w[0] + apha*e[x]*K1[x]
        w[1] = w[1] + apha*e[x]*K2[x]
        w[2] = w[2] + apha*e[x]*I1[x]
    epoch += 1
    #y += 1
    return  w


# e = w1k1 + w2k2 + w3i
print(Learing(W, H, E, I1, K1, K2, w))
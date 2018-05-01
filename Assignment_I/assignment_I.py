import numpy as np
from PIL import Image

img1 = "E.png"
img2 = "I.png"
img3 = "key1.png"
img4 = "key2.png"
img5 = "Eprime.png"

e = Image.open(img1)
i = Image.open(img2)
k1 = Image.open(img3)
k2 = Image.open(img4)
q = Image.open(img5)
# W = 400
# H = 300
#temp = np.zeros((W, H), int) # an initial W*H list
E = np.array(e) # transform img to array
# print E
I1 = np.array(i)
K1 = np.array(k1)
K2 = np.array(k2)
K1 = K1.flatten()
K2 = K2.flatten()
I1 = I1.flatten()
E = E.flatten()
Q = np.array(q)
Q = Q.flatten()
# print temp

def Learing(E, I1, K1, K2, Q): # define a function to learn the value of w
    #m = [K1, K2, I1]
    w = [0, 0, 0]
    # a = []
    # e = []
    apha = 0.00001
    #epoch = 1
    W = 400
    H = 300
    ans = np.zeros(H*W)
    #y = 0
    #while (epoch==1 or epoch<(W*H) and np.abs(w[y]-w[y-1])>0):
    for x in range(W*H):
        a = w[0]*K1[x] + w[1]*K2[x] + w[2]*I1[x]
        e = E[x] - a
        w[0] = w[0] + apha * e * K1[x]
        w[1] = w[1] + apha * e * K2[x]
        w[2] = w[2] + apha * e * I1[x]
    #epoch += 1
    #y += 1

    for x in range(W*H):
        ans[x] = (Q[x] - K1[x]*w[0] - K2[x]*w[1]) / w[2]
    #print ans
    ans = ans.reshape((300, 400))
    print ans

    Final_img = Image.fromarray(ans)
    Image._show(Final_img)
    Final_img.save('Final_img.jpg')
    return w

# e = w1k1 + w2k2 + w3i
print(Learing(E, I1, K1, K2, Q))
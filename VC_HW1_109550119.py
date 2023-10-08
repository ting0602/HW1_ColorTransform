import cv2
import numpy as np

# RGB to YUV
def rgb2yuv(R, G, B):
    Y = 0.299 * R + 0.587 * G + 0.114 * B
    U = -0.169 * R - 0.331 * G + 0.5 * B + 128
    V = 0.5 * R - 0.419 * G - 0.081 * B + 128
    return Y, U, V

def rgb2ycbcr(R, G, B):
    Y = 0.299 * R + 0.587 * G + 0.114 * B
    Cb = 128 - 0.168736 * R - 0.331264 * G + 0.5 * B
    Cr = 128 + 0.5 * R - 0.418688 * G - 0.081312 * B
    return Y, Cb, Cr

# read image
image = cv2.imread("./lena.png")

# split R, G, B
R = image[:,:,2]
G = image[:,:,1]
B = image[:,:,0]

Y, U, V = rgb2yuv(R, G, B)
_, Cb, Cr = rgb2ycbcr(R, G, B)

# create grayscale images
R_gray = np.uint8(R)
G_gray = np.uint8(G)
B_gray = np.uint8(B)
Y_gray = np.uint8(Y)
U_gray = np.uint8(U)
V_gray = np.uint8(V)
Cb_gray = np.uint8(Cb)
Cr_gray = np.uint8(Cr)

# save grayscale images
cv2.imwrite("R_gray.png", R_gray)
cv2.imwrite("G_gray.png", G_gray)
cv2.imwrite("B_gray.png", B_gray)
cv2.imwrite("Y_gray.png", Y_gray)
cv2.imwrite("U_gray.png", U_gray)
cv2.imwrite("V_gray.png", V_gray)
cv2.imwrite("Cb_gray.png", Cb_gray)
cv2.imwrite("Cr_gray.png", Cr_gray)
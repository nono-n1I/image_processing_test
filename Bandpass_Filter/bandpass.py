import cv2
import numpy as np
# import matplotlib.pyplot as plt


def bandpass(img):
    # フーリエ変換
    out = np.fft.fft2(img)
    out = np.fft.fftshift(out)
    # out = 20*np.log(np.abs(out))

    # マスク処理
    img2 = cv2.imread("./img/bandmask.png", 0)
    img2 = cv2.resize(img2, out.shape[1::-1])
    out = out*(img2//255)

    # フーリエ逆変換
    out = np.fft.ifftshift(out)
    out = np.fft.ifft2(out)
    out = np.abs(out)
    return out


img = cv2.imread("./img/lenna.jpeg", 0)
out = bandpass(img)
cv2.imwrite('./Bandpass_Filter/bandpass.png', out)

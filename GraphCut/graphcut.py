import numpy as np
import cv2


img = cv2.imread('./img/soccer.jpeg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (50, 50, 450, 290)
mask2, bgdModel, fgdModel = cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

img = img*mask2[:, :, np.newaxis]
cv2.imwrite("./GraphCut/graph.png", img)

# newmask is the mask image I manually labelled
newmask = cv2.imread('./img/newmask.png', 0)

# whereever it is marked white (sure foreground), change mask=1
# whereever it is marked black (sure background), change mask=0

mask[newmask == 0] = 0
mask[newmask == 255] = 1

mask, bgdModel, fgdModel = cv2.grabCut(img, mask, None, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)

mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

img = cv2.imread('./img/soccer.jpeg')
out = img*mask[:, :, np.newaxis]

cv2.imwrite("./GraphCut/graph1.png", out)

import cv2
import sys

from skimage.feature import hessian_matrix, hessian_matrix_eigvals
from matplotlib import pyplot as plt


def detect_ridges(gray, sigma=1.0):
    H_elems = hessian_matrix(gray, sigma=sigma, order='rc')
    maxima_ridges, minima_ridges = hessian_matrix_eigvals(H_elems)
    return maxima_ridges, minima_ridges

try:
    src=sys.argv[1]
    try:
        out = sys.argv[2]
    except:
        out = False
except: 
    print('No source provided!\nplease run "python(3) script.py input-image optional-output-name optional-sigma-value(float) optional-anything-for-min-instead-if-max"')

img = cv2.imread(src, 0)

try:
    sigma = float(sys.argv[3])
except:
    sigma = 1
a, b = detect_ridges(img, sigma=sigma)

try:
    if sys.argv[4]:
        minimum = True
    else:
        minimum = False
except:
    minimum = False

if minimum:
    plt.imshow(b)
else:
    plt.imshow(a)
if out:
    plt.savefig(out)
else:
    plt.show()



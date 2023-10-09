import cv2
import numpy as np

width_img = 800
height_img = 800

def reduce_height(img):
    matrix = []
    row = np.vsplit(img,5)
    for r in row:
        col = np.hsplit(r,4)
        for c in col:
            matrix.append(c)
    return matrix

def sub_split(img):
    matrix = np.zeros((5,5))
    rows = np.vsplit(img,5)
    for r in range(len(rows)):
        col = np.hsplit(rows[r],5)
        for c in range(len(col)):
            matrix[r][c] = cv2.countNonZero(col[c])
    return matrix

def get_bubbles(address):
    img = cv2.imread(address) #read image
    img = cv2.resize(img,(width_img,height_img))

    imgWarpGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgWarpThres = cv2.threshold(imgWarpGray,140,255,cv2.THRESH_BINARY_INV)[1]
    matrix = reduce_height(imgWarpThres)

    marks = dict()
    q = 0
    for i in range(4):
        for j in range(5):
            threshold_matrix = sub_split(cv2.resize(matrix[i+4*j],(300,300)))
            for row in threshold_matrix:
                marks[q+1] = np.where(row == np.amax(row))[0][0]
                q += 1
    return marks

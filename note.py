# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:24:04 2022

@author: Admin
"""

import random
import numpy as np

# slicing array
# https://www.hashbangcode.com/article/slicing-arrays-and-strings-using-colon-operator-python
arr = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(arr[1][0])
print("-----------")
print(arr[1])
print("-----------")
print(arr[1:])
print("-----------")
print(arr[0:2][:])
print("-----------")
print(arr[0:2][1:])
print("-----------")
print(arr[0:2:2])
print("-----------")
#slice nested array, get index 1 only
print(arr[:,1])
print("-----------")
#slice nested array, get array starting from index 1 until 2
print(arr[:,1:2])

#init array using for
print("=======================")
points = [0,1,2,3,4,5]
arr2 = np.array([p for p in points])
print(arr2)

# nupmpy clip
a = np.arange(10)
np.clip(a, 1, 8)
np.clip(a, 8, 1)
np.clip(a, 3, 6, out=a)
a = np.arange(10)
np.clip(a, [3, 4, 1, 1, 1, 4, 4, 4, 4, 4], 8)

# =======================================================
# import mat file than save as npy file
# 
import scipy.io as io
import numpy as np

mat = io.loadmat("C:\\Users\\Admin\\Desktop\\data\\TA\\Projek\\Dataset\\ShanghaiTech\\part_B\\test_data\\ground-truth\\GT_IMG_1.mat")
annotations = np.array(mat['image_info'][0][0][0][0][0])
savePath = "C:\\Users\\Admin\\Desktop\\data\\TA\\Projek\\Dataset\\Coba\\val\\IMG_1"
np.save(savePath, np.array(annotations))
print(np.load(savePath+".npy"))
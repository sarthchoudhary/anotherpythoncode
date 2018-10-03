# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:04:52 2018

@author: Sarth.choudhary
"""
import cv2
import numpy as np
import copy
#r'C:\Users\Sarth.choudhary\Desktop\Untitled Export\DSC_5202LR.jpg'
original_image = cv2.imread(r'C:\Users\Sarth.choudhary\Desktop\Untitled Export\DSC_5202LR.jpg')
[m,n,l] = original_image.shape
flipped_image= np.zeros(original_image.shape)
#flipped_image= copy.deepcopy(original_image)
for i in range(m):
    for j in range(n):
#        flipped_image[i,j,0]= original_image[i,n-j-1,0]
#        flipped_image[i,j,1]= original_image[i,n-j-1,1]
        flipped_image[i,j,:]= original_image[i,n-j-1,:]
cv2.resize(flipped_image, (0,0), fx=0.5,fy=0.5)
#from matplotlib import pyplot as plt
#plt.imshow(flipped_image)
cv2.imshow('flipped_image', flipped_image)
cv2.imwrite(r'C:\Users\Sarth.choudhary\Desktop\Untitled Export\flipped_image.png', flipped_image)
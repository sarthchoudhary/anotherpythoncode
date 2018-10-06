# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:44:18 2018

@author: Sarth.choudhary
"""

#Limb darkening correction
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import cv2
plt.close('all')
image_path = r'D:\IIA\Internship\Kodaikanal\H alpha20170803\Ha_20170803_103334940.fits'
flat_path = r'D:\IIA\Internship\Kodaikanal\H alpha20170803\Flat_20170803_112801100.fits'
dark_path = r'D:\IIA\Internship\Kodaikanal\H alpha20170803\Dark_20170803_133407830.fits'
def fitsread(file_path):
    return fits.getdata(file_path)
test_image = fitsread(image_path)
#plt.figure()
#plt.imshow(np.squeeze(test_image), cmap = 'gray')
flat = fitsread(flat_path)
dark = fitsread(dark_path)
def flat_fielding(test_image, dark, flat):
    return (test_image-dark)/(flat-dark)
test_image = flat_fielding(test_image,dark,flat)
plt.figure()
test_image= np.squeeze(test_image)
plt.imshow(test_image, cmap='gray')
intensity = []
for i in range(test_image.shape[0]):
    intensity.append(test_image[i][1024])
plt.figure()
plt.plot(intensity)
'''sobel filter operation'''
from scipy.ndimage.filters import gaussian_filter
blurred_image = gaussian_filter(test_image, sigma=2, truncate=0.75)
#plt.figure()
#plt.imshow(blurred_image, cmap='gray')
from scipy.signal import convolve2d
def detect_edge(img, thresh):
    sobelx = ([[-1,0,1], [-2,0,2], [-1,0,1]])
    sobely = ([[-1,-2,-1],[0,0,0],[1,2,1]])
    gradimgx = np.copy(img)
    gradimgy = np.copy(img)
    gradimgx = convolve2d(gradimgx, sobelx, mode='same')/4.0
    gradimgy = convolve2d(gradimgy, sobely, mode='same')/4.0
    anglegrad = np.arctan2(gradimgy, gradimgx)
    maggrad = np.sqrt(np.square(gradimgy) + np.square(gradimgx))
    isEdge = np.greater_equal(maggrad, thresh)
    return isEdge, anglegrad, maggrad
isEdge,anglegrad,maggrad = detect_edge(blurred_image, 0.035) #0.03
plt.figure()
plt.imshow(maggrad, cmap='gray')
plt.figure()
plt.imshow(isEdge, cmap='gray')




# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:34:30 2018

@author: Sarth.choudhary
"""
from astropy.io import fits
import matplotlib.pyplot as plt
import cv2
plt.close('all')
import numpy as np
image_pathB = r'D:\IIA\Internship\kavalur\2017june17\17june2017_saturn_B01.fits'
image_pathV = r'D:\IIA\Internship\kavalur\2017june17\17june2017_saturn_V01.fits'
image_pathR = r'D:\IIA\Internship\kavalur\2017june17\17june2017_saturn_R01.fits'
#image_pathB=r'D:\IIA\Internship\kavalur\2017june17\17june2017_Neptune_B01.fits'
#image_pathV=r'D:\IIA\Internship\kavalur\2017june17\17june2017_Neptune_V01.fits'
#image_pathR=r'D:\IIA\Internship\kavalur\2017june17\17june2017_Neptune_R01.fits'
test_imageB = fits.getdata(image_pathB)
test_imageV = fits.getdata(image_pathV)
test_imageR = fits.getdata(image_pathR)
dark = fits.getdata(r'D:\IIA\Internship\kavalur\2017june17\17june2017_dark01.fits')
flatB =fits.getdata(r'D:\IIA\Internship\kavalur\2017june17\sflat_B01.fits')
flatV =fits.getdata(r'D:\IIA\Internship\kavalur\2017june17\sflat_V01.fits')
flatR =fits.getdata(r'D:\IIA\Internship\kavalur\2017june17\sflat_R01.fits')
#test_image = np.squeeze(test_image)
#flat_fielding
def flat_fielding(img,flat_frame,dark_frame):
    return np.abs((img-dark_frame)/(flat_frame-dark_frame))
test_imageR = flat_fielding(test_imageR,flatR,dark)
test_imageV = flat_fielding(test_imageV,flatV,dark)
test_imageB = flat_fielding(test_imageB,flatB,dark)
plt.imshow(test_imageB, cmap = 'gray') # cmap = 'gray'
plt.figure()
plt.imshow(test_imageV, cmap = 'gray')
plt.figure()
plt.imshow(test_imageR, cmap = 'gray')
final_image = np.zeros(shape=(test_imageB.shape[0],test_imageB.shape[1],3), dtype = float)
final_image[:,:,0] = 0.4*test_imageR
final_image[:,:,1] = 0.3*test_imageV
#final_image[:,:,1] = test_imageR - test_imageV
final_image[:,:,2] = 0.3*test_imageB
plt.figure()
plt.imshow(final_image)
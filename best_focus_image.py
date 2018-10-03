# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 22:41:27 2018

@author: Sarth.choudhary
"""
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import cv2
#from scipy.optimize import curve_fit
plt.close('all')
star_loc = (1640,2549) #approximate (x,y) coordinates of star
contour_radius = 100
#from Ipython import get_ipython
test_image = fits.getdata(r'D:\IIA\Internship\kavalur\auto_focus(2)\22aug2018_WASP33_V_024.fits')
test_image1 = np.squeeze(test_image)
test_image1 = test_image1 - np.mean(test_image1)*np.ones(test_image1.shape) #background substraction
(m,n) = test_image1.shape
for i in range(m):
    for j in range(n):
        if test_image1[i,j]<0:
            test_image1[i,j] = 0
plt.figure()
plt.imshow(test_image1, cmap='gray', interpolation='None')
plt.title('Test Image')
#get_ipython().run_line_magic('matplotlib', 'qt')
my_mask = np.squeeze(np.zeros(test_image.shape, dtype=np.uint16))
cv2.circle(my_mask,star_loc, contour_radius, (1,1,1),-1,8,0)
plt.figure()
plt.imshow(my_mask, cmap='gray')
plt.title('Mask')
#result_array = test_image1 & my_mask
result_array = np.multiply(test_image1, my_mask)
plt.figure()
plt.imshow(result_array, cmap ='gray', interpolation='none')
plt.title('Selected Region')
y0, x0 = np.where(result_array == result_array.max())
y0 = int(y0); x0= int(x0)
intensity = []
x1 = x0 - contour_radius
x2 = x0 + contour_radius
for i in range(x1,x2+1): #change x1,x2 for vertival, 45deg etc line cuts and take avg.
    intensity.append(result_array[y0,i])
plt.figure()
plt.plot(range(x1, x2+1), intensity)
plt.title('intensity variation')

#x = np.linspace(0,200,199)
#x = range(0,2*contour_radius)
x = np.arange(x1,x2+1)
#y = intensity
#initial_vals = [1,0,1]
def gaussian(x,amp,cen,wid):
    return amp*np.exp(-(x-cen)**2/wid)
#best_val, covar = curve_fit(gaussian, x,y)
#[amp,cen,wid] = best_val
#fitted_intensity=[]
#for x in range(x1, x2):
#    fitted_intensity.append(gaussian(x,amp,cen,wid))
#plt.figure()
#plt.plot(fitted_intensity)
###
from lmfit import Model
gmodel = Model(gaussian)
#params = gmodel.make_params()
#params = gmodel.make_params(amp=1, cen=0, wid=1)
params = gmodel.make_params(amp=14000, cen=1640, wid=50)
fitted_intensity = gmodel.fit(intensity, params, x=x) #check?
plt.plot(x, fitted_intensity.best_fit, '-g')
result=fitted_intensity.best_fit
center_intensity = np.max(fitted_intensity.best_fit)
gaussian_center = np.argmax(fitted_intensity.best_fit)
#FWHM = 0
for i in range(contour_radius+1):
    if fitted_intensity.best_fit[gaussian_center + i] >= center_intensity/2:
#        FWHM = FWHM + 1
        continue
    else:
        break
print('FWHM :' + str(2*i))
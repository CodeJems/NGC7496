#%%
# from statistics import NormalDist
from astropy.visualization import make_lupton_rgb
import matplotlib.pyplot as plt
# from matplotlib.colors import LogNorm
import numpy as np
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits

# image_file = get_pkg_data_filename('F770W\jw02107-o038_t019_miri_f770w_segm.fits')

# img1 = get_pkg_data_filename('F770W\jw02107-o038_t019_miri_f770w_segm.fits')
# img2 = get_pkg_data_filename('F1000W\jw02107-o038_t019_miri_f1000w_segm.fits')
# img3 = get_pkg_data_filename('F1130W\jw02107-o038_t019_miri_f1130w_segm.fits')
# img4 = get_pkg_data_filename('F2100W\jw02107-o038_t019_miri_f2100w_segm.fits')
# Img test
img1 = get_pkg_data_filename('F770W\jw02107-o038_t019_miri_f770w_i2d.fits')
img2 = get_pkg_data_filename('F1000W\jw02107-o038_t019_miri_f1000w_i2d.fits')
img3 = get_pkg_data_filename('F1130W\jw02107-o038_t019_miri_f1130w_i2d.fits')
img4 = get_pkg_data_filename('F2100W\jw02107-o038_t019_miri_f2100w_i2d.fits')

img1.info()

fits.info(img4)
# Img1 770W
img1d = fits.getdata(img1, ext=1)
# print(image_data.shape)
# plt.figure()
# plt.imshow(img1d,'BuPu')
# plt.colorbar()

# Img2 1000W
img2d = fits.getdata(img2, ext=1)
# print(image_data.shape)
# plt.figure()
# plt.imshow(img2d,'YlGnBu')
# plt.colorbar()

# Img3 1130W
img3d = fits.getdata(img3, ext=1)
# print(image_data.shape)
# plt.figure()
# plt.imshow(img3d,'YlOrRd')
# plt.colorbar()

# Img4 2100W
img4d = fits.getdata(img4, ext=1)
# print(image_data.shape)
# plt.figure()
# plt.imshow(img4d,'Reds')
# plt.colorbar()

# %%
# Add images together into a list
img_arr = [img1d,img2d,img3d,img4d]
img_combo = np.zeros(shape=img_arr[0].shape)

for x in img_arr:
    img_combo += x
    
# %%
bin_val = []
for x in range(0,300):
    bin_val.append(x)
print(bin_val)
histo = plt.hist(img_combo.flatten(), bins=bin_val)
# %%
plt.imshow(img_combo,cmap='binary_r',vmin=253,vmax=330)
plt.colorbar()
# %%
# Let's make an RGB image using 2,3,4
bin_val_rgb = []
for x in range(210,220):
    bin_val_rgb.append(x)
# print(bin_val_rgb)
r = img2d+img1d
g = img3d
b = img4d

# [14,28,213]
rgb_arr = [r,g,b]
for ind,y in enumerate(rgb_arr):
    rgb_arr[ind]=np.zeros(shape=rgb_arr[ind].shape)
# print(rgb_arr)
rgb_test = make_lupton_rgb(r,g,b,minimum=[20,22,219],filename='NGC7496_rgb_test.jpeg',Q=20000,stretch=0.05)
# rgb_test = make_lupton_rgb(r,g,b,minimum=[0,0,],Q=50000,stretch=0.25)
# histo_rgb = plt.hist(rgb_test.flatten(), bins = bin_val_rgb)
# histo_r = plt.hist(b.flatten(),bins = bin_val_rgb)
# plt.imshow(rgb_test,norm=Log,Norm(vmin=900))
print('Next')
plt.imshow(rgb_test)
# %%

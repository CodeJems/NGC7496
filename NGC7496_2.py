#%%
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.visualization import make_lupton_rgb

img1 = fits.open('F770W\jw02107-o038_t019_miri_f770w_i2d.fits')
img2 = fits.open('F1000W\jw02107-o038_t019_miri_f1000w_i2d.fits')
img3 = fits.open('F1130W\jw02107-o038_t019_miri_f1130w_i2d.fits')
img4 = fits.open('F2100W\jw02107-o038_t019_miri_f2100w_i2d.fits')
# %%
# img1[0].header

img1data = img1[1].data
img2data = img2[1].data
img3data = img3[1].data
img4data = img4[1].data
# img1data.shape
# plt.imshow(img4data,cmap='gray',vmin=240,vmax=300)
# %%
plt.imshow(img1data,cmap='gray',vmin=5.2,vmax=11.9)
# %%

plt.imshow(img2data,cmap='gray',vmin=14.1,vmax=22)
# %%
plt.imshow(img3data,cmap='gray',vmin=20.9,vmax=35)
# %% Img 4 suffers from really bad distortion and shouldn't be included in final image
img4[1].header
bins_val = []
for x in range(210,235):
    bins_val.append(x)
plt.hist(img4data.flatten(),bins=bins_val)
# plt.imshow(img4data,cmap='gray',vmin=213.5,vmax=220)
# %%
r = img1data
g = img2data
b = img3data
rmin = 5.2
gmin = 14.1
bmin = 20.9
print(r.shape,g.shape,b.shape)
rgb_img = make_lupton_rgb(b,g,r,minimum=[bmin,gmin,rmin],stretch=5,Q=10,filename='NGC7749_magenta.jpg')
plt.axis('off')
plt.imshow(rgb_img,origin = 'lower')
# %%

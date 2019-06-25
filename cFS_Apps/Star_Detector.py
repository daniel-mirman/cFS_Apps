from matplotlib import pyplot as plt
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
from skimage.io import imread
from skimage import data
from math import sqrt

import glob
import numpy as np


image= glob.glob("/Users/danielmirman/Desktop/messier4K.tiff")[0]
grayscale = imread(image, as_gray=True)

# Compute radii in the 3rd column.
blobs_log = blob_log(grayscale, max_sigma=30, num_sigma=10, threshold=.1)
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
numStars1 = len(blobs_log)
stars1 = print('Number of stars counted Photo 1: ', numStars1)


blobs_dog = blob_dog(grayscale, max_sigma=30, threshold=.1)
blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)
numStars2 = len(blobs_dog)
stars2 = print('Number of stars counted Photo 2: ', numStars2)


blobs_doh = blob_doh(grayscale, max_sigma=30, threshold=.01)
numStars3 = len(blobs_doh)
stars3 = print('Number of stars counted Photo 3: ', numStars3)



blobs_list = [blobs_log, blobs_dog, blobs_doh]

# Visualization Information
colors = ['lime', 'yellow', 'red']

#stars = [stars1, stars2, stars3]

titles = ['Laplacian of Gaussian', 'Difference of Gaussian', 
	  'Difference of Hessian']

sequence = zip(blobs_list, colors, titles)

fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharex=True, sharey=True)
ax = axes.ravel()

for idx, (blobs, color, title) in enumerate(sequence):
    ax[idx].set_title(title)
    #ax[idx].set_title(star)
    ax[idx].imshow(grayscale, cmap='gray', interpolation='nearest')
    
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=.5, fill=False)
        ax[idx].add_patch(c)
    ax[idx].set_axis_off()

plt.tight_layout()
plt.show()

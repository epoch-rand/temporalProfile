
# temporalProfile v1.0 | 2020 | EPOCH Foundation
# This work is licensed under the GNU GENERAL PUBLIC LICENSE

# Project ID: o4CXRskH

# Official configs for EPOCH_temporalProfile.

#----------------------------------------------------------------------------

import os

import cv2 as cv
import numpy as np

import scipy.misc

#----------------------------------------------------------------------------

img_root = '/datasets/vimeo_90k/123'

#----------------------------------------------------------------------------

w_point = 224                # Choose weight-coordinate to be transferred to profile
img_height = 256

sequence = sorted(os.listdir(img_root))

p_length = len(sequence)

profile = np.zeros(shape = (p_length, img_height, 3))
print("Temporal Profile Shape:", profile.shape)
print("No. of frames:", p_length)

#----------------------------------------------------------------------------

i = 0
for image in sequence:

    frame = cv.imread(os.path.join(img_root, image))

    line = frame[:,w_point,:]
    profile[i,:,:] = line

    i += 1

#----------------------------------------------------------------------------

cv.imwrite('temporalProfile.png', profile)
print("Profile saved to disk")

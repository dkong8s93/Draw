### Imports
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import cv2

### Helpers
import helpers.image_processing as ip

### Main title
st.title('Draw')

### Image to experiment with
img_fname = "resources/ichigo.png"
img = ip.read_img(img_fname)

### Sidebar
blur_type = st.sidebar.selectbox("Image blur type (low pass filter)",
                                ("Average", "Gaussian", "Median"))

blur_kernel_size = st.sidebar.slider("Kernel size",
                                     min_value=3,max_value=35,step=4)

canny_threshold = st.sidebar.slider("Canny line detection threshold",
                                    min_value=1,max_value=75,value=30,step=1)

binary_inv_threshold = st.sidebar.slider("Binary inverse threshold",
                                         min_value=1,max_value=100,value=50,step=1)

### Image processing
img_blur = ip.blur_img(img,blur_type,blur_kernel_size) # Blur
img_line = ip.get_lines(img_blur,canny_threshold)           # Line detection
img_binary = ip.binary_inv(img_line,binary_inv_threshold)   # Binary inverse thresholding

### Canvas
fig,(ax_blur,ax_line,ax_threshold) = plt.subplots(1,3,
                                                  sharex='col',sharey='row',
                                                  gridspec_kw={'hspace': 0,'wspace': .1},
                                                  figsize=(30,15))

ax_blur.imshow(img_blur,cmap="gray")
ax_blur.set_title(f'{blur_type} blurring',fontsize=40)
ax_line.imshow(img_line,cmap="gray")
ax_line.set_title(f'Canny line detection',fontsize=40)
ax_threshold.imshow(img_binary,cmap="gray")
ax_threshold.set_title(f'Binary thresholding',fontsize=40)

st.pyplot(fig)

### Imports
import streamlit as st
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

### Helpers
import helpers.image_processing as ip
import helpers.sidebar as sb
import helpers.dashboard as db

### Main title
st.title('Image Process Tuning')

### Image to experiment with
fnames = list(filter(lambda f: ".png" in f or ".jpg" in f, os.listdir("resources/")))
img_fname = st.selectbox("Pick an image to experiment with", fnames, index=0)
img_rgb = cv2.cvtColor(cv2.imread(f"resources/{img_fname}"),cv2.COLOR_BGR2RGB)
img_gray = ip.read_img(f"resources/{img_fname}")

### Sidebar
sb.create_sidebar(img_rgb,img_gray)

### Image processing
imgs_processed = ip.process_img(img_gray)

### Dashboard
db.create_dashboard(imgs_processed)
# fig,(ax_blur,ax_line,ax_threshold) = plt.subplots(1,3,
#                                                   sharex='col',sharey='row',
#                                                   gridspec_kw={'hspace': 0,'wspace': .01},
#                                                   figsize=(30,15))

# ax_blur.imshow(img_blur,cmap="gray")
# ax_blur.axis('off')
# ax_blur.set_title(f'{blur_type} blurring',fontsize=40)
# ax_line.imshow(img_line,cmap="gray")
# ax_line.set_title(f'Canny line detection',fontsize=40)
# ax_line.axis('off')
# ax_threshold.imshow(img_binary,cmap="gray")
# ax_threshold.set_title(f'Binary thresholding',fontsize=40)
# ax_threshold.axis('off')
#
# st.pyplot(fig)

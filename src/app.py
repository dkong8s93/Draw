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

### Dashboard
db.create_dashboard(img_gray)

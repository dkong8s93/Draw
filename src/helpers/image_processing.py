# Imports
import cv2
import streamlit as st

# Read image
@st.cache
def read_img(img_fname):
    img = cv2.imread(img_fname)
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Blurring
def blur_img(img,blur_type="Average",blur_kernel_size=3):
    k = blur_kernel_size
    if blur_type == "Average":
        return cv2.blur(img, (k,k))
    elif blur_type == "Gaussian":
        return cv2.GaussianBlur(img, (k,k), 0)
    elif blur_type == "Median":
        return cv2.medianBlur(img, k)

# Line detection
def get_lines(img,thresh):
    return cv2.Canny(img,thresh,3*thresh)

# Binary inverse thresholding
def binary_inv(img,thresh):
    return cv2.threshold(img,thresh,255,cv2.THRESH_BINARY_INV)[1]

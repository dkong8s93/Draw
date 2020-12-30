### Imports
import streamlit as st
import matplotlib.pyplot as plt

def create_sidebar(img_rgb,img_gray):
    fig,(ax_0,ax_1) = plt.subplots(2,1,figsize=(5,10))
    ax_0.imshow(img_rgb)
    ax_0.set_title("Original Image (RGB)",fontsize=30)
    ax_0.axis("off")
    ax_1.imshow(img_gray,cmap="gray")
    ax_1.set_title("Original Image (gray)",fontsize=30)
    ax_1.axis("off")
    st.sidebar.pyplot(fig)

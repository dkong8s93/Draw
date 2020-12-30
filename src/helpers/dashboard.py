### Imports
import streamlit as st
import matplotlib.pyplot as plt

# Constants
from config.constants import *
import helpers.image_processing as ip

def create_dashboard(img_gray):
    imgs_processed = ip.process_img(img_gray)

    fig,axes = plt.subplots(4,4,sharex='col',sharey='row',
                            gridspec_kw={'hspace': 0,'wspace': 0},
                            figsize=(20,16))

    for i,imgs_blurred in enumerate(imgs_processed):
        for j,img_canny in enumerate(imgs_blurred):
            axes[i][j].imshow(img_canny,cmap="gray")
            axes[i][j].axis('on')
            axes[i][j].set_xticks([])
            axes[i][j].set_yticks([])
            axes[i][j].text(30,30,
                            f'Gaussian blur: {blur_kernel_size[j]}\nCanny line detection: {canny_threshold[i]}',
                            bbox={'facecolor': 'white', 'pad': 10})

    st.pyplot(fig)

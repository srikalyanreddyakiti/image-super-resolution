import streamlit as st  
import matplotlib.pyplot as pt
import pickle
import RRDBNet_arch as arch
import os.path as osp
import glob
import cv2
import numpy as np
import torch
import RRDBNet_arch as arch
from PIL import Image

#loading the trained model
pickle_in = open('D:\special project third year\models\RRDB_ESRGAN_x4.pth', 'rb') 
upscaler = pickle.load(pickle_in)

#containers in the web app
header = st.container()
drop_image = st.container()
HR_output = st.container()


with header:
    st.title("Welcome To the Super Resolution Tool!!")
    st.text("Upscaling your low resolution images has never been this easy With this tool you can upscale your images by 4 times")





with drop_image:
    st.header("Here is where the magic happens!!")
    in_img = (st.file_uploader("upload your low resolution image here",type=["jpg","png"]))
    st.image(in_img, caption="this is the image you uploaded -_-")

    
   # convert to numpy array
    image = Image.open(in_img)
    img_array = np.array(image)
    # scale pixel values to [0, 1]
    img_array/= 255.0
    img_array = torch.from_numpy(np.transpose(img_array[:, :, [2, 1, 0]], (2, 0, 1))).float()

    

with HR_output:
    with torch.no_grad():
        output = upscaler(in_img).in_img.squeeze().float().cpu().clamp_(0, 1).numpy()
        output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
        output = (output * 255.0).round()
        st.header("Here is your new high resolution image")
        st.image(output,caption = "this is the high resolution image!!")
import streamlit as st
import datetime
import requests
import numpy as np
import pandas as pd
import os
from deploy_model_custom import ObjectDetection
import subprocess

# with open('x264-output.mp4', 'rb') as f:
#     st.video(f)


### upload

st.markdown('''# Upload your video...''')

video_file = st.file_uploader('video', type = ['mp4'])

if video_file is not None:

    ### process video

    with open(os.path.join("input_vids",'uploaded_file.mp4'),"wb") as f:
        f.write((video_file).getbuffer())

    detection = ObjectDetection('models/20220311.pt',\
                                'input_vids/uploaded_file.mp4',\
                                'output_vids/mp4v_file.mp4')

    detection()

    comment = 'rm output_vids/x264_file.mp4'
    subprocess.call(comment, shell=True)

    comment = 'ffmpeg -i output_vids/mp4v_file.mp4 -vcodec libx264 -f mp4 output_vids/x264_file.mp4'
    subprocess.call(comment, shell=True)

    comment = 'rm output_vids/mp4v_file.mp4'
    subprocess.call(comment, shell=True)

    st.markdown('''# Here is what Kitt sees:''')
    video = 'output_vids/x264_file.mp4'
    video_file = open(video, 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

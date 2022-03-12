import streamlit as st
import datetime
import requests
import numpy as np
import pandas as pd
import os
from deploy_model_custom import ObjectDetection


### upload

st.markdown('''# Upload your video...''')

video_file = st.file_uploader('video', type = ['mp4'])

### process video



### play video

if video_file is not None:

    with open(os.path.join("input_vids",video_file.name),"wb") as f:
        f.write((video_file).getbuffer())

    detection = ObjectDetection('models/20220311.pt',\
                                'input_vids/'+video_file.name,\
                                'output_vids/sl_vid.mp4')

    detection()

    st.markdown('''# Here is what Kitt sees:''')
    video = 'output_vids/sl_vid.mp4'
    video_file = open(video, 'rb')
    video_bytes = video_file.read()

    # st.video(video_bytes, format="video/mp4", start_time=0)
    st.video(video_bytes)

    # video = video_file.read()
    # st.video(video, format="video/mp4", start_time=0)

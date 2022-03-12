import streamlit as st
import datetime
import requests
import numpy as np
import pandas as pd

### upload

st.markdown('''# Upload your video...''')

video_file = st.file_uploader('video', type = ['mp4'])

### process video



### play video

if video_file is not None:

    st.markdown('''# Here is what Kitt sees:''')
    video = video_file.read()
    st.video(video, format="video/mp4", start_time=0)

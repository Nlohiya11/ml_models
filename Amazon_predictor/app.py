import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import streamlit as st
from multipage import MultiApp
from app import backend,frontend

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpapercave.com/wp/JUbQu94.jpg");
background-size: 200%;
background-position: centre;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(80,120,230,140);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Amazon")
app = MultiApp()
app.add_app("Create Data of your product", frontend.app)
app.add_app("Sort by : ", backend.app)
app.run(0)
app.run(1)

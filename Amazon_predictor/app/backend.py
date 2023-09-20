import pandas as pd
import numpy as np
from PIL import Image
import urllib.request
import streamlit as st


def app():
    mf = pd.read_csv('data.csv')
    if len(mf) > 0:
        max_stars = max(mf['Stars'])
        min_stars = min(mf['Stars'])
        max_rating = max(mf['Rating'])
        min_rating = min(mf['Rating'])
        max_price = max(mf['Price'])
        min_price = min(mf['Price'])
        list_of_option = ['Price', 'Rating', 'Stars']
        pil = st.selectbox('Choose Your Requirement', list_of_option)
        if st.button('find'):
            if pil == 'Price':
                numberq = 0
                for index, row in mf.iterrows():
                    if (min_price + max_price)/2 < row['Price'] <= max_price:
                        if numberq < 10:
                            urllib.request.urlretrieve(row['Image'], "movie.jpg")
                            image = Image.open("movie.jpg")
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.write(' ')
                            with col2:
                                st.image(image)
                            with col3:
                                st.write(' ')
                            st.markdown(f'**:red[{row["Product"]}]**')
                            col1, col2 = st.columns([0.4, 0.6])
                            with col1:
                                st.markdown(f':green[Price of Product :  ₹ ] **{row["Price"]}** ')
                            with col2:
                                st.markdown(f':green[Rating of the product :] **{row["Stars"]}**')
                            col1, col2 = st.columns([0.4, 0.6])
                            with col1:
                                st.markdown(f':green[Estemated Delivery : ] **{row["Delievery_time"]}** ')
                            try:
                                with col2:
                                    st.markdown(f':green[more info:] **{row["Previous_buyers"]}**')
                            except:
                                with col2:
                                    st.write(' ')
                            st.markdown(f'**:red[Buy Here: ]** {row["link"]}')
                            numberq += 1
        if pil == 'Stars':
            numberq = 0
            for index, row in mf.iterrows():
                if min_stars+0.5 < row['Stars'] <= max_stars:
                    if numberq < 10:
                        urllib.request.urlretrieve(row['Image'], "movie.jpg")
                        image = Image.open("movie.jpg")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.write(' ')
                        with col2:
                            st.image(image)
                        with col3:
                            st.write(' ')
                        st.markdown(f'**:red[{row["Product"]}]**')
                        col1, col2 = st.columns([0.4, 0.6])
                        with col1:
                            st.markdown(f':green[Price of Product :  ₹ ] **{row["Price"]}** ')
                        with col2:
                            st.markdown(f':green[Rating of the product :] **{row["Stars"]}**')
                        col1, col2 = st.columns([0.4, 0.6])
                        with col1:
                            st.markdown(f':green[Estemated Delivery :  ] **{row["Delievery_time"]}** ')
                        try:
                            with col2:
                                st.markdown(f':green[more info:] **{row["Previous_buyers"]}**')
                        except:
                            with col2:
                                st.write(' ')
                        st.markdown(f'**:red[Buy Here: ]** {row["link"]}')
                        numberq += 1

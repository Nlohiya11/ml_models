import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import streamlit as st


def app():
    datainput = st.text_area("Entre your product which you required")

    def data_creating(product):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
        name = []
        price = []
        rating = []
        photo = []
        stars = []
        arrival = []
        last_buy = []
        link = []
        for number in range(0, 8):
            webpage = ""
            string = requests.get(f'https://www.amazon.in/s?k={product}&page={number}&ref=sr_pg_1',
                                  headers=headers).text
            webpage = string + webpage
            soup = BeautifulSoup(webpage, 'html.parser')
            page = soup.find('div', class_='a-section a-spacing-small a-spacing-top-small').text.strip().split(' ')[
                0].split('-')
            total_item = int(page[1]) - int(page[0])
            total_item = int(total_item)
            page_id = soup.find(type="product-ui/weblabs").get('data-version-id')
            if total_item > 20:
                products_2 = soup.find_all('div',
                                           class_=f's-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-{page_id} s-latency-cf-section s-card-border')
                for info in products_2:
                    try:
                        i = info.find('span', class_='a-price-whole').text.strip()
                        lit = i.split(',')
                        if len(lit) == 2:
                            tot = int(lit[0]) * 1000 + int(lit[1])
                        elif len(lit) == 3:
                            tot = int(lit[0]) * 100000 + int(lit[1]) * 1000 + int(lit[2])
                        else:
                            tot = int(lit[0])
                        price.append(tot)
                    except:
                        price.append(np.NaN)
                    try:
                        i = info.find('span', class_='a-size-base s-underline-text').text.strip()
                        lit = i.split(',')
                        if len(lit) == 2:
                            tot = int(lit[0]) * 1000 + int(lit[1])
                        elif len(lit) == 3:
                            tot = int(lit[0]) * 100000 + int(lit[1]) * 1000 + int(lit[2])
                        else:
                            tot = int(lit[0])
                        rating.append(tot)
                    except:
                        rating.append(np.NaN)
                    try:
                        photo.append(info.find('img', class_='s-image').get('src'))
                    except:
                        photo.append(np.nan)
                    try:
                        stars.append(float(info.find('span', class_='a-icon-alt').text.strip().split(' ')[0]))
                    except:
                        stars.append(np.nan)
                    try:
                        i = info.find('span', class_='a-color-base a-text-bold').text.strip()
                        arrival.append(i)
                    except:
                        arrival.append('No Date specified')
                    try:
                        i = info.find('span', class_='a-size-base-plus a-color-base a-text-normal').text.strip()
                        name.append(i)
                    except:
                        name.append(np.nan)
                    try:
                        i = info.find('span', class_='a-size-base a-color-secondary').text.strip()
                        last_buy.append(i)
                    except:
                        last_buy.append(np.nan)
                    try:
                        i = info.find('a',
                                      class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal').get(
                            'href')
                        link.append('https://www.amazon.in' + i)
                    except:
                        link.append(np.nan)
                    len(last_buy)
                dictionary = {'Product': name, 'Stars': stars, 'Rating': rating, 'Image': photo, 'Price': price,
                              'Delievery_time': arrival, 'Previous_buyers': last_buy, 'link': link}

            else:
                products_1 = soup.find_all('div',
                                           class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')
                for info in products_1:
                    try:
                        i = info.find('span', class_='a-price-whole').text.strip()
                        lit = i.split(',')
                        if len(lit) == 2:
                            tot = int(lit[0]) * 1000 + int(lit[1])
                        elif len(lit) == 3:
                            tot = int(lit[0]) * 100000 + int(lit[1]) * 1000 + int(lit[2])
                        else:
                            tot = lit[0]
                        price.append(tot)
                    except:
                        price.append(np.NaN)
                    try:
                        i = info.find('span', class_='a-size-base s-underline-text').text.strip()
                        lit = i.split(',')
                        if len(lit) == 2:
                            tot = int(lit[0]) * 1000 + int(lit[1])
                        elif len(lit) == 3:
                            tot = int(lit[0]) * 100000 + int(lit[1]) * 1000 + int(lit[2])
                        else:
                            tot = int(lit[0])
                        rating.append(tot)
                    except:
                        rating.append(np.NaN)
                    try:
                        photo.append(info.find('img', class_='s-image').get('src'))
                    except:
                        photo.append(np.nan)
                    try:
                        stars.append(float(info.find('span', class_='a-icon-alt').text.strip().split(' ')[0]))
                    except:
                        stars.append(np.nan)
                    try:
                        i = info.find('span', class_='a-color-base a-text-bold').text.strip()
                        arrival.append(i)
                    except:
                        arrival.append('No Date specified')
                    try:
                        i = info.find('span', class_='a-size-medium a-color-base a-text-normal').text.strip()
                        name.append(i)
                    except:
                        name.append('Kalu')
                    try:
                        i = info.find('a',
                                      class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal').get(
                            'href')
                        link.append('https://www.amazon.in' + i)
                    except:
                        link.append(np.nan)
                dictionary = {'Product': name, 'Stars': stars, 'Rating': rating, 'Image': photo, 'Price': price,
                              'Delievery_time': arrival, 'link': link}
        return pd.DataFrame(dictionary)

    tf = pd.DataFrame()

    if st.button('Predict'):
        df = data_creating(datainput)
        tf = pd.concat([tf, df], ignore_index=True, sort=False)
        tf.to_csv('data.csv')

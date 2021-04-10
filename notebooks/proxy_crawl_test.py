import os

import urllib3
import requests
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('proxy_crawl_token')
token = 'u5EA-HLLyCa3vDPm8EpeNg'

phrase = "chicken waffle maker"
url = urllib3.request.urlencode({'https://www.walmart.com/search/?query=':phrase})

url = f'https://api.proxycrawl.com/?token={token}&url=https%3A%2F%2Fwww.walmart.com'
url = 'https://www.walmart.com/search/?query=testing%20search%20query'
response = requests.get(url)
test = response.text
print(test)

response = requests.get(f'https://api.proxycrawl.com/?token={token}&url={url}')

# CHROME DRIVER TEST
# steps to get chromedriver not blocked by mac
# /usr/local/Caskroom/chromedriver
# $ xattr -d com.apple.quarantine chromedriver



import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('/Users/hamilton/1-Repos/walmart_scraper/chromedriver 2')  # Optional argument, if not specified will search path.
driver.get('https://www.walmart.com/')
search_bar = driver.find_element_by_xpath('//*[@id="global-search-input"]')
search_bar.send_keys('chicken waffle machine')
search_bar.send_keys(Keys.ENTER)


titles = driver.find_elements_by_class_name("search-result-product-title")
for title in titles:
    print(title.text)

prices = driver.find_elements_by_class_name('search-result-productprice')

for price in prices:
    print(price.text)

items = driver.find_elements_by_class_name('search-result-gridview-item')

items[0].find_element_by_class_name('search-result-productprice').text.split("$",1)[1]
items[0].find_element_by_class_name('price-characteristic').text
items[0].find_element_by_class_name('price-mantissa').text


for item in items:

    # sponsored data-us-item-id
    try:
        title = item.find_element_by_class_name('product-title-link ').text
        print(title)
    except:
        title = None

    try:
        item_id =

    try:
        # print(item.find_element_by_class_name('search-result-productprice').text.split("$",1)[1])
        dollar = int(item.find_elements_by_class_name('price-characteristic')[0].text)
        cent = int(item.find_elements_by_class_name('price-mantissa')[0].text)/100
        price_low = dollar + cent
        print(price_low)
    except:
        price_low = None

    try:
        dollar = int(item.find_elements_by_class_name('price-characteristic')[1].text)
        cent = int(item.find_elements_by_class_name('price-mantissa')[1].text) / 100
        price_high = dollar + cent
        print(price_high)
    except:
        price_high = None

    try:
        rating = float(item.find_element_by_class_name('seo-avg-rating').text)
        print(rating)

    except:
        rating = None

    try:
        reviews = int(item.find_element_by_class_name('stars-reviews-count').text.replace("\nratings",""))
        print(reviews)
    except:
        reviews = None


    # html = item.get_attribute('innerHTML')
    # soup = BeautifulSoup(html, 'lxml')
    # list_item = soup.find('')

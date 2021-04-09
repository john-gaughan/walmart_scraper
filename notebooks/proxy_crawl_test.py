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

element = driver.find_element_by_id(id_='searchProductResult')
txt = element.get_attribute('innerHTML')
soup = BeautifulSoup(txt, 'lxml')
list_items = soup.find_all('li')
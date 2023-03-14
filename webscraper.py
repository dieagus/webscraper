# Website Scraper!, scrape all images of shoes off of https://www.goat.com/sneakers
# imports 

import requests, json
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#"/Users/dieagus/Downloads/code/images"


# chrome driver


driver = webdriver.Chrome(executable_path=r"/Users/dieagus/Downloads/code/chromedriver")
driver.get("https://www.goat.com/sneakers")


time.sleep(5)
SCROLL_PAUSE_TIME = 5
pairs = []
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
t = 0

while t < 4:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    t += 1


# finds all images and gets their source tag: the source of the image
# initializing the html data

soup = BeautifulSoup(driver.page_source, 'html.parser')


# iterate through sneakers and add name + picture to pair list

final = []
row = ["shoe", "price", "src"]
prices = []
# finds prices 
for price in soup.find_all(attrs={'data-qa': 'grid_cell_product_price','class': 'GridCellProductInfo__Price-sc-17lfnu8-6 gsZMPb'}):
    prices.append(price.text)
    
#finds images and shoe title
for item in soup.find_all('img'):
    pair = [item['alt'], item['src']]
    pairs.append(pair)


#creates list with images shoe title and prices
for i in range(len(prices)-1):
    shoe = [pairs[i][0], prices[i], pairs[i][1]]
    final.append(shoe)

#keeps a csv of data
with open("shoes", 'w') as f:
    write = csv.writer(f)

    write.writerow(row)
    write.writerows(final)
print(final)

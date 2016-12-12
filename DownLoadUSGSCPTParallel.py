from selenium.common.exceptions import NoSuchElementException
from multiprocessing.dummy import Pool as ThreadPool
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import numpy as np
import requests
import selenium
import time
import wget



headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
s = requests.session()

home = 'http://earthquake.usgs.gov/research/cpt/data/table/'
#link = 'http://earthquake.usgs.gov/research/cpt/data/'


browser = webdriver.Chrome('/usr/local/bin/chromedriver') # Get local session of chrome


c = browser.get(home)
time.sleep(30)

txts = browser.find_elements_by_partial_link_text('ASCII')

urls=[]
for index, txt in enumerate(txts):
    link = txt.get_attribute("href")
    if link:
        urls.append(link)

print(urls)



# Make the Pool of workers
pool = ThreadPool()
# Open the urls in their own threads
# and return the results
results = pool.map(wget.download, urls)
#close the pool and wait for the work to finish
pool.close()
pool.join()


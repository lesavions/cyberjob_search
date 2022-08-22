# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 22:17:36 2022

@author: marti
"""

#SEARCH RECENTLY POSTED, REMOTE ONLY, MID-SENIOR LEVEL PENETRATION TESTER ROLES IN IRELAND

#Below enter path for saving screenshot if required
save_path = 'PATH/cyberjob_new.png'

from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('C:/Users/marti/chromedriver.exe')

url = 'https://ie.linkedin.com/jobs/search?keywords=Penetration%20Tester&location=Ireland&locationId=&geoId=104738515&f_TPR=r604800&f_E=3%2C4&f_WT=2&position=1&pageNum=0'

driver.get(url)
time.sleep(1)

#agrees all cookies
button = driver.find_element('xpath','//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[1]').click()
time.sleep(1)

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
soup

#finds recently posted jobs
postings = soup.find_all('div', class_= 'base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card job-search-card--active')
jobs = []
while True:
    for post in postings:
        jobs.append(post.text)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_= 'base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card job-search-card--active')
    jobs = list(set(jobs))
    if len(jobs) > 20:
        break
    
driver.save_screenshot(save_path)





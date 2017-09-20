# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:42:42 2017

@author: Desmonduz
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


username="your_username"
pwd="your_pwd"

driver=webdriver.Chrome()
driver.get("http://www.reddit.com")

elem = driver.find_element_by_name("user")
elem.clear()
elem.send_keys(username)

elem = driver.find_element_by_name("passwd")
elem.clear()
elem.send_keys(pwd)
elem.submit()
results=[]

def collect_results():
    links=[]
    elems = driver.find_elements_by_css_selector("div.entry")
    for elem in elems:
        print elem.text
        
        link={}
        try:        
            link["title"]=elem.find_element_by_css_selector("a.title").text
            link["url"]=elem.find_element_by_css_selector("a.title").get_attribute('href')
            link["sub"]=elem.find_element_by_css_selector("a.subreddit").text
            link["date"]=elem.find_element_by_css_selector("time").get_attribute('datetime')
        except:
            link["title"]=elem.find_element_by_css_selector("form.usertext").text
            link["url"]=elem.find_element_by_link_text("permalink").get_attribute('href')
            link["sub"]="user comment"
            link["date"]=elem.find_element_by_css_selector("time").get_attribute('datetime')
        
        links.append(link)
    return links


try:
    elem=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "logout"))
    )
    driver.get("https://www.reddit.com/user/%s/saved" % username)
        
    links = collect_results()
    while links:
        results+=links
        elem=driver.find_element_by_link_text('next ›')
        elem.click()
        links=collect_results()
finally:
    driver.close()
    if results:
        with open('saved_links.json', 'w') as f:
            json.dump(results, f)
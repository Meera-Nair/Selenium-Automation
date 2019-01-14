# Open facebook and login using Selenium Python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.facebook.com')

user = ""
pwd = ""

assert 'Facebook' in browser.title

elem = browser.find_element_by_id("email")
elem.send_keys(user)

elem2 = browser.find_element_by_id("pass")
elem2.send_keys(pwd + Keys.RETURN)
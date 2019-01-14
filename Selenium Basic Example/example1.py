#Example 0:
#    open a new Firefox browser
#    load the page at the given URL



from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://seleniumhq.org/')

from  selenium import webdriver
import chromedriver_binary      # => pip install chromedriver-binary-auto

# # open google chrome
# browser = webdriver.Chrome()

# # identify the page that i need go to
# browser.get('https://www.google.com/?gws_rd=ssl')

#=======================================================================================
#==============    deal with firefox       ===========
# import geckodriver_autoinstaller
# pip install geckodriver-autoinstaller

# browser = webdriver.Firefox()
# browser.get('https://www.google.com/?gws_rd=s


# extract data using selenium

# browser = webdriver.Chrome()
# browser.get('https://en.wikipedia.org/wiki/Main_Page')

# use "by" object

from selenium.webdriver.common.by import By

# define = browser.find_element(By.CSS_SELECTOR ,'#mp-right')   
"""By.CSS_SELECTOR  =>this is identifier to obtian data by css"""

# print(define.text)

# use elements 
# define = browser.find_elements(By.TAG_NAME ,'p')   
# print(len(define))



#==================================================================================
import time   #=>use to make the clothing of page late
browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/Main_Page')

# clik ()
# element = browser.find_element(By.CSS_SELECTOR ,'#ca-talk')
# element.click()
# time.sleep(5)

# write and searsh in the web

# element = browser.find_element(By.CSS_SELECTOR ,'#searchInput')
# element.send_keys('python')
# time.sleep(3)
# element = browser.find_element(By.CSS_SELECTOR ,'#searchButton')
# element.click()
# time.sleep(5)

# control up and down 
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/Main_Page')

# determine whole html page
html = browser.find_element(By.TAG_NAME , 'html')
html.send_keys(Keys.END)                            # =>to go down
time.sleep(5)
html.send_keys(Keys.HOME)                           #  => to return to first place 
time.sleep(5)
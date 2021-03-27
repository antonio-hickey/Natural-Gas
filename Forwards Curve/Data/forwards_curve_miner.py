#--------------------------------------------------------------------------------------------------------
# Importing Python Modules
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import os
import time
import pandas as pd
#--------------------------------------------------------------------------------------------------------
# Browser Path
PATH = "/home/sratus/Desktop/API/chromedriver"
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
prefs = {'download.default_directory' : "/home/sratus/QG Terminal/QG-Terminal/apps/data/"}
options.add_experimental_option('prefs',prefs)
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
#--------------------------------------------------------------------------------------------------------
# Request Page
driver.get('https://finance.yahoo.com/quote/NG%3DF/futures?p=NG%3DF')
time.sleep(3) # wait 3 seconds

# Define Target Data
front_price = driver.find_element_by_css_selector("tr.BdT:nth-child(1) > td:nth-child(3) > span:nth-child(1)")
front_date =  driver.find_element_by_css_selector("tr.BdT:nth-child(1) > td:nth-child(1) > a:nth-child(1)")
prices = []
dates = []
for element in range(2,50):
    prices.append(driver.find_element_by_css_selector("tr.Ta\(end\):nth-child({}) > td:nth-child(3) > span:nth-child(1)".format(element)).text)
for element in range(2,50):
    dates.append(driver.find_element_by_css_selector("tr.Ta\(end\):nth-child({}) > td:nth-child(1) > a:nth-child(1)".format(element)).text)
dates.insert(0,front_date.text)
dates_ = []
for date in dates:
    dates_.append(date[2:5])
prices.insert(0,float(front_price.text))

# Change contract code to month (ex. J21 -> April 21)
_date_ = []
for date in dates_:
    if date[0] == 'F':
        _date_.append("Jan {}".format(date[-2:]))
    if date[0] == 'G':
        _date_.append("Feb {}".format(date[-2:]))
    if date[0] == 'H':
        _date_.append("Mar {}".format(date[-2:]))
    if date[0] == 'J':
        _date_.append("Apr {}".format(date[-2:]))
    if date[0] == 'K':
        _date_.append("May {}".format(date[-2:]))
    if date[0] == 'M':
        _date_.append("Jun {}".format(date[-2:]))
    if date[0] == 'N':
        _date_.append("Jul {}".format(date[-2:]))
    if date[0] == 'Q':
        _date_.append("Aug {}".format(date[-2:]))
    if date[0] == 'U':
        _date_.append("Sep {}".format(date[-2:]))
    if date[0] == 'V':
        _date_.append("Oct {}".format(date[-2:]))
    if date[0] == 'X':
        _date_.append("Nov {}".format(date[-2:]))
    if date[0] == 'Z':
        _date_.append("Dec {}".format(date[-2:]))
    
df = pd.DataFrame({
    'Date': _date_,
    'Price': prices
})
print(df)

# Export to csv
filename="forwards_curve.csv"
columns = ["Date","Price"]
with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(columns)
    for val in range(len(_date_)):
        csvwriter.writerow([_date_[val],prices[val]])

#--------------------------------------------------------------------------------------------------------
# Quit driver
driver.quit()
#--------------------------------------------------------------------------------------------------------
import unittest

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://127.0.0.1:8000/')
print ('Proba' in driver.title)

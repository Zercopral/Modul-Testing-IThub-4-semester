from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome = webdriver.Chrome()

chrome.get("https://ya.ru")

search_input = chrome.find_element(By.CSS_SELECTOR, value="#text")

search_input.send_keys("hello\n")

chrome.quit()

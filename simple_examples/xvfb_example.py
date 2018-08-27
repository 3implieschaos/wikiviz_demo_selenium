#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(1000, 1000))
display.start()

browser = webdriver.Firefox()
browser.get('http://localhost:8080/')
assert browser.title == 'WikiViz'
browser.quit()

display.stop()
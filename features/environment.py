from selenium import webdriver
from browser import BDisplay
from browser import Browser
from pages.home_page import HomePage


def before_all(context):
    context.display = BDisplay() # Comment this out for live browser
    context.browser = Browser()
    context.home_page = HomePage()
    

def after_all(context):
    context.browser.close()
    context.display.stop()  # Comment this out for live browser
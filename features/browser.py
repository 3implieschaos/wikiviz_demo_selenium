from selenium import webdriver
from pyvirtualdisplay import Display  # Comment this out for live browser


class BDisplay(object): # Comment this out for live browser
    display = Display(visible=0, size=(1000, 1000))  # Comment this out for live browser
    display.start()  # Comment this out for live browser

    def stop(context): # Comment this out for live browser
        context.display.stop() # Comment this out for live browser
        
        
class Browser(object):

    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()

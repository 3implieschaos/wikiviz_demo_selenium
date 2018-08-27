from selenium.webdriver.common.by import By
from browser import Browser


class HomePage(Browser):
    # Home Page Actions

    def navigate(self, address):
        self.driver.get(address)
        
    def get_page_title(self):
        return self.driver.title
        
    def get_page_header(self):
        return self.driver.find_element_by_class_name("example").text
 
    def click_button(self, *locator):
        self.driver.find_element_by_class_name("button").click()
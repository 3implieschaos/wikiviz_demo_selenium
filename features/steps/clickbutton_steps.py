from nose.tools import assert_equal, assert_not_equal, assert_true
from selenium.webdriver.common.by import By

@given('I navigate to the Home page')
def step_impl(context):
    context.home_page.navigate("http://localhost:8080/")

@given('I see that the pagename is WikiViz')
def step_impl(context):
    assert_equal(context.home_page.get_page_title(), "WikiViz")
    
@given('I see the header "Hello World!"')
def step_impl(context):
    assert_equal(context.home_page.get_page_header(), "Hello World!")

@when('I click the button')
def step_impl(context):
    context.home_page.click_button()

@then('I see that the pagename is no longer WikiViz')
def step_impl(context):
    assert_not_equal(context.home_page.get_page_title(), "WikiViz")
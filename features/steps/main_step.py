from behave import *
from features.pages import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

@given(u'I at flocabulary home page')
def step_impl(context):

    main = MainPage(context)
    context.browser.get(main.base_url)

    assert(context.browser.title) == 'Flocabulary App'
    context.browser.find_element_by_id(main.id_password).send_keys('12341234')
    context.browser.find_element_by_xpath(main.preview_btn).click()

    # Validate if the properly logged to the apps
    assert(context.browser.title) == 'Educational Hip-Hop Songs & Videos for All Subjects, K-12'


@when(u'I login using correct email and password')
def step_impl(context):
    main = MainPage(context)
    login = LoginPage()
    context.browser.find_element_by_xpath(main.login_link).click()
    context.browser.find_element_by_name(login.username_field).send_keys(login.email)
    context.browser.find_element_by_name(login.password_field).send_keys(login.pswd)
    context.browser.find_element_by_xpath(login.login_btn).click()
    time.sleep(1)

@then(u'I should logged in to Flocabulary')
def step_impl(context):
    main = MainPage(context)
    assert(context.browser.find_element_by_css_selector(main.logged_user).text) == 'Budi'


# reuseable step from previous line
@given(u'I existing and logged user')
def step_impl(context):
    context.execute_steps(u"""
        given I at flocabulary home page
        when I login using correct email and password
    """)

@when(u'I request quote for my school')
def step_impl(context):
    main = MainPage(context)
    context.browser.get(main.base_url + '/plans')

    context.browser.find_element_by_css_selector(main.request_quote).click()
    select_state = Select(context.browser.find_element_by_name('shipping_state'))
    select_state.select_by_value('NY')
    time.sleep(1)
    context.browser.find_element_by_css_selector('.Select-placeholder').click()
    ActionChains(context.browser).send_keys('ps 306').perform()
    time.sleep(1)
    ActionChains(context.browser).send_keys(Keys.TAB, Keys.ENTER).perform()
    context.browser.find_element_by_css_selector('.signup__button').click()
    time.sleep(3)

@then(u'I should get request quote')
def step_impl(context):
    main = MainPage(context)
    assert(context.browser.find_element_by_css_selector(main.quote_msg).text) == 'Your custom quote is all set!'
    assert(context.browser.find_element_by_css_selector(main.quote_download_btn))

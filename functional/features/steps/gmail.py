'''
Feature: Login test

  @browser
  Scenario: Check Mail
    Given I am on "/"
      And I click Mail
      And I click Sign In
    When I log into google using as "Admin"
      And I wait for the page to load
    Then I am on inbox page

'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from hamcrest import assert_that, contains_string, equal_to
import time


# Locator Map
MAIL_LINK_LOCATOR = (By.XPATH, '//div/a[contains(text(),"Gmail")]')
SIGN_IN_LINK_LOCATOR = (By.CSS_SELECTOR, 'a.gmail-nav__nav-link__sign-in')
ACCOUNT_ICON_LOCATOR = (By.XPATH, '//a[starts-with(@title,"Google Account:")]')

@given('I click Mail')
def click_mail(context):
    el = context.driver.find_element(*MAIL_LINK_LOCATOR)
    el.click()


@given('I click Sign In')
def click_mail(context):
    el = context.driver.find_element(*SIGN_IN_LINK_LOCATOR)
    el.click()

@when('I wait for the page to load')
def click_mail(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(EC.visibility_of_element_located(ACCOUNT_ICON_LOCATOR))

@then('I am on inbox page')
def check_inbox_url(context):
    current_url = context.driver.current_url
    print(current_url)
    assert 'https://mail.google.com' in current_url, 'Did not end up in Inbox'
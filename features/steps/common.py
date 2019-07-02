from behave import *
from features.steps.pom.element_locators import continue_btn_xpath
from features.steps.pom.common_function import open_url, find_by_xpath_and_click
from nose.tools import assert_equals


@given('I visit url "{url}"')
def step_impl(context, url):
    open_url(context, url)


@then('title should be "{title}"')
def step_impl(context, title):
    assert_equals(title, context.driver.title)


@when('I click on Continue button')
def step_impl(context):
    find_by_xpath_and_click(context, continue_btn_xpath)

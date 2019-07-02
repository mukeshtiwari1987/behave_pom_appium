from behave import *
from features.steps.pom.element_locators import login_btn_id, incorrect_creds_msg_xpath
from features.steps.pom.common_function import wait, find_by_id_and_click, find_text_from_xpath_and_assert_text


@when('I click Login button')
def step_impl(context):
    find_by_id_and_click(context, login_btn_id)
    wait(2)


@then('I should see error "{error}"')
def step_impl(context, error):
    find_text_from_xpath_and_assert_text(context, incorrect_creds_msg_xpath, error)

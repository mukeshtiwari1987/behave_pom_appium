from behave import *
from nose.tools import assert_equals

from features.steps.pom.common_function import (
    find_by_id_and_click, find_by_xpath_and_click, find_by_xpath_and_send_keys,
    find_text_from_id_and_assert_text, find_text_from_xpath_and_assert_text,
    wait)
from features.steps.pom.element_locators import (checkmark_radio_xpath,
                                                 email_btn_xpath,
                                                 email_form_xpath,
                                                 email_input_xpath,
                                                 error_msg_xpath,
                                                 hamburger_icon_xpath,
                                                 login_btn_xpath, msg_id,
                                                 password_input_xpath,
                                                 signup_btn_xpath,
                                                 submit_btn_id, x_icon_xpath)


@when('I click Hamburger Icon')
def step_impl(context):
    find_by_xpath_and_click(context, hamburger_icon_xpath)
    wait(2)


@then('"{login}" button exists')
def step_impl(context, login):
    find_text_from_xpath_and_assert_text(context, login_btn_xpath, login)


@then('"{signup}" button should exists')
def step_impl(context, signup):
    find_text_from_xpath_and_assert_text(context, signup_btn_xpath, signup)


@when('I click on X icon')
def step_impl(context):
    find_by_xpath_and_click(context, x_icon_xpath)
    wait(2)


@then('"{continue_email}" button should also exists')
def step_impl(context, continue_email):
    email_btn_text = context.driver.find_element_by_xpath(email_btn_xpath).get_attribute('value')
    assert_equals(continue_email, email_btn_text)

    find_by_xpath_and_click(context, email_btn_xpath)
    wait(3)


@when('I click Continue With Email button')
def step_impl(context):
    wait(3)
    find_by_xpath_and_click(context, email_btn_xpath)


@when('I enter "{email}" in email placeholder')
def step_impl(context, email):
    find_by_xpath_and_send_keys(context, email_form_xpath, email)


@then('I should see "{error}" message')
def step_impl(context, error):
    find_text_from_xpath_and_assert_text(context, error_msg_xpath, error)


@when('I enter "{email}" in email address form')
def step_impl(context, email):
    find_by_xpath_and_send_keys(context, email_input_xpath, email)


@when('I enter "{password}" in password form')
def step_impl(context, password):
    find_by_xpath_and_send_keys(context, password_input_xpath, password)


@when('I click Terms of Use')
def step_impl(context):
    find_by_xpath_and_click(context, checkmark_radio_xpath)


@when('I click Submit button')
def step_impl(context):
    find_by_id_and_click(context, submit_btn_id)
    wait(2)


@then('I should see "{message}" error')
def step_impl(context, message):
    find_text_from_id_and_assert_text(context, msg_id, message)

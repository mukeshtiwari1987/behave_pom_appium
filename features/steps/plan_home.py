from behave import *
from selenium.webdriver.support.select import Select

from features.steps.pom.element_locators import title_icon_xpath, homestate_input_id,\
homecity_input_id, city_dropdown_xpath, zipcode_input_id, date_input_xpath, excellent_button_xpath,\
upfrontamount_input_xpath, monthlyspend_input_xpath, getmyplan_input_xpath, new_plan_xpath, zip_code_error_xpath,\
date_error_xpath, upfront_payment_xpath, month_payment_xpath

from features.steps.pom.common_function import wait, find_by_xpath_and_click, find_text_from_xpath_and_assert_text,\
find_by_id_and_send_keys, find_by_xpath_and_send_keys


@then('I should see "{plan_home_icon_text}"')
def step_impl(context, plan_home_icon_text):
    find_text_from_xpath_and_assert_text(context, title_icon_xpath, plan_home_icon_text)


@when('I click Select "New York" state')
def step_impl(context):
    select = Select(context.driver.find_element_by_id(homestate_input_id))
    select.select_by_value('NY')
    wait(3)


@when('I type "{city}" in city')
def step_impl(context, city):
    find_by_id_and_send_keys(context, homecity_input_id, city)
    wait(5)
    find_by_xpath_and_click(context, city_dropdown_xpath)


@when('I type "{zip}" in Zip code')
def step_impl(context, zip):
    find_by_id_and_send_keys(context, zipcode_input_id, zip)


@when('I type "{date}" in future date')
def step_impl(context, date):
    find_by_xpath_and_send_keys(context, date_input_xpath, date)


@when('I click "Excellent: 750+"')
def step_impl(context):
    find_by_xpath_and_click(context, excellent_button_xpath)


@when('I click in Upfront Amount')
def step_impl(context):
    find_by_xpath_and_click(context, upfrontamount_input_xpath)
    wait(2)


@when('I type "{upfront_amount}"')
def step_impl(context, upfront_amount):
    find_by_xpath_and_send_keys(context, upfrontamount_input_xpath, upfront_amount)
    wait(2)


@when('I click in Monthly spending')
def step_impl(context):
    find_by_xpath_and_click(context, monthlyspend_input_xpath)


@when('I type in "{monthlyspend_amount}"')
def step_impl(context, monthlyspend_amount):
    find_by_xpath_and_send_keys(context, monthlyspend_input_xpath, monthlyspend_amount)


@when('I click Get My Plan')
def step_impl(context):
    find_by_xpath_and_click(context, getmyplan_input_xpath)


@then('I should see "{new_plan}" page')
def step_impl(context, new_plan):
    find_text_from_xpath_and_assert_text(context, new_plan_xpath, new_plan)


@then('I should see "{message}" in zipcode')
def step_impl(context, message):
    find_text_from_xpath_and_assert_text(context, zip_code_error_xpath, message)


@then('I should see "{message}" in date')
def step_impl(context, message):
    find_text_from_xpath_and_assert_text(context, date_error_xpath, message)


@then('I should see "{message}" in upfront amount')
def step_impl(context, message):
    find_text_from_xpath_and_assert_text(context, upfront_payment_xpath, message)


@then('I should see "{message}" in monthly spending')
def step_impl(context, message):
    find_text_from_xpath_and_assert_text(context, month_payment_xpath, message)

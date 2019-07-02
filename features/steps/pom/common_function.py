from nose.tools import assert_equals
import time


def wait(seconds):
    time.sleep(seconds)


def open_url(context, url):
    context.driver.get(url)


def find_by_id_and_click(context, element_id):
    context.driver.find_element_by_id(element_id).click()


def find_by_xpath_and_click(context, element_xpath):
    context.driver.find_element_by_xpath(element_xpath).click()


def find_text_from_xpath_and_assert_text(context, element_xpath, element_message):
    element_message_text = context.driver.find_element_by_xpath(element_xpath).text
    assert_equals(element_message, element_message_text)


def find_text_from_id_and_assert_text(context, element_xpath, element_message):
    element_message_text = context.driver.find_element_by_id(element_xpath).text
    assert_equals(element_message, element_message_text)


def find_by_id_and_send_keys(context, element_id, value):
    context.driver.find_element_by_id(element_id).send_keys(value)


def find_by_xpath_and_send_keys(context, element_xpath, value):
    context.driver.find_element_by_xpath(element_xpath).send_keys(value)

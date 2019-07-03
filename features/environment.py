import json
import os

from selenium import webdriver

LOCAL_APPIUM_HUB = "http://127.0.0.1:4723/wd/hub"

CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'config/android.json'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

with open(CONFIG_FILE) as data_file:
    CONFIG = json.load(data_file)


def before_feature(context, scenario):

    if CONFIG_FILE == "config/android.json":
        desired_capabilities = CONFIG['environments'][TASK_ID]
        for key in CONFIG["capabilities"]:
            if key not in desired_capabilities:
                desired_capabilities[key] = CONFIG["capabilities"][key]

        context.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor=LOCAL_APPIUM_HUB
        )
    elif CONFIG_FILE == "config/ios.json":
        desired_capabilities = CONFIG['environments'][TASK_ID]
        for key in CONFIG["capabilities"]:
            if key not in desired_capabilities:
                desired_capabilities[key] = CONFIG["capabilities"][key]

        context.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor=LOCAL_APPIUM_HUB
        )
    elif CONFIG_FILE == "config/browserstack.json":
        BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['user']
        BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['key']

        desired_capabilities = CONFIG['environments'][TASK_ID]

        for key in CONFIG["capabilities"]:
            if key not in desired_capabilities:
                desired_capabilities[key] = CONFIG["capabilities"][key]

        context.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://{}:{}@hub-use.browserstack.com/wd/hub".format(BROWSERSTACK_USERNAME,
                                                                                   BROWSERSTACK_ACCESS_KEY)
        )


def after_feature(context, scenario):
    context.driver.quit()

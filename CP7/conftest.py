import datetime
import time

import pytest
import logging
import allure
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="firefox", choices=["chrome", "firefox"]
    )
    parser.addoption(
        "--headless", action='store_true'
    )
    parser.addoption(
        "--base_url", default='http:/localhost'
    )
    parser.addoption(
        "--log_level", action="store", default="INFO"
    )
    parser.addoption(
        "--executor", action="store", default="localhost"
    )

# @pytest.fixture()
# def base_url(request):
#     return request.config.getoption("--base_url")

@pytest.fixture()
def driver(request):
    executor = request.config.getoption("--executor")
    base_url = "https://demo-opencart.ru/index.php"
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info(
        "===> Test %s started at %s" % (request.node.name, datetime.datetime.now())
    )

    executor_url = f"http://{executor}:4444/wd/hub"
    # service = Service()

    if browser_name == "chrome":
        options = Options()
        if headless:
            options.add_argument("headless=new")
        # browser = webdriver.Chrome(service=service, options=options)
        options = Options()
        options.headless = headless
    elif browser_name == "firefox":
        options = FirefoxOptions()
        # browser = webdriver.Firefox(service=service, options=options)
        options.headless = headless
    else:
        raise NotImplemented()
    # options.add_argument(f'{"selenoid:options"}': {"enableVideo": True})
    options.set_capability('selenoid:options', {'enableVideo': True})

    browser = webdriver.Remote(command_executor=executor_url, options=options)
    allure.attach(
        name=browser.session_id,
        body=json.dumps(browser.capabilities),
        attachment_type=allure.attachment_type.JSON,
    )

    browser.log_level = log_level
    browser.logger = logger
    browser.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    browser.maximize_window()
    browser.get(base_url)

    def fin():
        browser.quit()
        logger.info(
            "===> Test %s finished at %s" % (request.node.name, datetime.datetime.now())
        )

    request.addfinalizer(fin)
    return browser
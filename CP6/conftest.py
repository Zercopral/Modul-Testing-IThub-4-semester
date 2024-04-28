import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture()
def driver(request):
    
    capabilities = {
        "platformName":'Android',
        "appium:options": {
            "deviceName":"Test Pixel 7 Pro API TiramisuPrivacySandbox",
            "automationName":'uiautomator2',
            "appPackage":'com.google.android.calculator',
            "noReset": True,
            # "forceAppLaunch": True
        }
    }

    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
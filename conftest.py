import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utils.config_reader import read_config


@pytest.fixture(scope="session")
def config():
    return read_config()


@pytest.fixture(scope="function")
def driver(config):
    browser = config.get('basic_info', 'browser')
    headless = config.getboolean('basic_info', 'headless')

    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(5)
        driver.maximize_window()
    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(5)
        driver.maximize_window()
    elif browser.lower() == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
        driver.implicitly_wait(5)
        driver.maximize_window()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()

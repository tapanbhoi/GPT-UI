import logging
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging at the top level of the test suite
@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger()
    logger.info("Logging is configured!")
    return logger

@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

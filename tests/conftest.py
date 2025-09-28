import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="session")
def driver():
    """
    Pytest fixture to set up and tear down the Chrome WebDriver session.
    Uses webdriver_manager to handle the driver executable automatically.
    """
    # Setup: Initialize the Chrome driver using WebDriverManager
    print("\nSetting up Chrome Driver...")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10) # Good practice to avoid simple failures

    # The 'yield' keyword passes the driver instance to the test functions
    yield driver

    # Teardown: Quit the browser after all tests in the session are complete
    print("\nQuitting Chrome Driver...")
    driver.quit()

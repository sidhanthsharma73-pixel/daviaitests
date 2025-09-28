import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# The base URL for the web application
BASE_URL = "https://www.iamdave.ai"

# -----------------------------------------------------------
# Test 1: Verify that the website loads and title/logo are correct
# -----------------------------------------------------------
def test_homepage_load_and_title(driver):
    """Verifies the homepage loads successfully and has the correct title."""
    driver.get(BASE_URL)
    
    # 1. Verification of the Page Title (SEO/Correct Page Check)
    expected_title = "Dave.AI - Enterprise AI assistant for sales and CX"
    assert driver.title == expected_title, f"Expected title: '{expected_title}', but got: '{driver.title}'"

    # 2. Verification of the Logo presence (Critical Element Check)
    # Using a robust CSS Selector for the logo
    logo_locator = (By.CSS_SELECTOR, "img[alt='Dave.AI']")
    
    # Use Explicit Wait to ensure the element is loaded (Robustness!)
    logo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(logo_locator)
    )
    assert logo.is_displayed(), "Dave.AI Logo is not displayed on the homepage"


# -----------------------------------------------------------
# Test 2: Test a navigation flow (Click 'Contact Us' and verify the page URL)
# -----------------------------------------------------------
def test_navigation_to_contact_us(driver):
    """Tests navigation from the homepage to the 'Contact Us' page."""
    driver.get(BASE_URL)
    
    # Locate the 'Contact Us' button/link - using an XPATH as a flexible alternative
    contact_link_locator = (By.XPATH, "//a[contains(text(), 'Contact Us')]")
    contact_link = driver.find_element(*contact_link_locator)
    
    # Click the link
    contact_link.click()

    # Verification: Check if the URL has changed to the expected Contact Us URL
    expected_url_part = "/contact"
    # Use Explicit Wait for the URL change
    WebDriverWait(driver, 10).until(
        EC.url_contains(expected_url_part)
    )
    
    assert expected_url_part in driver.current_url, (
        f"URL did not navigate to the expected '{expected_url_part}'. Current URL: {driver.current_url}"
    )


# -----------------------------------------------------------
# Test 3: Check for the presence of a specific element (a key heading/feature button)
# -----------------------------------------------------------
def test_presence_of_key_heading(driver):
    """Verifies that a key feature heading on the homepage is present."""
    driver.get(BASE_URL)

    # Locate the heading "The Enterprise AI Assistant for Sales and CX"
    # Using By.TAG_NAME combined with By.TEXT is less brittle than position-based XPATH
    heading_locator = (By.XPATH, "//h1[contains(text(), 'The Enterprise AI Assistant')]")

    heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(heading_locator)
    )

    assert heading.is_displayed(), "The main feature heading is not visible on the homepage."
    
    
# -----------------------------------------------------------
# Test 4 (BONUS): Test a simple input interaction (Search or Newsletter if available)
# Since a form is not immediately obvious, we'll simulate text input on the 'Contact Us' form.
# -----------------------------------------------------------
def test_contact_form_input_interaction(driver):
    """Tests if the name field on the Contact Us page can be interacted with."""
    
    # First, navigate to the contact page (as tested in test 2)
    driver.get(BASE_URL + "/contact")
    
    # Locate the Name input field (assuming it has a unique 'name' attribute or label)
    # Inspect the page source for the actual locator. Let's assume an ID for 'name' is present.
    # In a real test, you must check the element's attribute!
    name_field_locator = (By.NAME, "name") 
    
    name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(name_field_locator)
    )
    
    test_name = "Test User"
    name_field.send_keys(test_name)
    
    # Verification: Check that the value entered is actually present in the input field
    # We use .get_attribute("value") to retrieve the text in an input field
    actual_value = name_field.get_attribute("value")
    
    assert actual_value == test_name, f"Input field value was not set correctly. Expected: {test_name}, Got: {actual_value}"

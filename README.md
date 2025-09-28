# daviaitests
This is a repository that contains the test for ui automation scripts and api scripts

how to run the test scripts:

### 1. Prerequisites

You must have **Python 3.x** installed. The **Chrome browser** must be installed on your system for the UI tests to execute successfully.

### 2. Setup (Installation)

1.  **Clone the repository/Unzip the folder.**
2.  **Create and activate a Python Virtual Environment** (recommended practice):
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate   # Windows
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Test Execution

All tests are designed to be run using the `pytest` command from the root directory.

| Test Group | Command | Description |
| :--- | :--- | :--- |
| **All Tests** | `pytest` | Runs both API and UI tests. |
| **API Tests Only** | `pytest tests/test_api.py` | Runs only the tests interacting with Reqres API. |
| **UI Tests Only** | `pytest tests/test_ui.py` | Runs only the Selenium UI tests for iamdave.ai. |

## Test Design Choices & Rationale

### General Automation Principles

* **PyTest Framework:** Used for structured testing, providing clear reporting, test discovery, and the use of powerful **fixtures** for setup and teardown.
* **Decoupled Setup:** The Selenium WebDriver setup and teardown logic is placed in `conftest.py` using a session-scoped fixture (`@pytest.fixture(scope="session")`). This ensures the browser opens once for all UI tests and closes once they are all finished, saving execution time.
* **Selenium Manager:** Used (via `webdriver-manager` in `conftest.py`) to automatically manage the Chrome driver version, ensuring the tests are stable and not dependent on manual driver updates.

### Part 1: API Testing (`test_api.py`)

* **Tooling:** Used the dedicated `requests` library for clean, idiomatic Python HTTP calls.
* **Test Cases:** Focused on the **three key scenarios** requested: **Success** (status code 200/201), **Content Validation** (checking `data` key and specific `email` value), and **Error Handling** (checking status code 404 for non-existent resource).
* **Clarity:** Assertions are accompanied by meaningful error messages (e.g., `f"Expected Status Code 200, but got..."`) to aid in debugging.

### Part 2: Website Testing (`test_ui.py`)

* **Locator Strategy:** A mix of **robust locators** was used (`By.CSS_SELECTOR`, `By.XPATH`, `By.NAME`) avoiding reliance on fragile, position-based XPATH.
* **Stability (Waits):** **Explicit Waits** (`WebDriverWait` and `EC.presence_of_element_located` / `EC.visibility_of_element_located`) are used to ensure elements are ready before interaction, eliminating common timing-related test failures.
* **Usefulness:** Tests focused on high-impact scenarios: page load (title/logo), critical navigation flow (`Contact Us`), and basic user interaction validation (input field value check).

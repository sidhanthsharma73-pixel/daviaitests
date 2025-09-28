import pytest
import requests

# Base URL for the Reqres API
BASE_URL = "https://reqres.in/api"
# 1. Validate a successful response (status code 200) and content
def test_get_list_users_successful():
   
    endpoint = f"{BASE_URL}/users?page=2"
    response = requests.get(endpoint)

    # Assertion 1: Check for successful status code
    assert response.status_code == 200, f"Expected Status Code 200, but got {response.status_code}"

    # Convert the JSON response body to a Python dictionary
    data = response.json()

    # Assertion 2: Check if the required key 'data' exists in the response
    assert 'data' in data, "Response body missing the 'data' key"

    # Assertion 3: Check if the 'data' key is a list (contains user records)
    assert isinstance(data['data'], list), "The value of 'data' is not a list"

# 2. Validate response content (specific value is correct)
def test_get_single_user_content_validation():
    
    user_id = 2
    endpoint = f"{BASE_URL}/users/{user_id}"
    response = requests.get(endpoint)
    data = response.json()

    # Assertion 1: Check for successful status code
    assert response.status_code == 200, f"Expected Status Code 200, but got {response.status_code}"

    # Assertion 2: Validate a specific value in the response
    expected_email = "janet.weaver@reqres.in"
    actual_email = data['data']['email']

    assert actual_email == expected_email, (
        f"Expected email '{expected_email}', but found '{actual_email}'"
    )



# 3. Validate error handling (missing or invalid parameters)

def test_get_single_user_not_found():
    """
    Tests error handling for a non-existent user.
    Validates status code (404) for a user ID that doesn't exist.
    Endpoint: GET /api/users/23
    """
    non_existent_id = 23
    endpoint = f"{BASE_URL}/users/{non_existent_id}"
    response = requests.get(endpoint)

    # Assertion 1: Check for 'Not Found' status code
    assert response.status_code == 404, f"Expected Status Code 404 for not found, but got {response.status_code}"

    # Assertion 2: Check that the response body is empty or minimally informative (Reqres returns an empty object)
    assert response.json() == {}, "Response body was not empty for a 404 Not Found error"


# A bonus test to demonstrate POST request and payload validation
def test_create_user_successful():
    """
    Tests creating a new user (POST request).
    Validates successful status code (201) and checks for required keys in the response.
    Endpoint: POST /api/users
    """
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    endpoint = f"{BASE_URL}/users"
    response = requests.post(endpoint, json=payload)
    data = response.json()

    # Assertion 1: Check for successful creation status code
    assert response.status_code == 201, f"Expected Status Code 201, but got {response.status_code}"

    # Assertion 2: Check that the response contains the data sent, plus an ID and created time.
    assert data['name'] == payload['name']
    assert data['job'] == payload['job']
    assert 'id' in data
    assert 'createdAt' in data

import requests
from behave import when, then

@when('I send a GET request to "{endpoint}"')
def step_impl_get(context, endpoint):
    base_url = "https://restful-booker.herokuapp.com"
    url = f"{base_url}{endpoint}"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    print(f"\nSending GET request to: {url}")
    try:
        context.response = requests.get(url, headers=headers, allow_redirects=False)
        print(f"Response status code: {context.response.status_code}")
        print("Response headers:", context.response.headers)
        print("Response body:", context.response.text[:500])  # Print first 500 chars of response
    except Exception as e:
        print(f"Error making request: {str(e)}")
        raise e

@then('the response status code should be {status_code:d}')
def step_impl_status(context, status_code):
    print("Actual status code:", context.response.status_code)
    print("Response body:", context.response.text)
    assert context.response.status_code == status_code

@then('the response should contain "{text}"')
def step_impl_body(context, text):
    assert text in context.response.text

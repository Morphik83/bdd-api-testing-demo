import requests
from behave import when, then

@when('I send a GET request to "{endpoint}"')
def step_impl_get(context, endpoint):
    base_url = "https://automationintesting.online"
    url = f"{base_url}{endpoint}"
    headers = {
        'Accept': 'text/html',
        'Content-Type': 'text/html'
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
    print("\n=== Response Details ===")
    print(f"URL: {context.response.url}")
    print(f"Status Code: {context.response.status_code}")
    print("Headers:", context.response.headers)
    print("Response Body (first 1000 chars):")
    print("-" * 50)
    print(context.response.text[:1000])
    print("-" * 50)
    assert context.response.status_code == status_code, \
        f"Expected status code {status_code}, but got {context.response.status_code}"

@then('the response should contain "{text}"')
def step_impl_body(context, text):
    assert text in context.response.text

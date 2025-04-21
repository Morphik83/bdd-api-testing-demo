import requests
from behave import when, then

@when('I send a GET request to "{endpoint}"')
def step_impl_get(context, endpoint):
    url = f"https://automationintesting.online{endpoint}"
    context.response = requests.get(url)

@then('the response status code should be {status_code:d}')
def step_impl_status(context, status_code):
    assert context.response.status_code == status_code

@then('the response should contain "{text}"')
def step_impl_body(context, text):
    assert text in context.response.text

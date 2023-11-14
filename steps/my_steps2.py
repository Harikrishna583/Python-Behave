# my_steps2.py
from behave import then
from bs4 import BeautifulSoup
from steps.common_steps import *

@then('I should see the expected result')
def step_impl(context):
    # Implement the verification steps here
    title = context.soup.title.text
    expected_title = 'Google'
    assert expected_title in title, f"Expected '{expected_title}', but found: {title}"

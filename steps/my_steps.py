# my_steps.py
from behave import when
import requests
from bs4 import BeautifulSoup
from steps.common_steps import *

@when('I perform some action')
def step_impl(context):
    # Implement the action steps here
    response = requests.get('https://google.com', verify=False)


    context.response = response
    context.soup = BeautifulSoup(response.content, 'html.parser')

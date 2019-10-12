from behave import *
from samuranium.steps import *

@step("I verify this method which is implemented in the project defined steps")
def verify_this_project_levelstep(context):
    samuranium = context.samuranium
    element = samuranium.find_element('Wikipedia')
    assert element.text == 'Wikipedia'


@when('I search for: "{keyword}"')
def wikipedia_main_page_search(context, keyword):
    search_box_selector = 'searchInput' # Id selector for the Search Input box
    # Notice that we don't need to specify if it's a css, xpath, id nor class selector,
    # Samuranium will handle this for us
    context.samuranium.input_text_on_element(keyword, search_box_selector)
    # Lets send an enter key to select the first result
    context.samuranium.press_enter_key()


@then('I verify the header of the page is: "{text}"')
def step_impl(context, text):
    heading_selector = 'firstHeading'
    heading_element = context.samuranium.find_element(heading_selector)
    heading_text = heading_element.text
    assert heading_text == text, 'Heading text expected: "{}", found: "{}"'.format(text, heading_text)
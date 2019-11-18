from behave import step

"""
This file contains common BDD methods that can be implemented by importing it like this:

```from samuranium.steps import *```
"""

@step('I navigate to the url: "{url}"')
def navigate_to_url(context, url):
    """
    Navigates to a given url

    Example:
        When I navigate to the url: "http://www.wikipedia.org"
    Args:
        context: behave context
        url: Url string
    """
    context.samuranium.navigate_to_url(url)


@step('I verify the title of the page is: "{title}"')
def verify_page_title(context, title):
    """
    Verifies the page title

    Example:
        Then I verify the title of the page is: "Wikipedia"
    Args:
        context: behave context
        title: Expected title string

    """
    actual_title = context.samuranium.get_title()
    assert actual_title == title, "Title does not match. Expected: '{}' - Found: '{}'".format(title, actual_title)


@step('I wait for element with selector: "{selector}"')
def wait_for_element(context, selector):
    """
    Wait for an element with the given selector

    Example:
        When I wait for element with selector: "js-link-box-en"
        Then I wait for element with selector: "js-link-box-en"
    Args:
        context: behave context
        selector: A string matching the intended web element

    """
    return context.samuranium.wait_for_element(selector)


@step('I click on element with selector: "{selector}"')
def click_on_element(context, selector):
    """
    Clicks on an element with the given selector

    Example:
        When I click on element with selector: "js-link-box-en"

    Args:
        context: behave context
        selector: A string matching the intended web element

    """
    context.samuranium.click_on_element(selector)


@step('I write text "{text}" on element with selector: "{selector}"')
def write_text_on_element(context, text, selector):
    """
     Writes text on an element with the given selector

    Example:
        When I write text "samuranium" on element with selector: "js-link-box-en"
    Args:
        context: behave context
        text: string with text to be written
        selector: A string matching the intended web element

    """
    context.samuranium.input_text_on_element(text, selector)


@step('I verify the text of element "{selector}" is "{text}"')
def verify_text_content(context, selector, text):
    """
     Verifies text on an element matches the given value

    Example:
        Then I verify the text of element ".EnglishLink" is "English"
    Args:
        context: behave context
        text: string with text to be matched
        selector: A string matching the intended web element
    """
    element_text = context.samuranium.find_element(selector).text
    assert element_text == text, 'Error: Expected: "{}" found "{}"'.format(text, element_text)



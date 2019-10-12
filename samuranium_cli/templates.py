env_file_string = """from behave import fixture, use_fixture
from samuranium import Samuranium
from samuranium.reporter import Reporter

@fixture
def set_browser(context):
    context.samuranium: Samuranium = Samuranium()
    context.browser = context.samuranium.get_browser()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()

def before_all(context):
    use_fixture(set_browser, context)

def after_all(context):
    Reporter(context)

    """

sample_feature_file_string = """
Feature: Browser Basic Interaction

  Scenario: Open the Browser and Navigate to a Given Page
    Given I navigate to the url: "http://www.wikipedia.org"
    And I wait for element with selector: "central-featured-logo"
    Then I verify the title of the page is: "Wikipedia"
    When I click on element with selector: "js-link-box-en"
    And I verify this method which is implemented in the project defined steps

  Scenario: This scenario will fail
    Given I navigate to the url: "http://www.wikipedia.org"
    And I wait for element with selector: "central-featured-logo"
    Then I verify the title of the page is: "Workopedia"
    # The step above fails since the title is obviously not "Workopedia" (It's a great name though!)
    When I click on element with selector: "js-link-box-en"
    And I verify this method which is implemented in the project defined steps
"""

sample_steps_file_string = """from behave import *
from samuranium.steps import *

@step("I verify this method which is implemented in the project defined steps")
def verify_this_project_levelstep(context):
    samuranium = context.samuranium
    element = samuranium.find_element('Wikipedia')
    assert element.text == 'Wikipedia'
"""
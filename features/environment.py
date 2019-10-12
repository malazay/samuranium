from behave import fixture, use_fixture
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

    
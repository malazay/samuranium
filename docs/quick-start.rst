Quick Start Guide
==================

************
Installation
************

- Create a new folder and setup a virtual environment with `pipenv  <https://pipenv.kennethreitz.org/en/latest/#install-pipenv-today>`_:
    1. ``$ mkdir example-project && cd example-project``

    2. ``$ pipenv shell``
- Add the samuranium depedency
    ``$ pipenv install samuranium``

*************
Project Setup
*************

You can setup A Samuranium project to work with BDD feature files (Behave).

The quickest way is to use the *Samuranium-cli* which is included in the Samuranium module.

On the root folder run the following command:

    ``$ create-samuranium-project``

This will create the basic files and folders that you need, and it will look like this:

::

    example-project
    ├── Pipfile
    ├── Pipfile.lock
    ├── features
    │   ├── environment.py
    │   ├── sample.feature
    │   └── steps
    │       └── steps.py

::

The file sample.feature includes some very basic scenarios that run on `Wikipedia <http://www.wikipedia.org>`_

You can run this straight away with the following command (be sure you are on the root folder of the project):

``$ behave``

On the *steps/steps.py* file, first we import all the files from *behave*, which allows us to implement the steps definitions.

Then we import all from *samuranium.steps*. This file contains several steps defined in the Samuranium module.

After that you can see some other implemented steps.


*******************************
Adding more scenarios and steps
*******************************
Lets create a new feature file on the *features* folder: **my_feature.feature**.

Then we will create another scenario for Wikipedia, but this time we will use the *search* input displayed in the
language selection page

- Open the feature file and add a new scenario:

.. code-block:: gherkin

    Feature: Wikipedia Samurai investigation
        To be a good Samurai, you need to understand what a Samurai is


        Scenario: Wikipedia landing page search box
            Given I navigate to the url: "http://www.wikipedia.org"
            When I search for: "samurai"
            Then I verify the header of the page is: "Samurai"



Now we just need to implement those steps in our steps file.
If you are using PyCharm, you can hover over any of the new steps until a *bulb* icon is displayed, and press it to
create all the step definitions.
Otherwise, you can just run the command **behave** command and it will output an error saying that if found non defined steps.

More information about how `Behave <https://behave.readthedocs.io/en/latest/>`_ works can be found `here <https://behave.readthedocs.io/en/latest/tutorial.html>`_

******************************
So lets implement those steps
******************************
Since we already have the first Step defined in *samuranium.steps*,

we just need to add two methods:
One for *When I search for: "samurai"* and one for *Then I verify the header of the page is: "Samurai"*

- Open the steps file: *feature/steps/steps.py*
- Add the following methods:

.. code-block:: python

    @when('I search for: "{keyword}"')
    def wikipedia_main_page_search(context, keyword):
        pass


    @then('I verify the header of the page is: "{text}"')
    def verify_header_text(context, text):
        pass

..

If you run behave now, it will run all the scenarios, including the old ones.
If we only want to test our new scenario, we can make use of the *"@tags"*, which allows to only run scenarios that match certain criterias.
More information about tags can be found `here <https://behave.readthedocs.io/en/latest/tutorial.html>`_

So, lets add a tag @search to our new scenario

.. code-block:: gherkin

    Feature: Wikipedia Samurai investigation
        To be a good Samurai, you need to understand what a Samurai is

        @search
        Scenario: Wikipedia landing page search box
            Given I navigate to the url: "http://www.wikipedia.org"
            When I search for: "samurai"
            Then I verify the header of the page is: "Samurai"


Now run the command like this:

``$ behave --tags=search``

The output should state that everything passed, but now we need to add real code to perform the intended steps!

.. code-block:: python

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

..

Now run the behave command again!

``$ behave --tags=search``

And that's it! super easy!

You can verify which :ref:`Steps <bundled-steps>` come bundled with Samuranium so you don't duplicate code.






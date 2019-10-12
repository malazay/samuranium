.. _bundled-steps:

Bundled Steps
======================================

****************
Using the steps
****************
This file contains common BDD methods that can be implemented by importing at top level of any step file in your project:

.. code-block:: python

    from samuranium.steps import *

..

.. note::
    Steps can be preceded (In general) by Given, When or Then. But the idea is to use them as follows:

    Given: On preconditions like: Given I navigate to some page

    When: On actions like: When I click on this

    Then: On assertions and verifications like: Then I verify this content is displayed

    This is only for improved readability, but it won't make the steps fail if you mix the Preceding statements

    For instance, "*Given* I navigate to some page" is the same as "*Then* I navigate to some page"

**************
Included steps
**************

.. automodule:: samuranium.steps
   :members:
   :undoc-members:
   :show-inheritance:
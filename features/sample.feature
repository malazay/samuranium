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

  @search
  Scenario: Wikipedia Search
    Given I navigate to the url: "http://www.wikipedia.org"
    When I search for: "samurai"
    Then I verify the header of the page is: "Samurai"

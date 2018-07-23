Feature: Google your way to documentation

  @browser @minor
  Scenario: The first result for Python behave should contain expected title
    Given I am on "index"
    When I type in "Behave Python"
    Then the results should contain "Welcome to behave!"

  @browser @chrome-only @critical
  Scenario: There should be no severe console log errors on index page
    Given I am on "index"
    When I check the console logs
    Then there should be no severe console log errors

Feature: Tests that should be run on every page

  @requests @minor
  Scenario: SEO Best practices insist you should have open graphs
    Given I get "index" with requests session
    Then it should have an og:title
      And the content attribute should not be empty
      And it should have an og:description
      And the content attribute should not be empty
      And it should have an og:image
      And the content attribute should not be empty
      And it should have an og:url
      And the content attribute should not be empty


  # @browser @chrome-only @normal @local-only
  # Scenario: SEO Best practices insist you should have open graphs info
  #   Given I am on "index"
  #   When I check for og:url
  #
  # @browser @chrome-only @normal @local-only
  # Scenario: SEO Best practices insist you should have Twitter Card info
  #   Given I am on "index"
  #   When I check for og:url
  #     And I check for twitter:card
  #     And I check for twitter:site
  #     And I check for twitter:image
  #
  # @validity @minor
  # Scenario: SEO Best practices insist you should have a favicon
  #   Given I am on "index"
  #   When I look for a favicon
  #
  # @browser @minor
  # Scenario: SEO Best practices insist you should have a canonical link even if it is to yourself
  #   Given I am on "index"
  #   When I look for a canonical link
  #
  #
  # @browser @minor
  # Scenario: Sites must have <!DOCTYPE html>
  #   Given I am on "index"
  #   When I look for a "<!DOCTYPE html>"
  #
  # @browser @minor
  # Scenario: Sites must have a lang attribute on their html
  #   Given I am on "index"
  #   When I look for a "<!DOCTYPE html>"
Feature: Website
  Scenario: Check website is up
    When I send a GET request to "/"
    Then the response status code should be 200
    And the response should contain "Restful-booker-platform demo"

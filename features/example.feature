Feature: Booking API
  Scenario: Get room information
    When I send a GET request to "/reservation/1"
    Then the response status code should be 200
    And the response should contain "roomName"

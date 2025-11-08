Feature: Booking API
  Scenario: Get booking information
    When I send a GET request to "/booking"
    Then the response status code should be 200
    And the response should contain "bookingid"

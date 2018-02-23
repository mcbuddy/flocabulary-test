Feature: As end user I want to login to Flocabulary

  Scenario: Success login using correct email and password
    Given I at flocabulary home page
    When I login using correct email and password
    Then I should logged in to Flocabulary
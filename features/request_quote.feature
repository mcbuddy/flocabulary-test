Feature: As end user I want to Request Quote from flocabulary

  Scenario: Request Quote on Flocabulary
    Given I existing and logged user
    When I request quote for my school
    Then I should get request quote
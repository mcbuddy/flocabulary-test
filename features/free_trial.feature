Feature: As end user I want to use free trial from flocabulary

  Scenario: Start Free Trial on Flocabulary
    Given I at flocabulary plan page
    When I start Free Trial session
    And I join flocabulary with email address
    Then I should get Free Trial session
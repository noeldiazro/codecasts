Feature: Present Codecasts

Scenario: Present No Codecasts
   Given there are no codecasts
     And user U is logged in
    When system presents codecasts for user U
    Then no codecasts are presented

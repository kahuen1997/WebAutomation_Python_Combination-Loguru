Feature: Login Online Platform

  Background:
    Given User opens the browser
    And User navigates to the HexSchool main page
    When User clicks the "Login to Course Platform" button
    And User clicks the "Teachable" link

  Scenario Outline: Check the login box
    When User enters the email <Email>
    And User enters the password <Password>
    And User clicks the Consent Button
    And User quits the browser
    Then The signup process should be completed successfully

    Examples:
      | Password  | Email                 |
      | John Doe  | john.doe@example.com  |
      | Alice Lee | alice.lee@example.com |
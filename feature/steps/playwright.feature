Feature: Login Online Platform

  Background:
    Given User opens the browser
    And User navigates to the HexSchool main page

  Scenario Outline:
    When User clicks the "Login to Course Platform" button
    And User clicks the "Teachable" link
    And User clicks the "Sign Up" button
    And User enters the full name <Full name>
    And User enters the email <Email>
    And User clicks the Consent Button
    And User quits the browser
    Then The signup process should be completed successfully

    Examples:
      | Full name | Email                 |
      | John Doe  | john.doe@example.com  |
      | Alice Lee | alice.lee@example.com |
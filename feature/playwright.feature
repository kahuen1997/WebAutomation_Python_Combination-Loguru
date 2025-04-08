Feature: Login Online Platform

  Background:
    Given User Open the Browser
    And User Open HexSchool Main Page

  Scenario Outline:
    When User click 登入課程平台
    And User click Teachable
    And User click sign up
    And User Enter the <Full name>
    And User Enter the <Email>
    And User CLick Consent Button and Quit

    Examples:
      | Full name | Email                 |
      | John Doe  | john.doe@example.com  |
      | Alice Lee | alice.lee@example.com |
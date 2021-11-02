@tag
Feature: Calculator

  Scenario: add two numbers
    Given Two input values, 1 and 2
    When I add the two values
    Then I expect the result 3

  Scenario Outline: add two numbers
    Given Two input values, <first> and <second>
    When I add the two values
    Then I expect the result <result>
    Examples:
      | first | second | result |
      | 1     | 12     | 13     |
      | -1    | 6      | 5      |
      | 2     | 2      | 4      |

  Scenario: reverse the number
    Given input value, 4
    When The action is rvs
    Then I want the result 0.25
#
  Scenario: sqrt the number
    Given input value, 4
    When The action is sqr
    Then I want the result 2
#
  Scenario Outline:
    Given input value, <Input>
    When The action is <opt>
    Then I want the result <result>
    Examples:
      | Input | opt | result |
      | 4     | rvs | 0.25   |
      | 4     | sqr | 2      |
      | 36    | sqr | 6      |

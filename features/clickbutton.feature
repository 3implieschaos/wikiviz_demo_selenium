Feature: ClickButton

  Scenario: Click Away From Homepage
    Given I navigate to the Home page
    And I see that the pagename is WikiViz
    And I see the header "Hello World!"
    When I click the button
    Then I see that the pagename is no longer WikiViz
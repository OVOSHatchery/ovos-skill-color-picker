Feature: Get information about a colour
 
 Scenario: Ask for specific colour
   Given an english speaking user
    When the user says "show me the colour red"
    Then mycroft should reply "here is a lovely shade of red"

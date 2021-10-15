Feature: Get information about a color
 
  Scenario Outline: Ask for specific color
    Given an english speaking user
     When the user says "<request a color>"
     Then mycroft reply should contain "here is a lovely shade of <color>"

    Examples: requesting a color
      | request a color | color |
      | show me the color red | red |
      | what does yellow look like | yellow |
      | show me dark salmon | dark salmon |
      | what does light golden rod yellow look like | light golden rod yellow |

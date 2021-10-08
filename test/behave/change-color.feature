Feature: Change the colour

  @xfail 
  Scenario Outline: Change color by specified amount
    Given an english speaking user
      And the active color is set to <pre-color>
     When the user says "<change request>"
     Then the active color changes to <post-color>
      And mycroft should report the color as the RGB values
  
    Examples: color changes by specified amount
      | pre-color | change request | post-color |
      | #000000 | increase the red level by 20% | #330000 |
      | #ffffff | decrease the blue level by 32 | #ffffdf |

  @xfail 
  Scenario Outline: Change color without specifying amount
    Given an english speaking user
      And the active color is set to <pre-color>
     When the user says "<change request>"
     Then the active color changes to <post-color>
      And mycroft should report the color as the RGB values
  
    Examples: color changes without specifying amount
      | pre-color | change request | post-color |
      | #000000 | increase the red level | #140000 |
      | #ffffff | decrease the blue level | #ffffeb |
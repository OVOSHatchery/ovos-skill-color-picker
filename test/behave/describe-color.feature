Feature: Describe a color

  @xfail 
  Scenario Outline: Report the name of a known color
    Given an english speaking user
     When the user asks "<utterance>"
     Then mycroft should report the color as <color name>
  
    Examples: Request known color name
      | utterance | color name |
      | what color is #000000 | black |
      | what color is #ffffff | white |
      | what color is #fa8072 | salmon |
      | what color is #d2691e | chocolate |

  @xfail 
  Scenario Outline: Report the name of an unknown color
    Given an english speaking user
     When the user asks "<utterance>"
     Then mycroft should report the color as <color name>
  
    Examples: Request unknown color name
      | utterance | color name |
      | what color is #FEE255 | yellow |
      | what color is 254 226 85 | yellow |
      | what color is #222222 | nearly black |
      | what color is 17 17 17 | nearly black |
      | what color is #8CE0FE | light blue |
      | what color is #6C7A89 | dark grey |

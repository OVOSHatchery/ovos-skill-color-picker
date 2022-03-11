Feature: Get information about a color
 
  Scenario Outline: Ask for specific color by name
    Given an english speaking user
     When the user says "<request a color>"
     Then mycroft reply should contain "<color name> has a hex value of <hex-value>. In R. G. B. this is Red <red-value>, Green <green-value>, Blue <blue-value>"

    Examples: requesting a color
      | request a color | color name | hex-value | red-value | green-value | blue-value |
      | show me the color red | red | F. F. 0. 0. 0. 0 | 255 | 0 | 0 |
      | what does the color yellow look like | yellow | F. F. F. F. 0. 0 | 255 | 255 | 0 |
      | show me the color dark salmon | dark salmon | E. 9. 9. 6. 7. A | 233 | 150 | 122 |
      | what does the color light goldenrod yellow look like | light goldenrod yellow | F. A. F. A. D. 2 | 250 | 250 | 210 |

  Scenario Outline: Ask for color by hex value with known name
    Given an english speaking user
     When the user says "<request by hex>"
     Then mycroft reply should contain "That is <color name>. Its R. G. B. values are, Red <red-value>, Green <green-value>, Blue <blue-value>"

    Examples: requesting a color by hex
      | request by hex | color name | red-value | green-value | blue-value |
      | what color has a hex code of ff0000 | red | 255 | 0 | 0 |
      | what color has a hex code of e9967a | dark salmon | 233 | 150 | 122 |

  Scenario Outline: Ask for color by hex value with unknown name
    Given an english speaking user
     When the user says "<request by hex>"
     Then mycroft reply should contain "The R. G. B. values for this color are, Red <red-value>, Green <green-value>, Blue <blue-value>"

    Examples: requesting a color by hex
      | request by hex | red-value | green-value | blue-value |
      | what color has a hex code of ff0001 | 255 | 0 | 1 |
      | what color has a hex code of fadfad | 250 | 223 | 173 |

  Scenario Outline: Ask for color by RGB values with known name
    Given an english speaking user
      When the user says "<request by RGB>"
      Then mycroft reply should contain "<hex-value>"

    Examples: requesting a color by RGB value
      | request by RGB | color name | hex-value |
      | what color has an RGB value of 255 0 0 | red | F. F. 0. 0. 0. 0 |
      | what color has an RGB value of 233 150 122 | dark salmon | E. 9. 9. 6. 7. A |

  Scenario Outline: Ask for color by RGB values with unknown name
    Given an english speaking user
      When the user says "<request by RGB>"
      Then mycroft reply should contain "<hex-value>"

    Examples: requesting a color by RGB value
      | request by RGB | hex-value |
      | what color has an RGB value of 255 0 1 | F. F. 0. 0. 0. 1 |
      | what color has an RGB value of 250 223 173 | F. A. D. F. A. D |


